from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField,TextField,FileField,DateField,TimeField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from wtforms import HiddenField
from app.models import User2
from flask_login import current_user
from flask_wtf import Form
from datetime import date
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Enter your username'),Length(min=2,max=20,message='Username must be between 2 and 20 characters.')])
    password = PasswordField('Password', validators=[DataRequired(message='Enter your password'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class studentsignup1(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired(message='Enter your first name'),Length(min=2,max=20,message='First name must be between 2 and 20 characters.')])
    surname = StringField('Surname', validators=[DataRequired(message='Enter your surname'),Length(min=2,max=20,message='Surname must be between 2 and 20 characters.')])
    email = StringField('Email address', validators=[DataRequired(message='Enter your email address'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
    username = StringField('Username', validators=[DataRequired(message='Enter your username'),Length(min=2,max=20,message='Username must be between 2 and 20 characters.')])
    password = PasswordField('Password', validators=[DataRequired(message='Enter your password'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(message='Enter your password again'), EqualTo('password',message='Password\'s aren\'t the same'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
   
    type = HiddenField('type')
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User2.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User2.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class tutorsignup1(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired(message='Enter your first name'),Length(min=2,max=20,message='First name must be between 2 and 20 characters.')])
    surname = StringField('Surname', validators=[DataRequired(message='Enter your surname'),Length(min=2,max=20,message='Surname must be between 2 and 20 characters.')])
    email = StringField('Email address', validators=[DataRequired(message='Enter your email address'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
    username = StringField('Username', validators=[DataRequired(message='Enter your username'),Length(min=2,max=20,message='Username must be between 2 and 20 characters.')])
    password = PasswordField('Password', validators=[DataRequired(message='Enter your password'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(message='Enter your password again'), EqualTo('password',message='Password\'s aren\'t the same'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    type =  'tutor'
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User2.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User2.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class accountdetails1(FlaskForm):

    firstname = StringField('First name', validators=[DataRequired(message='Enter your first name'),Length(min=2,max=20,message='First name must be between 2 and 20 characters.' )])
    surname = StringField('Surname', validators=[DataRequired(message='Enter your surname'),Length(min=2,max=20,message='Surname must be between 2 and 20 characters.')])
    email = StringField('Email address', validators=[DataRequired(message='Enter your email address'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
    username = StringField('Username', validators=[DataRequired(message='Enter your username'),Length(min=2,max=20,message='Username must be between 2 and 20 characters.')])
    password = PasswordField('Password', validators=[DataRequired(message='Enter your password'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    address = StringField('Address',  validators=[Length(min=2,max=50,message='Address must be between 2 and 50 characters.')])
    town = StringField('Town', validators=[Length(min=2,max=20,message='Town must be between 2 and 20 characters.')])
    city = StringField('City', validators=[Length(min=2,max=20,message='City must be between 2 and 20 characters.')])
    postcode = StringField('Postcode',  validators=[Length(min=6,max=20,message='Postcode must be between 6 and 20 characters.')])
    phone = StringField('Phone number',  validators=[Length(min=11,max=11,message='Phone number must be 11 digits.')])
    workexperience = TextAreaField('Work experience', validators=[Length(min=2,max=50,message='Work experience must be between 2 and 50 characters.')])

    submit = SubmitField('Save details')

    def validate_username(self, username):
       if User2.query.filter_by(username=username.data).first() and username.data != current_user.username:
        
         raise ValidationError('Please use a different username.')

    def validate_email(self, email):
       if User2.query.filter_by(email=email.data).first() and email.data != current_user.email:
        
         raise ValidationError('Please use a different email address.')

class settingsform1(FlaskForm):
 
    password = PasswordField('New password', validators=[DataRequired(message='Enter your password'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    password2 = PasswordField(
        'Confirm password', validators=[DataRequired(message='Confirm your password '), EqualTo('password',message='Password\'s aren\'t the same'),Length(min=8,max=20,message='Password must be between 8 and 20 characters.')])
    email = StringField('New email address', validators=[DataRequired(message='Enter your email address'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
    email2 = StringField('Confirm email address', validators=[DataRequired(message='Confirm your email address '), EqualTo('email',message='Email addresses aren\'t the same'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
    
    submit = SubmitField('Save details')

    def validate_email(self, email):
       if User2.query.filter_by(email=email.data).first() and email.data != current_user.email:
        
         raise ValidationError('Please use a different email address.')

class deleteform(Form):
    delete = SubmitField('Delete account')

class addcourse1(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Enter the course name'),Length(min=2,max=50,message='Course name must be between 2 and 50 characters.' )])
    description = TextAreaField('Description', validators=[DataRequired(message='Enter the course description'),Length(min=2,max=200,message='Course description must be between 2 and 200 characters.' )])
    chapters = StringField('Chapters', validators=[DataRequired(message='Enter the course chapters'),Length(min=1,max=200,message='Course chapters must be between 1 and 200 characters.' )])
    user_id = current_user
    submit = SubmitField('Add course')

class addproject1(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Enter the project name'),Length(min=2,max=50,message='Course name must be between 2 and 50 characters.' )])
    description = TextAreaField('Description', validators=[DataRequired(message='Enter the project description'),Length(min=2,max=200,message='Course description must be between 2 and 200 characters.' )])
    chapters = StringField('Chapters', validators=[DataRequired(message='Enter the project chapters'),Length(min=1,max=200,message='Course chapters must be between 1 and 200 characters.' )])
    user_id = current_user
    submit = SubmitField('Add project')

class joincourseform(Form):
    joincourse = SubmitField('Join course')

class Uploadform(Form):
    file = FileField()
    submit = SubmitField('Upload files')

class helpform1(FlaskForm):
    sendername = StringField('Name', validators=[DataRequired(message='Enter your name'),Length(min=1,max=200,message='Your name must be between 1 and 100 characters.' )])
    email = StringField('Email address', validators=[DataRequired(message='Enter your email address'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
    phone = StringField('Phone number',  validators=[Length(min=11,max=11,message='Phone number must be 11 digits.')])
    ticketname = StringField('Ticket name', validators=[DataRequired(message='Enter the subject'),Length(min=2,max=50,message='Subject must be between 2 and 50 characters.' )])
    message = TextAreaField('Message', validators=[DataRequired(message='Enter your message'),Length(min=2,max=1000,message='Message must be between 2 and 1000 characters.' )])
    response = ''
    progress = 'Sent'
    assignedto = 'Tom'
    user_id = current_user
    date = date.today
    submit = SubmitField('Send message')

class helpform2(FlaskForm):
    response = TextAreaField('Response:', validators=[DataRequired(message='Enter your response'),Length(min=2,max=1000,message='Response must be between 2 and 1000 characters.')])
    submit = SubmitField('Send')

class booksession1(FlaskForm):
    sessionname = StringField('Session name', validators=[DataRequired(message='Enter the session name'),Length(min=2,max=200,message='The session name must be between 2 and 200 characters.')])
    date = DateField('Date', validators=[DataRequired(message='Enter the date of the session')])
    time = TimeField('Time', validators=[DataRequired(message='Enter the time of the session')])
    duration = StringField('Duration', validators=[DataRequired(message='Enter the duration of the session'),Length(min=2, max=100,message='Duration must be between 2 and 100 characters')])
    coursename = StringField('Course name', validators=[DataRequired(message='Enter the course name'),Length(min=2,max=200,message='Course name must be between 2 and 200 characters')])
    submit = SubmitField('Book session')

class paymentform(FlaskForm):
 firstname = StringField('First name', validators=[DataRequired(message='Enter your first name'),Length(min=2,max=50,message='Your first name should be between 2 and 50 characters')])
 surname = StringField('Surname', validators=[DataRequired(message='Enter your surname'),Length(min=2,max=50,message='Your surname should be between 2 and 50 characters')])
 address = StringField('Address',  validators=[DataRequired(message='Enter your address'),Length(min=2,max=50,message='Address must be between 2 and 50 characters.')])
 town = StringField('Town', validators=[DataRequired(message='Enter your town'),Length(min=2,max=20,message='Town must be between 2 and 20 characters.')])
 city = StringField('City', validators=[DataRequired(message='Enter your city'),Length(min=2,max=20,message='City must be between 2 and 20 characters.')])
 postcode = StringField('Postcode',  validators=[DataRequired(message='Enter your postcode'),Length(min=6,max=20,message='Postcode must be between 6 and 20 characters.')])
 phone = StringField('Phone number',  validators=[DataRequired(message='Enter your phone'),Length(min=11,max=11,message='Phone number must be 11 digits.')])
 email = StringField('Email address', validators=[DataRequired(message='Enter your email address'), Email(),Length(min=2,max=50,message='Email address must be between 2 and 50 characters.')])
 service = StringField('Service', validators=[DataRequired(message='Enter the service you are paying for'), Length(min=2,max=200,message='Service must be between 2 and 200 characters.')])
 amount = StringField('Amount',validators=[DataRequired(message='Enter the amount you are paying'), Length(min=1,max=200,message='Amount must be between 1 and 200 characters.')])
 cardno = StringField('Card number',validators=[DataRequired(message='Enter your card number'), Length(min=1,max=16,message='Card number must be between 1 and 16 characters.')])
 expirydate = StringField('Expiry date',validators=[DataRequired(message='Enter the expiry date on your card'), Length(min=1,max=5,message='Amount must be between 1 and 5 characters.')])
 securitycode = StringField('Security code',validators=[DataRequired(message='Enter the security code on your card'), Length(min=1,max=3,message='Amount must be between 1 and 3 characters.')])
 date = DateField('Date', validators=[DataRequired(message='Enter the date of the payment')])
 submit = SubmitField('Make payment')