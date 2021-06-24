# Import Flask dependency
from flask import Flask

#Create a new Flask App instance
app = Flask(__name__)

#Create Flask Routes
## Defining starting point (root)
@app.route('/')
def hello_world():
    return 'Hello World'