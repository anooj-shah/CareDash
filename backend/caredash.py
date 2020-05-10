import json
from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Doctor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  reviews = db.relationship('Review', backref='author', lazy=True, cascade = "all, delete, delete-orphan")

  def __repr__(self):
    return f"Doctor('')"

class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text, nullable=False)
  doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)

  def __repr__(self):
    return f"Review('')"

@app.route('/', methods=['GET'])
def home():
  return "successtest"

@app.route('/doctors', methods=['POST'])
def create_doctor():
  content = request.json
  doctor_name = content['name']
  print(doctor_name)
  doc = Doctor(name=doctor_name,reviews=[])
  db.session.add(doc)
  db.session.commit()
  return "success - added new doctor"

@app.route('/doctors/<doctor_id>/reviews', methods=['POST'])
def add_doctor_review(doctor_id):
  content = request.json
  description = content['description']
  doc_review = Review(description=description, doctor_id=doctor_id)
  db.session.add(doc_review)
  db.session.commit()
  return "success - added new doctor review"

@app.route('/doctors/<doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
  doc = Doctor.query.get(doctor_id)
  output = {}
  output['name'] = doc.name
  output['id'] = doc.id
  reviews = []
  for i in doc.reviews:
    review_object = {}
    review_object['id'] = i.id
    review_object['doctor_id'] = doc.id
    review_object['description'] = i.description
    reviews.append(review_object)
  output['reviews'] = reviews
  return json.dumps(output)

@app.route('/doctors/<doctor_id>/reviews/<review_id>', methods=['GET'])
def get_doctor_review(doctor_id, review_id):
  doc = Doctor.query.get(doctor_id)
  doc_reviews = doc.reviews
  review_object = {}
  for i in doc.reviews:
    if int(i.id) == int(review_id):
      review_object = {}
      review_object['id'] = i.id
      review_object['doctor_id'] = doc.id
      review_object['description'] = i.description
  return json.dumps(review_object)

@app.route('/doctors', methods=['GET'])
def get_all_doctors_and_reviews():
  doctors_all = Doctor.query.all()
  doctors_arr = []
  reviews = []
  review_object = {}
  curr_doc = {}
  for i in doctors_all:
    curr_doc = {}
    curr_doc['name'] = i.name
    curr_doc['id'] = i.id
    reviews = []
    for j in i.reviews:
      review_object = {}
      review_object['id'] = j.id
      review_object['doctor_id'] = i.id
      review_object['description'] = j.description
      reviews.append(review_object)
    curr_doc['reviews'] = reviews
    doctors_arr.append(curr_doc)
  return json.dumps(doctors_arr)

@app.route('/doctors/<doctor_id>/reviews/<review_id>', methods=['DELETE'])
def delete_doctor_review(doctor_id, review_id):
  doc = Doctor.query.filter_by(id=doctor_id).first()
  doc_reviews = doc.reviews
  for i in doc.reviews:
    if int(i.id) == int(review_id):
      review = Review.query.filter_by(id=review_id).first()
      db.session.delete(review)
  db.session.commit()
  return "success"

@app.route('/doctors/<doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
  # rows_deleted = db.session.query(Doctor).filter(Doctor.id == 1).delete(synchronize_session='evaluate')
  delete = Doctor.query.filter_by(id=doctor_id).first()
  db.session.delete(delete)
  db.session.commit()
  return "success"

if __name__ == '__main__':
  app.run()
