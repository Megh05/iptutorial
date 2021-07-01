import re
from flask import render_template, flash, redirect, url_for, send_file
from app import app
from app import db
from app.forms import LoginForm, studentsignup1, tutorsignup1, accountdetails1, settingsform1, deleteform, addcourse1, \
    joincourseform, addproject1, Uploadform, helpform1, helpform2, booksession1, paymentform
from app.models import User2, Courses, Project2, Content2, Supporttickets3, Sessions2, Payments, Work
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from io import BytesIO
from datetime import date
from flask_mail import Message
from flask_mail import Mail
from random import *
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/studentdashboard')
@login_required
def studentdashboard():
    course = Courses.query.filter_by(id='1')
    project = Project2.query.filter_by(id='1')
    return render_template('studentdashboard.html', course=course, project=project)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/studentsignup', methods=['GET', 'POST'])
def studentsignup():
    if current_user.is_authenticated:
        return redirect(url_for('studentdashboard'))
    form = studentsignup1()
    if form.validate_on_submit():
        user = User2(username=form.username.data, email=form.email.data, firstname=form.firstname.data,
                     surname=form.surname.data, type='student', password=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return render_template('studentsignup.html', title='Student sign up', form=form)


@app.route('/tutorsignup', methods=['GET', 'POST'])
def tutorsignup():
    if current_user.is_authenticated:
        return redirect(url_for('tutordashboard'))
    form = tutorsignup1()
    if form.validate_on_submit():
        user = User2(username=form.username.data, email=form.email.data, firstname=form.firstname.data,
                     surname=form.surname.data, type='tutor', password=form.password.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return render_template('tutorsignup.html', title='Tutor sign up', form=form)


@app.route('/courseprogress')
@login_required
def courseprogress():
    data = Courses.query.filter_by(id='1')

    return render_template('courseprogress.html', data=data)


@app.route('/projectprogress')
@login_required
def projectprogress():
    data = Project2.query.filter_by(id='1')
    work = Work.query.filter_by(id='3')

    return render_template('projectprogress.html', data=data, work=work)


@app.route('/certificates')
@login_required
def certificates():
    certificate = Content2.query.filter_by(id=2)
    return render_template('certificates.html', certificate=certificate)


@app.route('/supportpage')
@login_required
def supportpage():
    return render_template('supportpage.html')


@app.route('/messages')
@login_required
def messages():
    return render_template('messages.html')


@app.route('/studentprofile')
@login_required
def studentprofile():
    projects = Project2.query.filter_by(id='1')
    courses = Courses.query.filter_by(id='1')

    return render_template('studentprofile.html', projects=projects, courses=courses)


@app.route('/studentaccount', methods=['GET', 'POST'])
@login_required
def studentaccount():
    form = accountdetails1(request.form, obj=current_user)
    if request.method == 'POST':
        if form.validate_on_submit():
            current_user.username = form.username.data
            current_user.firstname = form.firstname.data
            current_user.surname = form.surname.data
            current_user.password = form.password.data
            current_user.email = form.email.data
            current_user.address = form.address.data
            current_user.town = form.town.data
            current_user.city = form.city.data
            current_user.postcode = form.postcode.data
            current_user.phone = form.phone.data
            current_user.workexperience = form.workexperience.data
            current_user.set_password(form.password.data)
            # #Ignore form fields not in data model
            # form_data = {i: form.data[i] for i in form.data if i not in ["csrf_token", "submit"]}
            # #Remove empty fields
            # new_data = {k: v for k, v in form_data.items() if v is not None}
            # #Unpack into Company model
            # current_user.update(**new_data)
            db.session.commit()
            flash('Your details have been changed.')
            return redirect(url_for('studentaccount'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.firstname.data = current_user.firstname
        form.surname.data = current_user.surname
        form.password.data = current_user.password_hash
        form.email.data = current_user.email
        form.address.data = current_user.address
        form.town.data = current_user.town
        form.city.data = current_user.city
        form.postcode.data = current_user.postcode
        form.phone.data = current_user.phone
        form.workexperience.data = current_user.workexperience
    return render_template('studentaccount.html', title='Student account',
                           form=form)


@app.route('/studentsettings', methods=['GET', 'POST'])
@login_required
def studentsettings():
    form = settingsform1(request.form, obj=current_user)
    if request.method == 'POST':
        if "savedetails" in request.form and form.validate_on_submit():
            current_user.password = form.password.data
            current_user.email = form.email.data

            current_user.set_password(form.password.data)

            db.session.commit()
            flash('Your details have been changed.')
            return redirect(url_for('studentsettings'))
    elif request.method == 'GET':

        form.password.data = current_user.password_hash
        form.email.data = current_user.email

    return render_template('studentsettings.html', title='Student settings',
                           form=form, obj=current_user)


@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    id = 1
    user = User2.query.filter(id == id).first()

    db.session.delete(user)
    db.session.commit()

    flash('Your account has been successfully deleted. ', 'success')
    return redirect(url_for('login'))
    return render_template('login.html', form=form, id=id, user=user)


@app.route('/coursedetails', methods=['GET', 'POST'])
def coursedetails():
    course = Courses.query.filter_by(id='1')
    return render_template('coursedetails.html', course=course)


@app.route('/projectdetails2', methods=['GET', 'POST'])
def projectdetails2():
    project = Project2.query.filter_by(id='1')
    return render_template('projectdetails2.html', project=project)


@app.route('/joincourse', methods=['GET', 'POST'])
@login_required
def joincourse():
    course = Courses(name='Intellectual property', description='copyright laws', chapters='20', status='confirmed',
                     user_id=current_user.id)

    db.session.add(course)
    db.session.commit()
    flash('Joined course')
    return redirect(url_for('coursedetails'))

    return render_template('coursedetails.html', title='Course details', form=form)


@app.route('/confirmcourse', methods=['GET', 'POST'])
def confirmcourse():
    course = Courses(name='Intellectual property', description='copyright laws', chapters='20', status='confirmed',
                     user_id=current_user.id)

    db.session.add(course)
    db.session.commit()
    flash('Confirmed course')
    return redirect(url_for('courserequests'))

    return render_template('courserequests.html', title='Course requests', form=form)


@app.route('/joinproject', methods=['GET', 'POST'])
@login_required
def joinproject():
    project = Project2(name='Trademarks', description='trademark laws', chapters='22', user_id=current_user.id)

    db.session.add(project)
    db.session.commit()
    flash('Joined project')
    return redirect(url_for('projectdetails2'))

    return render_template('projectdetails2.html', title='Project details', form=form)


@app.route('/helpform', methods=['GET', 'POST'])
def helpform():
    form = helpform1()
    if form.validate_on_submit():
        ticket = Supporttickets3(sendername=form.sendername.data, email=form.email.data, phone=form.phone.data,
                                 ticketname=form.ticketname.data, message=form.message.data, user_id=current_user.id,
                                 date=date.today(), assignedto='Tom', progress='sent')

        db.session.add(ticket)
        db.session.commit()
        flash('Help form submitted')
        return redirect(url_for('helpform'))
    return render_template('helpform.html', title='Help form', form=form)


@app.route('/supporttickets')
@login_required
def supporttickets():
    supportticket = Supporttickets3.query.filter_by(id='2')

    return render_template('supporttickets.html', supportticket=supportticket)
    return render_template('supporttickets.html')


@app.route('/submitwork', methods=["GET", "POST"])
@login_required
def submitwork():
    if request.method == 'POST':
        file = request.files['inputFile']
        firstname = request.form['firstname']
        surname = request.form['surname']
        projectname = request.form['projectname']
        coursename = request.form['coursename']
        titleofwork = request.form['titleofwork']

        newFile = Work(filename=file.filename, file=file.read(), title=titleofwork, studentfirstname=firstname,
                       studentsurname=surname, projectname=projectname, coursename=coursename, date=date.today(),
                       user_id=current_user.id)
        db.session.add(newFile)
        db.session.commit()
        flash('Work submitted')
        return redirect(url_for('submitwork'))

    return render_template('submitwork.html')


@app.route('/tutordashboard')
@login_required
def tutordashboard():
    work = Work.query.filter_by(id='5')
    return render_template('tutordashboard.html', work=work)


@app.route('/markwork', methods=["GET", "POST"])
@login_required
def markwork():
    work = Work.query.filter_by(id='5')

    if request.method == 'POST':
        grade = request.form['grade']
        feedback = request.form['feedback']

        newFile = Work(filename='Report (1).docx', title='Assignment 1', studentfirstname='Lucy',
                       studentsurname='Abbott', projectname='Trade secrets', coursename='Intellectual property',
                       date=date.today(), user_id=current_user.id, grade=grade, feedback=feedback)
        db.session.add(newFile)
        db.session.commit()
        flash('The work has been marked')
        return redirect(url_for('markwork'))

    return render_template('markwork.html', work=work)


@app.route('/content')
@login_required
def content():
    content = Content2.query.filter_by(id='1')
    return render_template('content.html', content=content)


@app.route('/meeting')
@login_required
def meeting():
    return render_template('meeting.html')


@app.route('/payment')
@login_required
def payment():
    payment = Payments.query.filter_by(id='1')
    return render_template('payment.html', payment=payment)


@app.route('/sessions')
@login_required
def sessions():
    session = Sessions2.query.filter_by(id='1')

    return render_template('sessions.html', session=session)


@app.route('/tutorcourses')
@login_required
def tutorcourses():
    course = Courses.query.filter_by(id='1')
    user = User2.query.filter_by(id='3')
    return render_template('tutorcourses.html', course=course, user=user)


@app.route('/booksession', methods=['GET', 'POST'])
@login_required
def booksession():
    form = booksession1()
    if form.validate_on_submit():
        session = Sessions2(sessionname=form.sessionname.data, date=form.date.data, time=form.time.data,
                            duration=form.duration.data, coursename=form.coursename.data, user_id=current_user.id)

        db.session.add(session)
        db.session.commit()
        flash('Session booked')
        return redirect(url_for('sessions'))
    return render_template('booksession.html', title='Book session', form=form)


@app.route('/newmeeting')
@login_required
def newmeeting():
    return render_template('newmeeting.html')


@app.route('/meetingcode')
@login_required
def meetingcode():
    return render_template('meetingcode.html')


@app.route('/invoice')
@login_required
def invoice():
    return render_template('invoice.html')


@app.route('/admindashboard')
@login_required
def admindashboard():
    course = Courses.query.filter_by(id='1')
    ticket = Supporttickets3.query.filter_by(id='2')
    return render_template('admindashboard.html', course=course, ticket=ticket)


@app.route('/adminsupportpage', methods=['GET', 'POST'])
@login_required
def adminsupportpage():
    form = helpform2(request.form, obj=current_user)
    supportticket = Supporttickets3.query.filter_by(id='2')
    if request.method == 'POST':

        if form.validate_on_submit():
            ticket = Supporttickets3(sendername='Cher Lloyd', email='cher@example.com', phone='07656787678',
                                     ticketname='Cancel membership', message='How do I cancel my membership?',
                                     user_id='5', date=date.today(), assignedto='Tom', progress='recieved',
                                     response=form.response.data)

            db.session.add(ticket)
            db.session.commit()
            flash('Response submitted')
    return render_template('adminsupportpage.html', supportticket=supportticket, form=form)

    return render_template('adminsupportpage.html')


@app.route('/courserequests')
@login_required
def courserequests():
    course = Courses.query.filter_by(id='1')
    return render_template('courserequests.html', course=course)


@app.route('/projectdetails')
@login_required
def projectdetails():
    project = Project2.query.filter_by(id='1')

    work = Work.query.filter_by(id='3')
    user = User2.query.filter_by(id='2')

    return render_template('projectdetails.html', project=project, work=work, user=user)


@app.route('/studentdetails')
@login_required
def studentdetails():
    user = User2.query.filter_by(id='2')
    course = Courses.query.filter_by(id='1')
    work = Work.query.filter_by(id='3')
    project = Project2.query.filter_by(id='1')
    return render_template('studentdetails.html', user=user, course=course, project=project, work=work)


@app.route('/tutordetails')
@login_required
def tutordetails():
    tutor = User2.query.filter_by(id='2')
    student = User2.query.filter_by(id='3')
    course = Courses.query.filter_by(id='1')
    project = Project2.query.filter_by(id='1')
    return render_template('tutordetails.html', tutor=tutor, student=student, course=course, project=project)


@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.type == 'student':

            return redirect(url_for('studentdashboard'))
        elif current_user.type == 'tutor':
            return redirect(url_for('tutordashboard'))
        elif current_user.type == 'admin':
            return redirect(url_for('admindashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User2.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            if user.type == 'student': next_page = url_for('studentdashboard')
            if user.type == 'tutor': next_page = url_for('tutordashboard')
            if user.type == 'admin': next_page = url_for('admindashboard')
        return redirect(next_page)
        return redirect(url_for('studentdashboard'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/addcourse', methods=['GET', 'POST'])
def addcourse():
    form = addcourse1()
    if form.validate_on_submit():
        course = Courses(name=form.name.data, description=form.description.data, chapters=form.chapters.data,
                         status='unconfirmed', user_id=current_user.id)

        db.session.add(course)
        db.session.commit()
        flash('Course added')
        return redirect(url_for('addcourse'))
    return render_template('addcourse.html', title='Add course', form=form)


@app.route('/tutorprojects')
@login_required
def tutorprojects():
    project = Project2.query.filter_by(id='1')
    student = User2.query.filter_by(id='3')

    return render_template('tutorprojects.html', project=project, student=student)


@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
    form = addproject1()
    if form.validate_on_submit():
        project = Project2(name=form.name.data, description=form.description.data, chapters=form.chapters.data,
                           user_id=current_user.id)

        db.session.add(project)
        db.session.commit()
        flash('Project added')
        return redirect(url_for('addproject'))
    return render_template('addproject.html', title='Add project', form=form)


@app.route('/upload', methods=["GET", "POST"])
def upload():
    file = request.files['inputFile']
    newFile = Content2(name=file.filename, file=file.read())
    db.session.add(newFile)
    db.session.commit()
    flash('File added')
    return redirect(url_for('content'))
    return render_template('content.html')


@app.route('/download', methods=["POST"])
def download():
    file_data = Content2.query.filter_by(id=1).first()
    return send_file(BytesIO(file_data.file), attachment_filename='flask.pdf', as_attachment='True')


@app.route('/download2', methods=["POST"])
def download2():
    file_data = Content2.query.filter_by(id=2).first()
    return send_file(BytesIO(file_data.file), attachment_filename='degree certificate.pdf', as_attachment='True')


@app.route('/download3', methods=["POST"])
def download3():
    file_data = Work.query.filter_by(id=2).first()
    return send_file(BytesIO(file_data.file), attachment_filename='lastReport.docx', as_attachment='True')


@app.route('/verify', methods=["POST"])
def verify():
    code = randint(000000, 999999)
    mail = Mail(app)
    email = request.form["email"]
    msg = Message('code', sender='username@gmail.com', recipients=[email])
    msg.body = str(code)
    mail.send(msg)
    return render_template('emailverification.html')


@app.route('/validate', methods=["POST"])
def validate():
    user_code = request.form['code']
    if code == int(user_code):
        user = User2(username='lucy', email='lucy@example.com', firstname='Lucy', surname='Abbott', type='student',
                     password='lucy1234', confirmed='1', timestamp=datetime.now())
        user.set_password('lucy1234')
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/makepayment', methods=['GET', 'POST'])
def makepayment():
    form = paymentform()
    if form.validate_on_submit():
        payment = Payments(firstname=form.firstname.data, surname=form.surname.data, address=form.address.data,
                           town=form.town.data, city=form.city.data, postcode=form.postcode.data, phone=form.phone.data,
                           service=form.service.data, amount=form.amount.data, email=form.email.data,
                           cardno=form.cardno.data, expirydate=form.expirydate.data,
                           securitycode=form.securitycode.data, date=form.date.data, user_id=current_user.id)

        db.session.add(payment)
        db.session.commit()
        flash('Payment made')
        return redirect(url_for('payment'))
    return render_template('makepayment.html', title='Make payment', form=form)
