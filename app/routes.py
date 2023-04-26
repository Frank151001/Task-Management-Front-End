from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)
BACKEND_URL="http://127.0.0.1:5000"

@app.get("/")
def index():
    timestap = datetime.now().strftime("%F %H:%M:%S")
    return render_template("index.html", ts=timestap)

@app.get("/about")
def about_me():
    me={
        "First_Name":"Francisco",
        "Last_Name" :"Ibarra",
        "Hobbies":"Watch Movies"
    }
    return render_template("about.html", about=me)

@app.get("/tasks")
def display_all_tasks():
    url="%s/%s" % (BACKEND_URL, "tasks")
    resp= requests.get(url)
    if resp.status_code ==200:
        task_data = resp.json()
        return render_template("task_list.html", task=task_data["tasks"])
    return render_template("error.html", error_code=resp.status_code), resp.status_code

