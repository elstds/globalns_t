from flask import render_template, redirect, url_for
from app import app
from app.forms import RegistrationForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():

        return redirect(url_for('success_registration'))
    return render_template('index.html', title='Зарегистрируйтесь', form=form)

@app.route('/success', methods=['GET', 'POST'])
def success_registration():
    return render_template('success.html')