from flask import Flask, render_template, request, redirect, session
from datetime import timedelta, datetime
import time
import user_management as dbHandler
import threading

# Code snippet for logging a message
# app.logger.critical("message")

app = Flask(__name__)
app.secret_key = 'secretkeyhere' #do this later
app.permanent_session_lifetime = timedelta(minutes=1)
print("TIMEOUT VAL", app.permanent_session_lifetime)

def check_session_timeout():
    while True:
        time.sleep(1)  # Check every second
        if 'last_activity' in session:
            session_age = datetime.now() - session['last_activity']
            if session_age > app.permanent_session_lifetime:
                session.clear()
                print("SESSION TIMEOUT!!")
            else:
                print(f"SESSION: {session_age}")

@app.route("/success.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addFeedback():
    session.permanent = True
    session['last_activity'] = datetime.now()
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        feedback = request.form["feedback"]
        dbHandler.insertFeedback(feedback)
        dbHandler.listFeedback()
        return render_template("/success.html", state=True, value="Back")
    else:
        dbHandler.listFeedback()
        return render_template("/success.html", state=True, value="Back")


@app.route("/signup.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def signup():
    session.permanent = True
    session['last_activity'] = datetime.now()
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


@app.route("/index.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
@app.route("/", methods=["POST", "GET"])
def home():
    session.permanent = True
    session['last_activity'] = datetime.now()
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return redirect(url, code=302)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        isLoggedIn = dbHandler.retrieveUsers(username, password)
        if isLoggedIn:
            dbHandler.listFeedback()
            return render_template("/success.html", value=username, state=isLoggedIn)
        else:
            return render_template("/index.html")
    else:
        return render_template("/index.html")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    threading.Thread(target=check_session_timeout, daemon=True).start()
    app.run(debug=True, host="0.0.0.0", port=5000)
