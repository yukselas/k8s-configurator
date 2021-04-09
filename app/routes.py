
from app import app
from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc

from app.dbmodel import *

#from app.dbmodel import db

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
            if key in ["ipblockstart","ipblockend","netmask","gateway"]:
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
    configlist=k8sconfig.query.all()
    return render_template('step-2-ip-configuration.html', ipblockstart=ipblockstart, ipblockend=ipblockend, netmask=netmask, gateway=gateway ) 
     

@app.route('/step-3/review-configuration', methods=['GET', 'POST'])
def step3():
    if request.method == 'POST':
        return 'Go to next step!'     
    return render_template('step-3-review-configuration.html')  

@app.route('/step-4/perform-installation', methods=['GET', 'POST'])
def step4():
    if request.method == 'POST':
        return 'Go to next step!'     
    return render_template('step-4-perform-installation.html') 


@app.route( '/stream' )
def stream():
    g = proc.Group()
    p = g.run( [ "bash", "test.sh" ] )

    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield "data: " +str(line) +"\n\n"

    return Response( read_process(), mimetype= 'text/event-stream' )
