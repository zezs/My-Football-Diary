import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")
client = MongoClient("mongodb+srv://{}:{}@footall-diary.qe8s4ox.mongodb.net/".format(mongo_username, mongo_password))
#client = MongoClient("mongodb+srv://username:password@footall-diary.qe8s4ox.mongodb.net/")
app.db = client.footballdiary



# entries = [("Wizard returns", "KDB is back! Klopp said KDB is back from injury and all prem teams are shaking", "2024-02-01")]

@app.route("/", methods=["GET", "POST"])
def home():
    print([e for e in app.db.enries.find({})])
    if request.method == "POST":
        entry_title = request.form.get("title") 
        entry_content = request.form.get("content")
        date = datetime.datetime.today().strftime("%Y-%m-%d") 
        # print( entry_title,entry_content, date)
        # entries.append((entry_title, entry_content, date))
        app.db.entries.insert_one({"title": entry_title, "content": entry_content, "date": date})

    entries_with_date = [
            (
                entry["title"],
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
    ]

    return render_template("index.html", entries = entries_with_date)
