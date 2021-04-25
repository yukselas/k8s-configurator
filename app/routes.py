
from app import app
from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc
from cidrize import cidrize
from app.dbmodel import *
import os

#from app.dbmodel import db

'''Usage:
    getrange('<range>','<percent>','<exclude-last-X-items>')
'''
def getrange(iprange,percent,excludelast):
    startip=iprange.split('-')[0]
    start=startip.split('.')[3]
    endip=iprange.split('-')[1]
    end=endip.split('.')[3]
    prefix=startip.split('.')[0]+'.'+startip.split('.')[1]+'.'+startip.split('.')[2]+'.'
    iplist=[]
    for ip in range(int(start),int(end)+1):
        iplist.append(ip)
    iplist=iplist[0:(-1*excludelast)]
    c=len(iplist)
    sc=float(c*percent/100)
    se=float(c*(100-percent)/100)
    #print(c)
    #print(sc)
    #print(se)
    i=0
    firstipblock=[]
    secondipblock=[]
    for ip in iplist:
        if i<sc:
            firstipblock.append(prefix+str(ip))
        else:
            secondipblock.append(prefix+str(ip))
        i=i+1
    #print(iplist)
    #print(firstipblock)
    #print(secondipblock)
    return firstipblock[0]+'-'+firstipblock[-1], secondipblock[0]+'-'+secondipblock[-1]



def genmultusnetstr(nvriprange,iprange,gateway):
    mycidr=str(cidrize(iprange)[0])
    multusnet=nvriprange+','+mycidr+','+gateway
    return multusnet

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gelen=''
        for key in request.form:
            if key in ["repourl","installtype"]:
                check = k8sconfig.query.filter_by(name=str(key)).first()                
                if check:                    
                    check.config=str(request.form[key])   
                    print(str(key)+' == '+str(request.form[key])+' updated!')        
                    db.session.commit()  
            else:                      
                check = isimModule.query.filter_by(name=str(key)).first()                
                if check:                    
                    check.val=str(request.form[key])            
                    db.session.commit()  

                      
            gelen+=str(key)+"="+request.form[key]+"<br>"
        return gelen
     
       
     
    repourl=str(k8sconfig.query.filter_by(name='repourl').first().config)
    installtype=str(k8sconfig.query.filter_by(name='installtype').first().config)
    radioonline=''
    radiooffline=''
    if installtype == 'online':
        radioonline='checked'
    if installtype == 'offline':
        radiooffline='checked'
    modulelist=isimModule.query.all()
    configlist=k8sconfig.query.all()
    return render_template('index.html', modulelist=modulelist, ham=str(modulelist), repourl=repourl, onlinechecked=radioonline, offlinechecked=radiooffline)

@app.route('/step-2/ip-configuration', methods=['GET', 'POST'])
def step2():
    global db
    if request.method == 'POST':
        gelen=''
        for key in request.form:
            if key in ["ipblockstart","ipblockend","netmask","gateway","nvr1","nvr2","nvr3"]:
                check = k8sconfig.query.filter_by(name=str(key)).first()                
                if check:                    
                    check.config=str(request.form[key])           
                    db.session.commit()                        
            gelen+=str(key)+"="+request.form[key]+"<br>"
        return gelen
    ipblockstart=str(k8sconfig.query.filter_by(name='ipblockstart').first().config)
    ipblockend=str(k8sconfig.query.filter_by(name='ipblockend').first().config)
    netmask=str(k8sconfig.query.filter_by(name='netmask').first().config)
    gateway=str(k8sconfig.query.filter_by(name='gateway').first().config)
    nvr1val=str(k8sconfig.query.filter_by(name='nvr1').first().config)
    nvr2val=str(k8sconfig.query.filter_by(name='nvr2').first().config)
    nvr3val=str(k8sconfig.query.filter_by(name='nvr3').first().config)
    modulelist=isimModule.query.all()
    configlist=k8sconfig.query.all()
    # create first block from %20, exclude last 3 items
    firstrange, secondrange = getrange(ipblockstart+'-'+ipblockend,20,3)
    metallbconf='''apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: isim-static-ip-space
      protocol: layer2
      addresses:
      - '''+firstrange+'''
      auto-assign: false
    - name: isim-ip-space
      protocol: layer2
      addresses:
      - '''+secondrange

    return render_template('step-2-ip-configuration.html', metallbconf=metallbconf, modulelist=modulelist, ipblockstart=ipblockstart, ipblockend=ipblockend, netmask=netmask, gateway=gateway, nvr1val=nvr1val, nvr2val=nvr2val, nvr3val=nvr3val ) 
     

@app.route('/step-3/perform-installation', methods=['GET', 'POST'])
def step3():
    runcmd=False
    commands=''

    if request.method == 'POST': 
        commandsarr=str(request.form['commands']).split('\r\n')
        commands=str(request.form['commands'])
        runfile='/tmp/installer-batch-script.sh'
        os.system('echo>'+runfile)
        f=open(runfile,'a', encoding='utf-8')
        for line in commandsarr:
            f.write(line.strip()+"\n")
        f.write("\necho exit; exit 0")
        f.close()
        os.chmod(runfile, 0o755)
        runcmd=True
    repourl=str(k8sconfig.query.filter_by(name='repourl').first().config) 
    return render_template('step-3-perform-installation.html', runcmdstr=str(runcmd), runcmd=runcmd, commands=commands, repourl=repourl)



@app.route( '/step-3/stream')
def stream():
    mycmd=[]
    cwd=os.getcwd()
    repourl=request.args['repourl']    

    #return str(mycmd)
    g = proc.Group()
    p = g.run( ["bash", "/tmp/installer-batch-script.sh"])


    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield "data: " +str(line) +"\n\n"

    return Response( read_process(), mimetype= 'text/event-stream' )
