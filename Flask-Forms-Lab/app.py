from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


usernametrue = "llo2ay"
passwordtrue = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

isFriend= False

@app.route('/', methods= ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		useruser = request.form['username']
		passuser = request.form['password']
		if useruser == usernametrue and passuser == passwordtrue:
			redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home', methods= ['GET','POST'])
def home():
	return render_template('home.html', facebook_friends= facebook_friends)

@app.route('/friend_exists/<string:name>',methods= ['GET','POST'])
def exist(name):
	for x in facebook_friends:
		if name == x:
			isFriend= True
			break
		else:
			isFriend=False


	return render_template('friend_exists.html',isFriend=isFriend,name= name)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)