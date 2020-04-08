from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/instructions')
def instructions():
    return render_template('Instructions.html')


@app.route('/moves')
def moves():
    return render_template('Moves.html')


@app.route('/progress_table')
def progress_table():
    return render_template('Progress_Table.html')


@app.route('/car_bodies')
def car_bodies():
    return render_template('Car_Bodies.html')


@app.route('/items')
def items():
    return render_template('Items.html')


@app.route('/rlcs')
def rlcs():
    return render_template('RLCS.html')


@app.route('/best_teams')
def best_teams():
    return render_template('Best_Teams.html')


if __name__ == '__main__':
    app.run()
