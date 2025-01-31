from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()], id='floatingName')
    phone_number = StringField('Номер телефона', validators=[DataRequired()], id='floatingPhone')
    submit = SubmitField('Зарегистрироваться')

    def validate_phone_number(self, phone_number):
        user = db.session.scalar(sa.select(User).where(User.phone_number == phone_number.data))
        if user:
            flash("Номер уже использован")
            raise ValidationError('Номер уже использован')