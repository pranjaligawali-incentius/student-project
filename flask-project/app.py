import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pdb
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres123@localhost:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    languages = db.Column(db.String(200))
    def __repr__(self):
        return f'<student {self.name}>'


with app.app_context():
    db.create_all()

@app.route("/api/get_students", methods=['GET']) 
def get_students():
    all_students = student.query.order_by(student.id).all()
   
    output = []
    for s in all_students:
        output.append({
            "id": s.id, "name": s.name, "age": s.age, 
            "gender": s.gender, "languages": s.languages
        })
    return jsonify(output)

@app.route("/api/add", methods=['POST'])
def add():
   
    if request.method == 'POST':  
        name =request.json.get("name","")
        age = request.json.get('age',"")
        gender=request.json.get('gender',"")
        languages=request.json.get('languages',"")
        new_stud = student(name=request.json.get("name"), age=request.json.get("age"), gender=request.json.get("gender"), languages=request.json.get("languages"))
        db.session.add(new_stud)
        db.session.commit()
        return jsonify(ok=True)

    



@app.route("/api/edit/<int:id>", methods=['POST'])
def edit(id):
    stud = student.query.get(id) 
    if stud:
       
        data = request.json
        stud.name = data.get("name")
        stud.age = data.get("age")
        stud.gender = data.get("gender")
        stud.languages = data.get("languages")
        db.session.commit()
        return jsonify(ok=True)
    return jsonify(ok=False) 

@app.route("/api/delete/<int:id>",methods=['DELETE'])  
def delete(id):
    
    stud=student.query.get(id)
    
    if stud:
      db.session.delete(stud)
      db.session.commit()
      return jsonify(ok=True,message="successfully deleted")
    return jsonify(ok=False,message="Not deleted")



if __name__ == "__main__":
    app.run(debug=True)