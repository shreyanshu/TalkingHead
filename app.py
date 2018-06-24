from flask import Flask, render_template
import DemoMain
import DemoRealTime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/play')
def hello():
    DemoMain.run()
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


