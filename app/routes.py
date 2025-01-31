from flask import render_template, redirect, url_for
import sqlalchemy as sa
import sqlalchemy.orm as so

from app import app, db
from app.forms import RegistrationForm
from utils import send_querry
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        number = form.phone_number.data
        user = User(name=name, phone_number=number)
        db.session.add(user)
        db.session.commit()
        response = send_querry(number, name)
        if response.get('uuid'):

            return redirect(url_for('success_registration'))

    return render_template('index.html', title='Зарегистрируйтесь', form=form)

@app.route('/success')
def success_registration():
    return render_template('success.html')