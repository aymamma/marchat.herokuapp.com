import flask
import flask_socketio
from flask_socketio import SocketIO

app = flask.Flask(__name__, static_url_path="/web")

socketio = SocketIO(app)


@app.route("/")
def index():
    return flask.send_from_directory("web", "index.html")


@socketio.on("connect")
def onconnect():
    print("Client connected")


@socketio.on("message")
def onmessage(msg):
    if isinstance(msg, str):
        flask_socketio.emit("chatmsg", msg, broadcast=True)
        print(msg)
    else:
        print(type(msg))
        flask_socketio.emit("d", msg)


socketio.run(app, host="0.0.0.0", port=80)
