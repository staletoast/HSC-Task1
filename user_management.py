import sqlite3 as sql
import time
import random


def insertUser(username, password, DoB):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (username,password,dateOfBirth) VALUES (?,?,?)",
        (username, password, DoB),
    )
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
    if cur.fetchone() == None:
        con.close()
        return False
    else:
        cur.execute(f"SELECT * FROM users WHERE password = '{password}'")
        # Plain text log of visitor count as requested by Unsecure PWA management
        with open("visitor_log.txt", "r") as file:
            number = int(file.read().strip())
            number += 1
        with open("visitor_log.txt", "w") as file:
            file.write(str(number))
        # Simulate response time of heavy app for testing purposes
        time.sleep(random.randint(80, 90) / 1000)
        if cur.fetchone() == None:
            con.close()
            return False
        else:
            con.close()
            return True


def insertEntry(entry,developer,project,timecreated):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO entry (entry,developer,project,timecreated) VALUES ('{entry}','{developer}','{project}','{timecreated}')")
    con.commit()
    con.close()


def listEntry():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM entry").fetchall()
    con.close()
    f = open("templates/partials/success_entries.html", "w")
    for row in data:
        f.write("<p>\n")
        f.write(f"Developer: {row[2]}\n")
        f.write("</p>\n")
        f.write("<p>\n")
        f.write(f"Project: {row[3]}\n")
        f.write("</p>\n")
        f.write("<p>\n") 
        f.write(f"Date/Time: {row[4]}\n")
        f.write("</p>\n")
        f.write("<p>\n") 
        f.write(f"Log Entry: {row[1]}\n") 
        f.write("</p>\n")
        f.write("<p>\n ________________</p>")
    f.close()

def searchEntries(entry, developer, project, timecreated):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    query = "SELECT * FROM entry WHERE 1=1"
    params = []
    
    checkval = int
    checkval = 0
    if developer:
        query += " AND developer LIKE ?"
        params.append(f"%{developer}%")
        checkval = 1
    if project:
        query += " AND project LIKE ?"
        params.append(f"%{project}%")
        checkval = 1
    if timecreated:
        query += " AND timecreated LIKE ?"
        params.append(f"%{timecreated}%")
        checkval = 1
    if entry:
        query += " AND entry LIKE ?"
        params.append(f"%{entry}%")
        checkval = 1

    if checkval > 0:
        cur.execute(query, params)
        results = cur.fetchall()
        con.close()
        return results
    else: 
        con.close()
        results=[]
        return results