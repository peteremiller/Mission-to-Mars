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



#NEW CODE

# Import Dependencies 
#from flask import Flask, render_template, redirect 
#from flask_pymongo import PyMongo
#import scrape_mars
#import os


# Hidden authetication file
#import config 

# Create an instance of Flask app
#app = Flask(__name__)


# Use flask_pymongo to set up mongo connection locally 
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Create route that renders index.html template and finds documents from mongo
#@app.route("/")
#def home(): 

    # Find data
    #mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    #return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
#@app.route("/scrape")
#def scrape(): 

    # Run scrapped functions
#    mars_info = mongo.db.mars_info
#    mars_data = scrape_mars.scrape_mars_news()
#    mars_data = scrape_mars.scrape_mars_image()
#    mars_f = scrape_mars.scrape_mars_facts()
#    mars_w = scrape_mars.scrape_mars_weather()
#    mars_data = scrape_mars.scrape_mars_hemispheres()
#    mars_info.update({}, mars_data, upsert=True)

#    return redirect("/", code=302)

#if __name__ == "__main__": 
#    app.run(debug= True)
    
    
    
#NEW CODE
#from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
#import scrape_mars

# Create an instance of Flask
#app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Create route that renders index.html template and finds data from mongo
#@app.route("/")
#def home(): 

    # Find data
#    mars_facts = mongo.db.collection.find_one()

    # Return template and data
#    return render_template("index.html", mars=mars_facts)

# Route that will trigger the scrape function
#@app.route("/scrape")
#def scrape():

    # Run the scrape function
#    mars_data = scrape_mars.scrape()

#    # Update the Mongo database using update and upsert=True
#    mongo.db.collection.update({}, mars_data, upsert=True)

#    # Redirect back to home page
#    return redirect("/")

#if __name__ == "__main__":
#    app.run(debug=True)
