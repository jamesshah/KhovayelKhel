from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, Length
from kk.models import User
from flask import request


class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Id', validators=[Email(), DataRequired()])
    mobile = StringField('Mobile Number', validators=[
                         DataRequired(), Length(min=10, max=13)])
    en_num = StringField("Enrollment Number", validators=[
                         DataRequired(), Length(min=12, max=12)], id="s_enroll")
    submit = SubmitField('Submit')

    def validate_email(self, email):
        existing_user = User.query.filter_by(email=email.data).first()

        if existing_user:
            raise ValidationError('Email Address Already Used.')

    def validate_mobile(self, mobile):
        existing_user = User.query.filter_by(mobile=mobile.data).first()

        if existing_user:
            raise ValidationError('Mobile Number Already Used.')

    def validate_en_num(self, en_num):

        existing_user = User.query.filter_by(en_num=en_num.data).first()

        if existing_user:
            raise ValidationError('Enrollment Number Already Registered.')
