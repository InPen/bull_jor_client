from flask import Flask, render_template
# web server
app = Flask(__name__)
# first route
@app.route('/')

def index():
    return render_template('index.html')
# second route
@app.route('/home')
def home():
    return render_template('home.html')
# take app variable and call method run
if __name__=='__main__':
    app.run(debug=True)
# to run server run `python <path of file>`
