from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)

app.secret_key = '923643589235892asdwsregafkjs!&'  
users = [
    {'username': 'kittygurl',
     'password': 'meow472' },
    {'username': 'gizmo',
    'password': 'theg'}
     
]

dates = {
        "2/7/2025": "Golfing",
        "2/5/2025": "Soccer",
        "2/3/2025": "Skiing",
        "2/27/2025": "Fishing",
    }


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
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    return render_template('index.html',error = error_message)
   
            
    
=======
    return render_template('index.html')
>>>>>>> Stashed changes
=======
    return render_template('index.html')
>>>>>>> Stashed changes




@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']

    return render_template('dashboard.html', username=username)  



# Schedule Functions
@app.route('/schedule')
def schedule():
    if request.method == "POST":
        date = request.form.get("date")
        task = request.form.get("task")
    
        if date and task:
            if date not in dates:
                dates[date] = []
            
            dates[date].append(task)

    
    
    return render_template('schedule.html', dates = dates)


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
