from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy import create_engine


app = Flask(__name__)
Bootstrap(app)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ks8_configurator.db' 


db = SQLAlchemy(app)
class k8sconfig(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True) # name bos birakilabilir
    config = Column(Text , nullable=True) # name bos birakilabilir
    version = Column(Integer)
    def __repr__(self):
        return '<Name %r>' % self.name    

engine = create_engine('sqlite:///ks8_configurator.db')

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        check = k8sconfig.query.filter_by(name='ayse updated!').first()
        if check == None:
            conf = k8sconfig()
            conf.name='ayse'
            conf.config='123'
            conf.version=1
            db.session.add(conf)
            db.session.commit()
        else:
            check.name='ayse'
            check.config='123'
            check.version=1
            db.session.commit()                    
        return 'Go to next step! 1'     
    return render_template('index.html')

@app.route('/step-2/ip-configuration', methods=['GET', 'POST'])
def step2():
    if request.method == 'POST':
        return 'Go to next step!'     
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

if __name__ == "__main__":    
    app.run(debug=True)



