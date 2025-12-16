from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

