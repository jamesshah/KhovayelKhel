from flask import render_template, url_for, flash, redirect, request
from kk import app, db, mail
from kk.registration import RegistrationForm
from kk.models import participants
from flask_mail import Message

mail_id = ""
st_name = ""


@app.route('/', methods=['GET', 'POST'])
def home():
    global st_name, mail_id
    form = RegistrationForm()
    if form.validate_on_submit():
        st_name = form.name.data
        mail_id = form.email.data
        enroll = request.form['en_num']
        year = int(enroll[0:2])
        d2d_or_reg = enroll[5]
        dept = int(enroll[6:9])

        if dept is 116:
            s_dept = "IT"
        elif dept is 107:
            s_dept = "CE"
        elif dept is 111:
            s_dept = "EC"
        elif dept is 103:
            s_dept = "BM"
        elif dept is 117:
            s_dept = "IC"
        elif dept is 121:
            s_dept = "MET"

        if d2d_or_reg is "0":
            s_sem = (20 - year) * 2
        else:
            s_sem = (20 - year + 1) * 2

        newuser = participants(name=form.name.data, email=form.email.data,
                               mobile=form.mobile.data, en_num=form.en_num.data, sem=s_sem, branch=s_dept)

        db.session.add(newuser)
        db.session.commit()
        msg = Message(subject="Confirmation Mail",
                      sender="khovayelkhel@gmail.com",
                      recipients=[mail_id])
        msg.html = render_template('email.html', name=form.name.data)
        mail.send(msg)
        flash("Registered Succefully!!Check your email for confirmation", 'success')
        return redirect(url_for('home'))

    return render_template('home.html', title="Home", form=form)


@app.route('/send_mail')
def send_mail():
    global st_name, mail_id


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/games')
def games():
    return render_template('games.html', title="Games")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


'''@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        enroll = request.form['en_num']
        year = int(enroll[0:2])
        d2d_or_reg = enroll[5]
        dept = int(enroll[6:9])

        if dept is 116:
            s_dept = "IT"
        elif dept is 107:
            s_dept = "CE"
        elif dept is 111:
            s_dept = "EC"
        elif dept is 103:
            s_dept = "BM"
        elif dept is 117:
            s_dept = "IC"
        elif dept is 121:
            s_dept = "MET"

        if d2d_or_reg is "0":
            s_sem = (20 - year) * 2
        else:
            s_sem = (20 - year + 1) * 2

        newuser = User(name=form.name.data, email=form.email.data,
                       mobile=form.mobile.data, en_num=form.en_num.data, sem=s_sem, branch=s_dept)

        db.session.add(newuser)
        db.session.commit()
        flash("Registered Succefully!!", 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title="Registration", form=form)
'''
