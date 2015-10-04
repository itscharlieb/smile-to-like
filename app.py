#!/usr/bin/env python 
from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
from instagram.client import InstagramAPI
import requests
import indicoio

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



def get_instagram():
	media_feed, next = api.user_media_feed(count=10)
	data = {}
	usernames = []
	dates = []
	descriptions = []
	prof_photos = []
	photos = []
	num_likes = []
	indexer = []
	for media in media_feed:
		descriptions.append(media.caption.text)
		photos.append(media.get_standard_resolution_url())
		usernames.append(media.user.username)
		num_likes.append(media.likes.count)
		prof_photos.append(media.user.profile_picture)
	data['photos'] = photos
	data['descriptions'] = descriptions
	data['num_likes'] = num_likes
	data['usernames'] = usernames
	data['prof_photos'] = prof_photos
	for x in xrange(0,10):
		print x
		indexer.append(x)
	data['indexer'] = indexer
	return data


@app.route('/')
def index():
	print "hi"
	data = get_instagram()
	return render_template('index.html', **data)

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/get_test', methods=['POST'])
def get_test():
    data = request.get_json(force=True)
    sentiment = indicoio.fer(data['uri'])
    return jsonify(sentiment)

def pageNotFound(e):
  """ Handle 404 errors """
  return render_template('404.html'), 404

@app.errorhandler(405)
def serverNotFound(e):
  """ Handle 404 errors """
  return render_template('404.html'), 405


if __name__ == '__main__':
    indicoio.config.api_key = '3e8805a619346600f1e5954226208e00'
    app.run(debug=True)
