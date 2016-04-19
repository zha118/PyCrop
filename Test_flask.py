# -*- coding: utf-8 -*-

# author Gang Zhao, gang.zhao3@bayer.com
from flask import Flask
app = Flask(__name__)

@app.route('/test_flask')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
    
    
    
    