# ma dependencies
from flask import Flask, render_template, redirect, url_for, request

# web server
app = Flask(__name__)

# first route. login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # logic to handle POST request
    if request.method == 'POST':
        # if the method is post, check user input
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password, please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# second route
@app.route('/home')
def home():
    return render_template('home.html')

# third route
@app.route('/to_do')
def to_do():
    return render_template('to_do.html')

# take app variable and call method run
if __name__=='__main__':
    app.run(debug=True)
# to run server run `python <path of file>`
