#!/usr/bin/env python 
from flask import Flask, render_template, request, url_for, redirect, make_response
from instagram.client import InstagramAPI

app = Flask(__name__)

client_id = 'b8e0e0bf4c214c9f920bc630374b27b3'
client_secret = 'b5c36307fef8432b9233d6ab436b3b18'
redirect_uri = 'http://localhost:5000/oauth_callback'
access_token = '2222183970.b8e0e0b.d7f43b7e651a46fbbf0b1b71e40fb217'

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
# popular_media = api.media_popular(count=20)
# for media in popular_media:
#     print media.images['standard_resolution'].url

# media_feed, next = api.user_media_feed()
# photos = []
# for media in media_feed:
# 	print media.get_standard_resolution_url()
	# photos.append('<img src="%s"/>' % media.get_standard_resolution_url())

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/get_test', methods=['GET'])
def get_test():
    print request.get_json(force=True)





if __name__ == '__main__':
  app.run(debug=True)