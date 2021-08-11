# API in Python using Flask

# Application programming interface- Client(request) (front end)-> server(response) (backend) by HTTP; 
#Json(java script object notation)/XML type is how the API is stored

# This code is to consume the API. Basically using the API and editing it to view the details.

#importing the  modules for API
import requests
import json

#using get to take the web address and use it to view the details
response = requests.get(
'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow') #requesting web page address 

#print the content from the the response variable to verify if it is working
print(response.json()['items'])

#loop the items and then get only title and link for answer count == 0, else try to skip it
for data in response.json()['items']:
	if data['answer_count'] == 0:
		print(data['title'])
		print(data['link'])
		print()

	else:
		print('Skipped')
		print() # this is to add the space 

################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@###############################

# create your own API:

# install the flask and flask-sqlalchemy
# touch command to create a new file directly from the command line

# flask is for web development 
#import the flask and request
from flask import Flask, request

# connect to the database
from flask_sqlalchemy import SQLAlchemy

# use to call the flask
app = Flask(__name__)

#configuring the uRI to database 
app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:///data.db"

# calling the sql
db = SQLAlchemy(app)

#writing a class to take the database model
class Drink(db.model):
	#building the id, name and description for  the drink table
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(80),unique= True,nullable= False)
	description = db.Column(db.String(120))

    # repr is used for returns a printable representational string of the given object.
	def __repr__(self):
		return f"{self.name} - {self.description}"

# writing a API using app.route
@app.route('/')
def index(): #checking if the api url is generated on the browser
	return 'Hello!'

# API for the drinks where get the name of drink and its description
@app.route('/drinks')
def get_drinks():
	drinks = Drink.query.all()
	output = []
    #loop the drink and save it in output 
	for drink in drinks:
		drink_data = {'name': drink.name, 'description': drink.description}

		output.append(drink_data)

	return {"drinks": output}

# here, we are using id of the drink and querying it for 404 error
@app.route('/drinks/<id>')
def get_drink(id):
	drink = drink.query.get_or_404(id)
	return jsonify({"name":drink.name, "description": drink.description})


# In this app we are using the post method to write a new addition to the given drink data
@app.route("/drinks", methods = ['POST'])
def add_drink():
	drink = Drink(name=request.json["name"],description=request.join["description"])
	db.session.add(drink)# adding the drink
	db.session.commit() # commiting the drink
	return {'id': drink.id}

#here we are deleting the drink using the id
@app.route('/drinks/<id>', methods =['DELETE'])
def delete_drink(id):
	drink = Drink.query.get(id)
	if drink is None: # if drink is not found
		return {'error':"not found"}
	db.session.delete(drink) #remove the drink 
	db.session.commit()
	return {"message": "yeet!!"}

###############################@@@@@@@@@@@@@@@@@@@@@@@##########################

# commands to use in the python terminal to run the API call

# Postman is an API platform for building and using APIs. So, could use it to write the code
# 1. Set the python environment
# 2. install - pip3 install requests
# 3. should in the api folder
# 4. python3 -m venv .venv - create new folder to make a environment
# 5. source .venv/bin/activate
# 6. pip3 install flask
# 7. pip3 install flask-sqlalchemy -> use to work with database
# 8. pip3 freeze > requirements.txt -> all dependency in one place and everyone can use it
# 9. touch application.py
# 10. export FLASK_APP = application.py
# 11. export FLASK_ENV = development   # export is done again again when you open the terminal
# 12. flask run -> shows the website -> make the app to use it
# 14. set up the database using the terminal using python3 interactive terminal
# 15. python3
# 16. from application import db
# 17. configure the database
# 18. db.create_all()
# 19. db.session.add()
# 20. db.session.query_all()
# 21. db.commit()
# 22. flask run