from flask import Flask, jsonify
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

# Define more routes if needed

def handler(event, context):
    return DispatcherMiddleware(app, {
        '/.netlify/functions/flask_app': app
    }).__call__(event, context)
