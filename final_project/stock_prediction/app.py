import io
from flask import Flask, render_template, Response, request, redirect, url_for
from model import Predict
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


app = Flask(__name__)

@app.route('/home', methods=["GET", "POST"])
@app.route('/')
def index():
    if request.method == "POST":
        ticker = request.form.get("ticker")
        interval = request.form.get("interval")
        iterations = request.form.get("iterations")
        tolerance = request.form.get("tolerance")
        layers = request.form.get("layers")

        return redirect(url_for('post/+ /ticker + /interval + /iterations + /tolerance + /layers'))

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