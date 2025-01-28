from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
app.secret_key = '923643589235892asdwsregafkjs!&'  
users = [
    {'username': 'kittygurl',
     'password': 'meow472' },
    {'username': 'gizmo',
    'password': 'theg'}
     
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('psswrd')
    error_message = "Incorrect Username Or Password!" 
    
    for user in users:
        
        if (username == user['username']) and (password == user['password']):
            session['username'] = username.title()
            
            return redirect(url_for('dashboard'))

            
         
            
    # Redirect User to the Home Page

    return render_template('index.html',error = error_message)




@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']

    return render_template('dashboard.html', username=username)  

if __name__ == '__main__':
    app.run(debug=True)
