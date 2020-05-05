import io
from flask import Flask, render_template, Response
from model import Predict
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/plot/<stock>/<interval>/<hidden>/<iterations>/<tolerance>')
def plot(stock, interval, hidden, iterations, tolerance):
    data = Predict(stock, interval, int(hidden), int(iterations), float(tolerance))

    figure = data.predictionGraph()
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



if __name__ == "__main__":
    app.run(debug=True)