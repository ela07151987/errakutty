'''
Created on Dec 10, 2020

@author: EXE2KQF
'''
from flask import Flask, render_template, abort, request, url_for, redirect
from datetime import datetime
from pythonproj.data import db, save_data


app = Flask(__name__)
@app.route("/")
def welcome():
    return render_template("welcome.html", message="You logged in @" + str(datetime.now()), indxs=db)

@app.route("/event")
def event():
    return render_template("event.html")

@app.route('/contact/<int:indx>')
def contact(indx):  
    try: 
        index = db[indx]
        return render_template("listcontact.html", 
                               index=index, 
                               indx=indx,
                               indx_max=len(db)-1)
    except IndexError:
        abort(404)
        
@app.route("/api/contact/<int:indx>")
def rest_contact(indx):
    try:
        return db[indx]
    except IndexError:    
        abort(400)
        
@app.route("/add_con", methods=["POST", "GET"])
def add_con():
    if request.method == "POST":
            contact={"Name":request.form['Name'],"Contact":request.form['Contact'],
             "Place":request.form['Place'],"Details":request.form['Details']}
            db.append(contact)
            save_data()
            return redirect(url_for("contact", indx=len(db)-1))
    else:
            return render_template("add_con.html")
        

@app.route("/remove_con/<int:indx>", methods=["GET", "POST"])
def remove_con(indx):
    try:
        if request.method == "POST":
            del db[indx]
            save_data()
            return redirect(url_for("welcome"))
        else:
            return render_template("remove_con.html", card=db[indx])
    except:
        abort(404)
