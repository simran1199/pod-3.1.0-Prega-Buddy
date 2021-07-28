from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template('landingPage.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')

# all the routes go here


@socketio.on('message')
def handleMsg(msg):
    #print('Message: ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
