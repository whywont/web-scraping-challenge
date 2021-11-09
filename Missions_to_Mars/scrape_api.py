from flask import Flask, render_template, redirect
from pymongo.mongo_client import MongoClient
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

#create client
client = MongoClient("mongodb://localhost:27017")

#create db and collection
db = client.mars_db
mars_data = db.mars_collection

@app.route('/')
def index():

    #Find one record of data from the mongo database
    find_data = mars_data.find_one()
    return render_template("index.html", data=find_data)

@app.route("/scrape")
def mars_scrape():

    #run scrape and insert into db
    mars_scrape_data = scrape_mars.scrape()
    mars_data.insert_one(mars_scrape_data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


