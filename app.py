from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import subprocess
app = Flask(__name__)
Bootstrap(app)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'Go to next step!'    
    return render_template('index.html')

@app.route('/run')
def terminal():
    return
if __name__ == "__main__":
    app.run(debug=True)