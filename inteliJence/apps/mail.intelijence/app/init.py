#(@: Name): "intelijenceMail"

#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence ProtectiveRights please edit and use it with all the care you can give

#(@:App-Type): "Api (Restfull & RestLess)"

#(@:Language): "Python"

#(@:Language Compiler): "python 2.9"

#(@:Framework): "Flask"

#(@:Required-Modules): "Flask, Flask_restful, Flask_restless, Flask SQL Alchemy, Flask_MYSQL, Flask_Mail, Flask-WTF, Flask_Socket, Imaplib, python 2.9, email, html5lib, Jinja, Flask_Sijax, Flask_Admin, Flask_Login, **more to come**"

#wow if you are done with the above
#and
#you get it
#you are on the right track
#boom!!!!!!!! now lets start the job

#import the flask framework and all it's modules like the flask_restful and api's methods
#import all classes used in routing from the classes package/directory to access all api handlers



from flask import Flask,request,jsonify,render_template
from flask_restful import Resource, Api
from db import Connectors#import connector for database
# from classes import *
import classes


#Instantiate all classes and modules to start operation
#modules like flask and restful api
app=Flask(__name__)
dbConnector=Connectors(app)#create database connection and pass
conn=dbConnector.cursor()#cursor that db bastard
api=Api(app)#initialize the api class by passing the flask object to it
#end all instantiation and lets go to the next stage

#let the coding begin

#this variable would hold the currently logged in client application details to aid faster response
userData={}


class connect(Resource):
	"""connect class handles connection to the api.
	 as this connect class is the most important api call because without connecting the client device then
	 no request from the user of the client app can be made and all other api classes cannot be accessed 
	 because a session would be set for this particular client application"""
	

	def get(self,ijm_Name,ijm_Auth):#call the get method yo bitch

		 #import the model package to handle checking of client authentication
		from model import validateAuth

		connect=False
		aut=validateAuth(conn,ijm_Name,ijm_Auth)
		if aut==True:
			print aut
			connect=True
		userData[ijm_Name]=ijm_Auth
		return{"user":ijm_Name,"Auth":ijm_Auth,"connect":connect}#return the username and auth key, then return True if client app details is correct else False
		#add resources to the api and get routed
api.add_resource(connect,'/connect/<string:ijm_Name>/<string:ijm_Auth>')#stack up the above class with this url and get bounded





#create a main page where you'd talk about this api and then allow user's to create a client account
#thiis can be done later


# @app.route("/create")
# def helloToIntelijence():
# 	return render_template("index.html")


# @app.route("/activate",methods=['POST'])
# def activateAcct():
# 	if request.method=='POST' and request.form["Desc"] and request.form["appName"]:
# 		print request.form["Desc"]
# 		desc=request.form["Desc"]
# 		name=request.form["appName"]
# 		if name is not "" and desc is not"":
# 			return "Your Auth Password is "+request.form["appName"]
			
	#end of activate function


#end of codes
#now start the engine and let the car start moving
#run flask here

if __name__ == '__main__':
	app.run(debug=True,port=9000)#run flask engine on port 9000
		
