from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os

app = Flask(__name__)

line_bot_api = LineBotApi(
    'F+JuK+abskhFzrJHfIKoxh/IZc3B+cINRk7GBYWDc3qKVGPkmL5cnSSmgT0Ef9cSqT0Es0todCdMFeALCNjdX7f1q+J1GoTw5GJ6bZX7k/TLuy2PdO509OMem2zFa9hYKUBO2rx5jiuvr9tuAZmpQQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66ca26000500a514b397557c3e7bb4e1')

line_bot_api.push_message('U3181e6f68900069d013696dfdb239d08', TextSendMessage(text='你可以開始了'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    #
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    line_bot_api.reply_message(event.reply_token, TextSendMessage(message))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
