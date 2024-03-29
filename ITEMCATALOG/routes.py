from flask import flash, redirect, render_template, url_for

from ITEMCATALOG import app, db, bcrypt 
from ITEMCATALOG.forms import LoginForm, RegistrationForm
from ITEMCATALOG.models import Post, User

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

#home and default page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def aboutpage():
    return render_template("about.html")
    

@app.route("/register", methods=['GET', 'POST'])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(username=form.username.data, email=form.email.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created! You are now able to log in', 'success')
                return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                        flash('You have been logged in!', 'success')
                        return redirect(url_for('home'))
                else:
                        flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)
