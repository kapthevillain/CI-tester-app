from flask import Flask, jsonify
import os

greeting = {'Port':os.environ['FLASK_PORT'], 'Environment':os.environ['ENV'], '👋':'🌎'}

api = Flask(__name__)
# Simple REST endpoint
@api.route('/', methods=['GET'])
def hello():
    return jsonify(greeting)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=os.environ['FLASK_PORT'])

