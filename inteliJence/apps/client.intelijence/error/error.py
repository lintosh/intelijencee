


#email Management, and automation

# @(Author): "inteliJence development team"

#under the lincense of Apache 2.0
#import the flask framework and all it's modules like the flask_restful and api's methods
#import all classes used in routing from the classes package/directory to access all api handlers

#wow if you are done with the above
#then
#and you get it
#you are on the right track
#boom!!!!!!!! now lets start the job

from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from classes import *
# io.set('polling duration', 5);


#Instantiate all classes and modules to start operation
#modules like flask and restful api
app=Flask(__name__)
# api=Api(app)


#let the coding begin



"""main router handles redirecting and all for main"""

#add resources to the api and get routed
@app.route("/<name>")
def home(name):
	return jsonify({"response":name})


#end of codes
#now start the engine and let the car start moving
#run flask here

if __name__ == '__main__':
	app.run(debug=True,port=9000)
		

