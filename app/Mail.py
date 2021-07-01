import code

from flask import *
from flask_mail import *
from random import *
from datetime import datetime

app = Flask(__name__)
mail = Mail(app)
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'username@gmail.com'
app.config['MAIL_PASSWORD'] = '*************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(000000, 999999)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    msg = Message('code', sender='username@gmail.com', recipients=[email])
    msg.body = str(code)
    mail.send(msg)
    return render_template('emailverification.html')


@app.route('/validate', methods=["POST"])
def validate():
    user_code = request.form['code']
    if code == int(user_code):
        return "<h3> Email  verification is  successful </h3>"
        user = User2(username='lucy', email='lucy@example.com', firstname='Lucy', surname='Abbott', type='student',
                     password='lucy1234', confirmed='1', timestamp=datetime.now())
        user.set_password('lucy1234')
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return "<h3>failure, verification code does not match</h3>"
    if __name__ == '__main__':
        app.run(debug=True)
