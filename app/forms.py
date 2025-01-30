from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()])
    phone_number = StringField('Номер телефона', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')