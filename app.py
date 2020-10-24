from flask import Flask, redirect
from flask import render_template
from flask_pymongo import PyMongo
import scraping

#Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Create route
@app.route("/")
def index():
   #Find data
   mars = mongo.db.mars.find_one()
   #Return template and data
   return render_template("index.html", mars=mars)

#Create route to scrape function
@app.route("/scrape")
def scrape():
   #Run scrapped functions 
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect("/")

if __name__ == "__main__":
   app.run()



