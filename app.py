from flask import Flask, request, abort
#flask是用來建網站套件
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('2pmBcwuJKJ3MIAKlh4Td7YfJfaOiULwz8BYCd7nbigEPKfEmGrglSgVg7JEwOi94uuOLr5BJNx9L3MT4CA+DbyoqxTHGDA16rMuVLl+KDpNm9jJgTotIqY6uO9Ro6fWBCeBfyv5CdWNWP/PkM531EQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('752bf3c50b8e256a08ae58fb916df958')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '你吃飯了嗎？'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=))


if __name__ == "__main__":
    app.run()