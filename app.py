from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ks8_configurator.db' 


db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'Go to next step!'     
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


