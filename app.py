from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import json
import os
import random
from dateideas import *

app = Flask(__name__)

app.secret_key = '923643589235892asdwsregafkjs!&'  
users = [
    {'username': 'kittygurl',
     'password': 'meow472' },
    {'username': 'gizmo',
    'password': 'theg'}
     
]

wishlist = [
    
]

images_folder = os.path.join(app.static_folder, 'images', 'CatPhotos')

images = [f'images/CatPhotos/{filename}' for filename in os.listdir(images_folder) if filename.endswith(('jpg'))]


@app.route('/')
def home():
    error_message = None
    return render_template('index.html', error = error_message)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('psswrd')
    

   
    for user in users:
        
        if (username == user['username']) and (password == user['password']):
            session['username'] = username.title()
            
            return redirect(url_for('dashboard'))
       


    error_message = "Incorrect Username or Password"

    
    

    return render_template('index.html',error = error_message)
   


@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']

    return render_template('dashboard.html', username=username)  




@app.route('/dateideas', methods=['GET', 'POST'])
def dateideas():
    return render_template('dateideas.html', idea=None)


@app.route('/generate-date-idea', methods=['POST'])
def generate_date_idea():
    selected_index = int(request.form["options"]) # Get index from dropdown
    idea = get_random_idea(selected_index) # Generate random idea
    return render_template('dateideas.html', idea=idea)

def get_random_idea(index):
    return random.choice(list_of_categories[index])


@app.route('/boredom')
def boredom():

    images_folder = os.path.join(app.static_folder, 'images', 'CatPhotos')

    images = [f'images/CatPhotos/{filename}' for filename in os.listdir(images_folder) if filename.endswith(('jpg', 'png', 'jpeg'))]

    return render_template('boredom.html', images=images)



@app.route('/get_image', methods=['GET'])
def get_image():
  
  
    images_folder = os.path.join(app.static_folder, 'images', 'CatPhotos')

    
    images = [f'images/CatPhotos/{filename}' for filename in os.listdir(images_folder) if filename.endswith(('jpg', 'png', 'jpeg'))]

    
    selected_image = random.choice(images)

   
    return jsonify({'image_url': selected_image})






@app.route('/wishlist', methods = ['GET'])
def wishlist_page():
    global wishlist

    try:
        with open('wishlist.json', 'r') as file:
            wishlist = json.load(file)
    except FileNotFoundError:
        wishlist = []


    return render_template('wishlist.html', wishlist = wishlist)

@app.route('/wishlist/add', methods=["POST"])
def add_wishlist_item():
    item = request.form.get('item')
    link = request.form.get('link')

    if item and link:
        new_item = {'item': item, 'link': link}
        wishlist.append(new_item)
    
        with open('wishlist.json', 'w') as file:
            json.dump(wishlist,file)
    
    return redirect(url_for('wishlist_page'))

def load_wishlist():
    global wishlist
    try:
        with open('wishlist.json', 'r') as file:
            wishlist = json.load(file)
    except FileNotFoundError:
        wishlist = []

def save_wishlist():
    with open('wishlist.json', 'w') as file:
        json.dump(wishlist, file)

@app.route('/wishlist/remove/<int:item_index>', methods=["POST"])
def remove_wishlist_item(item_index):
    global wishlist

    
    if 0 <= item_index < len(wishlist):
        del wishlist[item_index]

    
    save_wishlist()

   
    return redirect(url_for('wishlist_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

