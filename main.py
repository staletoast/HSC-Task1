from datetime import datetime, timedelta
import time
from flask import Flask, render_template, request, redirect, session
import user_management as dbHandler

# Code snippet for logging a message
# app.logger.critical("message")

app = Flask(__name__)
app.secret_key = 'secretkeyhere' #do this later
app.permanent_session_lifetime = timedelta(days=1)
app.currentUser = " "

'''
def countdown(): #countdown for session timeout
    timeout_duration = 2 * 60
    while timeout_duration > 0:
        print(f"Time remaining: {timeout_duration} seconds")
        time.sleep(1)
        timeout_duration -= 1
    print("Timeout reached!")
    exit()
'''

@app.route("/signup.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def signup(): #signup
    session.permanent = True
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        DoB = request.form["dob"]
        dbHandler.insertUser(username, password, DoB)
        return render_template("/index.html")
    else:
        return render_template("/signup.html")

@app.route("/success.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addEntry(): 
    session.permanent = True
    developer = app.currentUser
    if developer == " ":
        return render_template("/index.html")
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        entry = request.form["entry"]
        project = request.form["project"]
        timecreated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # timestamp
        dbHandler.insertEntry(entry, developer, project, timecreated)
        dbHandler.listEntry()
        return render_template("/success.html", state=True, value="Back")
    else:
        dbHandler.listEntry()
        return render_template("/success.html", state=True, value="Back")

@app.route("/index.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
@app.route("/", methods=["POST", "GET"])
def home(): #homepage
    session.permanent = True
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        isLoggedIn = dbHandler.retrieveUsers(username, password)
        if isLoggedIn:
            dbHandler.listEntry()
            app.currentUser = username
            return render_template("/success.html", value=username, state=isLoggedIn)
        else:
            return render_template("/index.html")
    else:
        return render_template("/index.html")

@app.route("/search.html", methods=["GET", "POST"])
def searchEntries():
    session.permanent = True
    if request.method == "POST":
        developer = request.form.get("developer")
        project = request.form.get("project")
        timecreated = request.form.get("timecreated")
        entry = request.form.get("entry")
        
        results = dbHandler.searchEntries(entry, developer, project, timecreated)
        return render_template("/search.html", results=results)
    else:
        return render_template("/search.html", results=[])

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    #countdown()
    app.run(debug=True, host="0.0.0.0", port=5000)