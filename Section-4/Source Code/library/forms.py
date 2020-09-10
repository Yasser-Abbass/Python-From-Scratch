from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, FormField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField
from datetime import date, timedelta


class PublisherForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    founded = DateField('Founded', default=date.today, validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    save = SubmitField('Save')
    update = SubmitField('Update')
    delete = SubmitField('Delete')


class SubscriberForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    address = StringField("Address", validators=[DataRequired()])
    ssn = StringField("SSN", validators=[DataRequired()])
    save = SubmitField('Save')
    update = SubmitField('Update')
    delete = SubmitField('Delete')


class BorrowForm(FlaskForm):
    subscriber = FormField(SubscriberForm)
    start = DateField()
    end = DateField()


class BookForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    pages = IntegerField(validators=[DataRequired()])
    publish_date = DateField(validators=[DataRequired()])
    publisher = SelectField(validate_choice=False)
    borrowing_history = FieldList(FormField(BorrowForm))
    subscriber = SelectField(validate_choice=False)
    start = DateField(default=date.today)
    date_after = date.today() + timedelta(days=10)
    end = DateField(default=date_after)
    save = SubmitField('Save')
    update = SubmitField('Update')
    delete = SubmitField('Delete')
    borrow = SubmitField('Borrow')
