from flask import Flask
import getmtadata

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = getmtadata.getmtadata("L", "L16N")
    return result
