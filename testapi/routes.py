# Author:       Trevor Strobel
# Date:         9/7/2022

from flask import request
from testapi import app
from testapi.models import Widget
from datetime import datetime




# create databse tabels if they're not already there

from testapi import db
try:
    db.create_all()
    print("tables created successfully")
except:
    print("Table creation failed.")


#helper function to strip db rows of the "row" object.
def rowToDict(row):
    x = {}
    for col in row.__table__.columns:
        x[col.name] = str(getattr(row, col.name))

    return x



#default route. nothing to see here as this is an api and does not contain front end work. 
@app.route("/", methods=["GET", "POST"])
def hello():
    return "hello all!"

# to retreive records for all widgets in the DB. 
@app.route("/widget", methods=["GET"])
@app.route("/widget/", methods=["GET"])
def widget():
    result = []
    widgs = Widget.query.with_entities(Widget.id, Widget.name, Widget.parts, Widget.date_create, Widget.date_update).all()
    #widgs = Widget.query.first()
    for w in Widget.query.all():
        result.append(rowToDict(w))
    return result

    


# To retrieve a record for a single widget given a name
@app.route("/widget/<wname>", methods=['GET', 'DELETE'])
@app.route("/widget/<wname>/", methods=['GET', 'DELETE'])
def get_widget(wname):
    w = Widget.query.filter_by(name=wname).first()
    if request.method == "GET":   
        return w.as_dict()
    if request.method == "DELETE":
        db.session.delete(w)
        db.session.commit()
        return 

# to create or update a record for a single widget in the DB
@app.route("/widget/<wname>/<int:no_parts>", methods=['POST'])
@app.route("/widget/<wname>/<int:no_parts>/", methods=['POST'])
def alter_Widget(wname, no_parts):
    w = Widget.query.filter_by(name=wname).first()
    print(type(w))

    if(w == None): #if the record doesn't exist, let's create it.
        widg = Widget(name = wname, parts = no_parts)
        db.session.add(widg)
        db.session.commit()
        return "<p>Record created</p>"
    elif(type(w) != None):                  #if the record already exists...update the existing one.
        w.parts = no_parts
        w.date_update = datetime.utcnow()
        db.session.commit()
        return "<p>Record Updated.</p>"

        
        
        
    




