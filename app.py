# Import Dependecies 
from Flask import Flask, render_template, redirect
from flask_pymongo import flask_pymongo
import scrape_mars
import os

# Flask app

app = Flask(__name__)

#Use flask_pymongo to set the connection
app.config["Mongo_UR"] = os.environ.get('authentication')
mongo = PyMongo

#Use flask_pymongo to set up local connection

@app.route("/")
def home() :

    # Find data 
    mars_info = mongo.db.mars_info.find_one()

    return render_template("index.html", mars_info=mars_info)


    #Route that will use the scrape function
    @app.route("/scrape")
    def scrape():

    #Run the scraped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemisspheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    










