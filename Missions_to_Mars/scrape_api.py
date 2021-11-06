from flask import Flask, render_template, redirect
from pymongo.mongo_client import MongoClient
# import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017")

