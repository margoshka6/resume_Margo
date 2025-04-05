import pandas as pd
import numpy as np
from flask import Flask,render_template
import os
def index():
    data=pd.read_csv("Ріта.csv")
    photo="мый.png"
    name=data[data["category"]=="name"]["text"].values[0]
    position=data[data["category"]=="position"]["text"].values[0]
    contacts=data[data["category"]=="contacts"][["text","link"]].replace({no.nan:None}).values
    skills=data[data["category"]=="skills"]["text"].values
    projects=data[data["category"]=="projects"][["text","link"]].replace({no.nan:None}).values
    education=data[data["category"]=="education"]["text"].values
    achivments=data[data["category"]=="achivments"]["text"].values
    facts=data[data["category"]=="facts"]["text"].values
    return render_template("index.html",name=name,photo=photo,position=position,contscts=contacts,skills=skills,projects=projects,education=education,achivments=achivments,facts=facts)

folder=os.getcwd()
app=Flask(__name__,template_folder=folder,static_folder=folder)
app.add_url_rule("/","index",index)
app.run()


