from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping
import os

#Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Create route
@app.route("/")
def index():
   #Find data
   mars = mongo.db.mars_app.find_one()
   #Return template and data
   return render_template("index.html", mars=mars)

#Create route to scrape function
@app.route("/scrape")
def scrape():
   #Run scrapped functions 
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   
   return "Scraping Successful!"

if __name__ == "__main__":
   app.run(debug= True)



