# ma dependencies
from flask import Flask, render_template, redirect, url_for, request, jsonify
# ma dummy Heroku cousin
from pusher import Pusher
# ma data
import json
# web server
app = Flask(__name__)

# object that interacts with pusher
pusher = Pusher(
    app_id= '662823',
    key = '52066437e2e5cc33416d',
    secret = '2ccab47907310ec26d73',
    cluster = 'us2',
    ssl=True
)

# first route. login
@app.route('/', methods=['GET', 'POST'])
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
#
# third route
# index route, shows index.html view
@app.route('/todo')
def index():
  return render_template('index.html')

# endpoint for storing todo item
@app.route('/add-todo', methods = ['POST'])
def addTodo():
  data = json.loads(request.data) # load JSON data from request
  pusher.trigger('todo', 'item-added', data) # trigger `item-added` event on `todo` channel
  return jsonify(data)

# endpoint for deleting todo item
@app.route('/remove-todo/<item_id>')
# target item by id
def removeTodo(item_id):
  data = {'id': item_id }
  pusher.trigger('todo', 'item-removed', data)
  return jsonify(data)

# endpoint for updating todo item
@app.route('/update-todo/<item_id>', methods = ['POST'])
def updateTodo(item_id):
  data = {
    'id': item_id,
    'completed': json.loads(request.data).get('completed', 0)
  }
  pusher.trigger('todo', 'item-updated', data)
  return jsonify(data)

# take app variable and call method run
if __name__=='__main__':
    app.run(debug=True)
# to run server run `python <path of file>`
