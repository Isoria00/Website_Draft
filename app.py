from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
app.secret_key = '923643589235892asdwsregafkjs!&'  
users = [
    {'username': 'kittygurl',
     'password': 'meow472' },
    {'username': 'gizmo',
    'password': 'theg'}
     
]

events = [
    {'title': 'Meet and Greet', 'start': '2025-02-15T10:00:00', 'end': '2025-02-15T11:00:00'},
    {'title': 'Workshop', 'start': '2025-02-16T14:00:00', 'end': '2025-02-16T16:00:00'}
]
@app.route('/')
def home():
    error_message = None
    return render_template('index.html', error = error_message)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('psswrd')
    

    # Check if user in list
    for user in users:
        
        if (username == user['username']) and (password == user['password']):
            session['username'] = username.title()
            
            return redirect(url_for('dashboard'))
       


    error_message = "Incorrect Username or Password"

    
    # Redirect User to the Home Page

    return render_template('index.html',error = error_message)
   
            
    




@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']

    return render_template('dashboard.html', username=username)  


# START OF CALENDAR FUNCTIONS

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/api/get-events')
def get_events():
    return jsonify(events)


@app.route('/api/save-event', methods=['POST'])
def save_event():
    new_event = request.get_json()
    events.append(new_event)
    return jsonify(new_event), 201

# END OF CALENDAR FUNCTIONS

@app.route('/dateideas')
def dateideas():
    return render_template('dateideas.html')

@app.route('/boredom')
def boredom():
    return render_template('boredom.html')

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

if __name__ == '__main__':
    app.run(debug=True)
