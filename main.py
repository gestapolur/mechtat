# -*- coding: utf-8 -*-
"""
Copyright 2014, Gestalt LUR. All rights reserved.

A simple Blog framework.

"""

import json
import logging
import datetime
import time
import os

import requests
import redis
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory

REDIS_URL = os.environ.get("REDIS_URL")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def test():
    return render_template('index.html',
                           time=time.time())

@app.route('/post')
def hello():
    return "hello %s" % str(int(time.time()))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    redis_conn = redis.StrictRedis(host=REDIS_URL, port=REDIS_PORT)
    post = redis_conn.get("post:%d" % post_id)
    return post
