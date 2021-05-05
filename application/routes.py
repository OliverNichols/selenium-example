from flask import redirect, url_for, render_template, request

from application import app, db
from application.models import Games
from application.forms import BasicForm

@app.route('/')
@app.route('/<error>')
def index(error=None):
    form = BasicForm()

    history = Games.query.order_by(Games.id.desc()).limit(5).all()

    return render_template('index.html', form=form, history=history, error=error)

@app.route('/add', methods=['POST'])
def add():

    name = request.form.get('name', '')
    error = None

    if name.strip() == '':
        error = "The name field can't be empty!"

    elif len(name) > 30: 
        error = "This name is too long!"

    else:
        new_game = Games(name=name)
        db.session.add(new_game)
        db.session.commit()

    return redirect(url_for('index', error=error))