from flask import Flask
from flask import request
from time import time
import hashlib
import templet

import xml.etree.ElementTree as et

import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '123'

@app.route('/weixin',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        my_signature = request.args.get('signature')
        my_timestamp = request.args.get('timestamp')
        my_nonce = request.args.get('nonce')
        my_echostr = request.args.get('echostr')

        token = 'creak'

        data = [token,my_timestamp,my_nonce]
        data.sort()

        temp = ''.join(data)

        mysignature = hashlib.sha1(temp).hexdigest()

        if my_signature ==mysignature:
            return my_echostr
        else:
            return ''

    if request.method == 'POST':
        xml_data = request.stream.read()
        xml_rec = et.fromstring(xml_data)

        ToUserName = xml_rec.find('ToUserName').text
        fromUser = xml_rec.find('FromUserName').text
        MsgType = xml_rec.find('MsgType').text
        Content = xml_rec.find('Content').text
        MsgId = xml_rec.find('MsgId').text

        Content = random.choice(['cnm','nmb','ngsb'])
            

        return templet.reply_templet(MsgType) % (fromUser, ToUserName, str(int(time())), Content)



if __name__ == '__main__':
    app.run()
