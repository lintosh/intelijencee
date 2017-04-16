from flask import Flask,render_template,session,url_for,redirect,request,send_from_directory
import os

#load deck and initialize all classes and plugins here
app=Flask(__name__)
app.secret_key='$_$pecctrums$_$'
#end 
@app.route("/")
def home():
	return render_template("index.html")



if __name__ == '__main__':
	app.run(port=5050,debug=True)