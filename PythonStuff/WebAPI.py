from flask import request, Flask, jsonify
import os
from player import Player
from card import Card
import driver

url = 'https://localhost:5000'

@app.route('/startgame', methods=['POST'])
def addOne():
    received = request.get_json()
    print(received)
    return jsonify("Game Started")

#if python WebAPI.py is called
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000, ssl_context='adhoc')


