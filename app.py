import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries = [("Wizard return", "KDB is back! Klop said KDB is back from injury and the whole prem is shaking", "2024-02-01")]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_title = request.form.get("title") 
        entry_content = request.form.get("content")
        date = datetime.datetime.today().strftime("%Y-%m-%d") 
        print( entry_title,entry_content, date)
        entries.append((entry_title,entry_content, date))
    return render_template("index.html", entries=entries)
