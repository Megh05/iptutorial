from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class User2(UserMixin,db.Model):
    __tablename__ = 'users2'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(100))
    town = db.Column(db.String(100))
    city = db.Column(db.String(100))
    postcode = db.Column(db.String(7))
    phone = db.Column(db.String(11))
    workexperience = db.Column(db.String(100))
 
    type = db.Column(db.String(20),default="student")
    confirmed = db.Column(db.Boolean(1),default = '0')
    timestamp = db.Column(db.DateTime())
    
    
   
    def __init__(self, firstname, surname, username, email, password, address=None,town=None,city=None,postcode=None,phone=None,workexperience=None,type=None,confirmed=0,timestamp=None):
        self.firstname = firstname
        self.surname = surname
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.address = address
        self.town = town
        self.city = city
        self.postcode = postcode
        self.phone = phone
        self.workexperience = workexperience
        self.type = type
        self.confirmed = confirmed
        self.timestamp = timestamp

    def __repr__(self):
        return '<User2 {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User2.query.get(int(id))

class Courses(db.Model):

    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    chapters = db.Column(db.String(200))
    status = db.Column(db.String(50),default='unconfirmed')
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, name, description, chapters,status,user_id):
        self.name = name
        self.description = description
        self.chapters = chapters
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return '<Courses {}>'.format(self.name)

class Project2(db.Model):

    __tablename__ = 'projects2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    chapters = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, name, description, chapters,user_id):
        self.name = name
        self.description = description
        self.chapters = chapters
        self.user_id = user_id

    def __repr__(self):
        return '<Project2 {}>'.format(self.name)

class Content2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    file = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, name=None, file=None, user_id=None):
        self.name = name
        self.file = file
        self.user_id = user_id

    def __repr__(self):
        return '<Content2 {}>'.format(self.name)

class Supporttickets3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticketname = db.Column(db.String(100))
    date = db.Column(db.Date())
    message = db.Column(db.String(1000))
    sendername = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(11))
    response = db.Column(db.String(1000))
    progress = db.Column(db.String(50))
    assignedto = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, ticketname=None, date=None, message=None, sendername=None, email=None, phone=None, response=None, progress=None, assignedto=None, user_id=None):
        self.ticketname = ticketname
        self.date = date
        self.message = message
        self.sendername = sendername
        self.email = email
        self.phone = phone
        self.response = response
        self.progress = progress
        self.assignedto = assignedto
        self.user_id = user_id

    def __repr__(self):
        return '<Supporttickets3 {}>'.format(self.name)

class Sessions2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionname = db.Column(db.String(100))
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    duration = db.Column(db.String(100))
    coursename = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, sessionname=None, date=None, time=None, duration=None, coursename=None, user_id=None):
        self.sessionname = sessionname
        self.date = date
        self.time = time
        self.duration = duration
        self.coursename = coursename
        self.user_id = user_id
      

    def __repr__(self):
        return '<Session2 {}>'.format(self.name)

class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    address = db.Column(db.String(100))
    town = db.Column(db.String(100))
    city = db.Column(db.String(100))
    postcode = db.Column(db.String(7))
    phone = db.Column(db.String(11))
    service = db.Column(db.String(200))
    amount = db.Column(db.Numeric(10,2))
    email = db.Column(db.String(120))
    cardno = db.Column(db.String(16))
    expirydate = db.Column(db.String(5))
    securitycode = db.Column(db.String(3))
    date = db.Column(db.Date())
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, firstname=None, surname=None, address=None, town=None, city=None,postcode=None,phone=None,service=None,amount=None,email=None,cardno=None,expirydate=None,securitycode=None,date=None, user_id=None):
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.town = town
        self.city = city
        self.postcode = postcode
        self.phone = phone
        self.service = service
        self.amount = amount
        self.email = email
        self.cardno = cardno
        self.expirydate = expirydate
        self.securitycode = securitycode
        self.date = date
        self.user_id = user_id
      

    def __repr__(self):
        return '<Payments {}>'.format(self.name)

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    studentfirstname = db.Column(db.String(50))
    studentsurname = db.Column(db.String(50))
    projectname = db.Column(db.String(100))
    date = db.Column(db.Date())
    coursename = db.Column(db.String(100))
    grade = db.Column(db.String(100))
    feedback = db.Column(db.String(1000))
    filename = db.Column(db.String(300))
    file = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('users2.id'))

    users = db.relationship(User2)

    def __init__(self, title=None,studentfirstname=None,studentsurname=None,projectname=None,date=None,coursename=None,grade=None,feedback=None,filename=None, file=None, user_id=None):
        self.title = title
        self.studentfirstname = studentfirstname
        self.studentsurname = studentsurname
        self.projectname = projectname
        self.date = date
        self.coursename = coursename
        self.grade = grade
        self.feedback = feedback
        self.filename = filename
        self.file = file
        self.user_id = user_id

    def __repr__(self):
        return '<Work {}>'.format(self.name)
