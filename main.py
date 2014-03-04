import json
import logging
import datetime
import traceback
import time

import requests
import redis
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory

# BEANSTALK_URL = '192.168.1.29'
# BEANSTALK_TUBE = 'test-work-request'

app = Flask(__name__)
app.config['DEBUG'] = True

logger = logging.getLogger('mechtat')
logger.setLevel(logging.INFO)


@app.route('/', methods=['POST', 'GET'])
def test():
    return render_template('index.html',
                           time=time.time())
