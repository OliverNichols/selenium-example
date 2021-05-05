from flask import redirect, url_for, render_template, request

from application import app, db
from application.models import Games
from application.forms import BasicForm

@app.route('/')
@app.route('/<error>')
def index(error=None):
    form = BasicForm(request.form)

    history = Games.query.order_by(Games.id.desc()).limit(5).all()
    return render_template('index.html', form=form, history=history, error=error)

@app.route('/add', methods=['POST'])
def add():
    form = BasicForm(request.form)

    if form.validate_on_submit():
        db.session.add(Games(name=form.name.data))
        db.session.commit()

    error = next(iter(form.name.errors), None)
    return redirect(url_for('index', error=error))