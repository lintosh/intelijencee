#(@:Description): "Client testing for email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence ProtectiveRights please edit and use it with all the care you can give

#(@:App-Type): "Dynamic"

#(@:Language): "Python"

#(@:Language Compiler): "python 2.9"

#(@:Framework): "Flask"

#(@:Required-Modules): "Flask,  Flask SQL Alchemy, Flask_MYSQL, Flask-WTF, Flask_Socket, html5lib, Jinja, Flask_Sijax, Flask_Admin, Flask_Login, Request **more to come**"

#wow if you are done with the above
#and
#you get it
#you are on the right track
#boom!!!!!!!! now lets start the job

#import the flask framework and all it's modules and start testing
#import all classes used in routing from the classes package/directory to access all api handlers



from flask import Flask,request,jsonify
from requests import put,get
import json
# from classes import *



#Instantiate all classes and modules to start operation
#modules like flask and restful api
app=Flask(__name__)


#let the coding begin
@app.route("/")
def loadMain():##connect client with mail.intelijence api so as to access all other api calls
	returnedVal=json.loads(get('http://localhost:9000/connect/pichaBot/hf234we6f984ewsd32j89yds').text)#decode response from json format to type 'dict'
	# return returnedVal["Auth"]
	if(returnedVal["connect"]==True):
		return ("AuthKey: {} <br/>User: {} <br/>connect: {}".format(returnedVal["Auth"],returnedVal["user"],returnedVal["connect"]))#end format and return block
	else:
		return "Sorry An Error Occured, relaunch this app please"



#end of codes
#now start the engine and let the car start moving
#run flask here

if __name__ == '__main__':
	app.run(debug=True,port=8000)
		
