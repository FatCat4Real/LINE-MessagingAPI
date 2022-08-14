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

app = Flask(__name__)

id_1='VlkGmtf89SV460/d/Bqchx4TqssECi9bwuQkxINvPIuN+HN0VzxIf7nlwM9wxGF+LotgiPflAWsMIph5UT9/i43YfrmDK4csMvG3trr6nLUvfd+P2EpBNZUxdFWHcfwMHogJh+TiWKbODpW/ojnqqQdB04t89/1O/w1cDnyilFU='
id_2='869a0bcabfb772d23057a021509aa213'

line_bot_api = LineBotApi(id_1)
handler = WebhookHandler(id_2)




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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
