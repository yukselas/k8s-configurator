from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from shelljob import proc



app = Flask(__name__)
Bootstrap(app)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///k8s_configurator.db' 
# app.config['SQLALCHEMY_ECHO'] = True

from app import initdb   
 
from app import routes

if __name__ == "__main__":
    app.run(debug=True)



