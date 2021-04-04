
from app import app
from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc

from app.dbmodel import *

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gelen=''
        for key in request.form:
            if key in ["repourl","installtype"]:
                pass
            else:                      
                check = isimModule.query.filter_by(name=str(key)).first()                
                if check:                    
                    check.val=str(request.form[key])
                    print(1)                
                    db.session.commit()  

                      
            gelen+=str(key)+"="+request.form[key]+"<br>"
        return str(gelen)
        # check = k8sconfig.query.filter_by(name='ayse updated!').first()
        # if check == None:
        #     conf = k8sconfig()
        #     conf.name='ayse'
        #     conf.config='123'
        #     conf.version=1
        #     db.session.add(conf)
        #     db.session.commit()
        # else:
        #     check.name='ayse'
        #     check.config='123'
        #     check.version=1
        #     db.session.commit()               
        # return 'Go to next step! 1'  
     
    modulelist=isimModule.query.all()              
    return render_template('index.html', modulelist=modulelist, ham=str(modulelist))

@app.route('/step-2/ip-configuration', methods=['GET', 'POST'])
def step2():
    if request.method == 'POST':
        hello = request.form.getlist('modules[]')
        
        return 'Go to next step!' + str(request.form) + "<br>Start: " +str(hello)
    return render_template('step-2-ip-configuration.html')    

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
