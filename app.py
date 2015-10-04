#!/usr/bin/env python 
from flask import Flask, render_template, request, url_for, redirect, make_response
from instagram import client

app = Flask(__name__)

client_id = 'b8e0e0bf4c214c9f920bc630374b27b3'
client_secret = 'b5c36307fef8432b9233d6ab436b3b18'
redirect_uri = 'http://localhost:5000/oauth_callback'


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():

	return render_template('test.html')

@app.route('/test2')
def test2():
	return render_template('test2.html')

@app.route('/get_test', methods=['GET'])
def get_test():
    print request.get_json(force=True)







if __name__ == '__main__':
  app.run(debug=True)