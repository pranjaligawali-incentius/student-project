import os
from flask import Flask, render_template, request, url_for, redirect, jsonify,session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres123@localhost:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.secret_key = os.urandom(24)
class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    languages = db.Column(db.String(200))
    value=db.Column(db.Boolean(False))
   
    def __repr__(self):
        return f'<student {self.name}>'

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    email=db.Column(db.String(100))
    hashed_password=db.Column(db.String(500))
 
    
    def __repr__(self):
        return f'<user {user.username}>'
    

with app.app_context():
    db.create_all()

@app.route("/api/register", methods=["POST"])
def register():
    if request.method=="POST":
        username=request.json.get("username","")
        email=request.json.get("email","")
        password=request.json.get("password","")
        u=user.query.filter_by(email=email).all()
        
        if u:
            return jsonify(ok=False,message="User already exist")  
        
        if username and password:
            new_user=user(username=username,email=email,hashed_password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return jsonify(ok=True)
        
@app.route("/api/login" ,methods=["POST"])
def login():
    
    if request.method=="POST":
        username=request.json.get("username")
        password=request.json.get("password")

        u=user.query.filter_by(username=username).first()
        if u is not None and check_password_hash(u.hashed_password, password):
            session['username']=username
            session['email']=request.json.get("email","")
            return jsonify(ok=True,message="SuccessFully Login")
        return jsonify(ok=False,message="Invalid Credential")
    

@app.route("/api/get_authenticated",methods=["GET"])
def get_authenticated():
    if request.method=="GET":
      username=request.json.get("username")
      email=request.json.get("email")
      u=user.query.filter_by(username=username).first()
      if session.get('username'):
         session["username"]=request.json.get("username")
         session["email"]=request.json.get("email")
         return jsonify(ok=True,message="Authenticated User")
      return jsonify(ok=False,message="Not authencticated")


@app.route("/api/get_students", methods=['GET']) 
def get_students():
    all_students = student.query.order_by(student.id).all()
   
    output = []
    for s in all_students:
        output.append({
            "id": s.id, "name": s.name, "age": s.age, 
            "gender": s.gender, "languages": s.languages,"value":s.value
        })
    return jsonify(output)

@app.route("/api/add", methods=['POST'])
def add():
   
    if request.method == 'POST':  
        name =request.json.get("name","")
        age = request.json.get('age',"")
        gender=request.json.get('gender',"")
        languages=request.json.get('languages',"")
        languages = ",".join(languages)
        value=request.json.get('value',"")
        new_stud = student(name=name, age=age, gender=gender, languages=languages,value=value)
        db.session.add(new_stud)
        db.session.commit()
        return jsonify(ok=True)

    



@app.route("/api/get_student/<int:id>", methods=['GET'])
def get_single_student(id):
    stud = student.query.get(id)
    if stud:
        return jsonify({
            "name": stud.name, 
            "age": stud.age,
            "gender": stud.gender,
            "languages": stud.languages.split(",") ,##convert to array
            "value":stud.value
            
        })            
    return jsonify({"error": "Not found"})


@app.route("/api/edit/<int:id>", methods=['POST'])
def edit(id):
    stud = student.query.get(id) 
    if stud:
        data = request.json
        stud.name = data.get("name")
        stud.age = data.get("age")
        stud.gender = data.get("gender")
        stud.languages = data.get("languages")
        stud.value=data.get("value")
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