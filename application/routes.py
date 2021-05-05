from flask import redirect, url_for, render_template, request

from application import app, db
from application.models import Games
from application.forms import BasicForm

@app.route('/')
def index():
    form = BasicForm()

    history = Games.query.order_by(Games.id.desc()).limit(5).all()

    return render_template('index.html', form=form, history=history)

@app.route('/add', methods=['POST'])
def add():
    new_game = Games(name=request.form.get('name'))
    
    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))