"""
pip install protobuf
pip install google
sudo apt install python-protobuf
protoc -I . --python_out=. Message.proto
"""
import time

from flask import Flask, jsonify, make_response
from flask_sockets import Sockets

from service.Message_pb2 import WSMessage

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/ohmypoker')
def foo0(ws):
    while not ws.closed:
        # now = datetime.datetime.now().isoformat() + 'Z'
        message_client = ws.receive()
        message = WSMessage()
        message.ParseFromString(message_client)

        ws.send( message.SerializeToString() )
        # ws.send(now)  # 发送数据
        time.sleep(1)


@app.route('/test0', methods=['POST'])
def foo1():
    rst = make_response(jsonify({'2': 2}))
    rst.headers['Access-Control-Allow-Origin'] = 'http://localhost:7456'
    rst.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    rst.headers['Access-Control-Max-Age'] = '86400',
    rst.headers['Access-Control-Allow-Credentials'] = 'true'
    rst.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    rst.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    rst.headers[
        'Access-Control-Allow-Headers'] = 'Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With'

    return rst


@app.route('/test')
def foo2():
    rst = make_response(jsonify({'1': 2}))
    rst.headers['Access-Control-Allow-Origin'] = 'http://localhost:7456'
    rst.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST'
    rst.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    rst.headers['Access-Control-Max-Age'] = '86400',
    rst.headers['Access-Control-Allow-Credentials'] = 'true'
    rst.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    rst.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    rst.headers[
        'Access-Control-Allow-Headers'] = 'Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With'

    return rst


@app.route('/get_serverinfo')
def foo3():
    return 1
    ###直接渲染文件内容,或作为附件

    # rst = make_response(jsonify( {'version':123}))
    # rst.headers['Access-Control-Allow-Origin'] = '*'
    # return rst


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('0.0.0.0', 4000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
