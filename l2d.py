from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import requests

import os
import json

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['pxtWV+1/jdVPs9tRXpxzwsndJpxkuGbLSwiOJyPWF/NLwfVHR0ZWy2RCUpLi2iZyX0j1QtBhTs0pTyCWiXZ9qI2oLfGqenC+t9/p0ZlMxJxbXCPbQH8X/7La+DA9CyZd2ezuH2DQ1UT8PDMyxAUxxAdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['b3eae7c2febd15b0054199a3ce6ab266'])

discord_webhook = os.environ['https://discord.com/api/webhooks/952110323442266153/lG68Z6xxxd0GJO5CJcfjz3lkZkMGb_nUWI81_VoAVhDZA8jT7Cb_s2-RmzmhqVM_Cuw8']

@app.route("/")
def root():
    return 'OK'

@app.route("/callback",methods=['POST'])
def callback():
    sign = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, sign)
    except InvalidSignatureError:
        print("Invalid signature. Check token and/or secret")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    content = event.message.text
    content += "\n" + str(event)
    profile = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)
    request_data = {
        "content":event.message.text,
        "username":profile.display_name + " from LINE",
        "avatar_url":profile.picture_url
    }
    requests.post(url=discord_webhook,data=request_data)

if __name__ == "__main__":
    app.run()