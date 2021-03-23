from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc

app = Flask(__name__)
Bootstrap(app)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

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


