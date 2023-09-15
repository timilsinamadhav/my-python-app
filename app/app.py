from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO DEVOPS CLASS'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

