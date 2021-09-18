from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def drawInitialBoard(boardWidth = None, boardLength = None):
    return render_template('index.html', boardWidth = 8, boardLength = 8)

@app.route('/4')
def draw8By4Board(boardWidth = None, boardLength = None):
    return render_template('index.html', boardWidth = 8, boardLength = 4)

@app.route('/<int:x>/<int:y>')
def drawbyInput(x, y):
    return render_template('index.html', boardWidth = x, boardLength = y)

if __name__ == "__main__":
    app.run(debug=True)

