
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/AreaSquare")
def areasq():
    return render_template('areasquare.html')

@app.route("/AreaRectangle")
def arearec():
    return render_template('arearec.html')

@app.route("/AreaCircle")
def areacirc():
    return render_template('areacirc.html')

@app.route("/AreaTriangle")
def areatri():
    return render_template('areatri.html')

@app.route("/VolumeCube")
def volcube():
    return render_template('volcube.html')

@app.route("/VolumeRectangularPrism")
def volrecprism():
    return render_template('volrectpris.html')

@app.route("/VolumeSphere")
def volsphe():
    return render_template('volspher.html')

@app.route("/PythagoreanTheoremSides")
def pysides():
    return render_template('pyththeoside.html')

@app.route("/FindThirdAngle")
def thirdangle():
    return render_template('thirdangle.html')

@app.route("/CompSupAngles")
def compsup():
    return render_template('compsupangles.html')


if __name__ == '__main__':
    app.run(debug=True)