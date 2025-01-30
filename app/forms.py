from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()], id='floatingName')
    phone_number = StringField('Номер телефона', validators=[DataRequired()], id='floatingPhone')
    submit = SubmitField('Зарегистрироваться')