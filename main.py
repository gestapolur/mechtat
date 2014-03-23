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
def show_main_page():
    redis_conn = redis.StrictRedis(host=REDIS_URL, port=REDIS_PORT)
    post_list = redis_conn.lrange("post_list", 0, -1)
    if post_list:
        return render_template('index.html',
                               post_list=post_list)
    else: # @todo: for test use
        return render_template('index.html',
                               post_list=["Test article 1",
                                          "Test article 2",
                                          "Test article 3"])
        
    return render_template('index.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = redis.StrictRedis(
        host=REDIS_URL, port=REDIS_PORT).get("post:%d" % post_id)
    if post:
        post = json.loads(post)
        return render_template(
            'post.html',
            time=datetime.datetime.fromtimestamp(
                int(post["time"])).strftime("%x %X"),
            title=post["title"],
            text=post["text"])
    return "Post not found."
