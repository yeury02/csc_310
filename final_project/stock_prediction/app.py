from flask import Flask, render_template
from model import Predict

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/plot/<stock>/<interval>/<hidden>/<iterations>/<tolerance>')
def plot(stock, interval, hidden, iterations, tolerance):
    

if __name__ == "__main__":
    app.run(debug=True)