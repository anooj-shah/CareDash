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
  reviews = db.relationship('Review', backref='author', lazy=True)

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
  print(doc)
  return jsonify(id=doc.id, name=doc.name, reviews=doc.reviews)

@app.route('/doctors/<doctor_id>/reviews/<review_id>', methods=['GET'])
def get_doctor_review(doctor_id, review_id):
  doc = Doctor.query.get(doctor_id)
  doc_reviews = doc.reviews
  for i in doc.reviews:
    if i.id == review_id:
      return jsonify(id=i.id,doctor_id=i.doctor_id)
  return jsonify()
  # print(doc)
  # return jsonify(id=doc.id, name=doc.name, reviews=doc.reviews)

@app.route('/doctors', methods=['GET'])
def get_all_doctors_and_reviews():
  # doctors_all = Doctor.query.all()
  return "test"
  # return jsonify(doctors_all)

@app.route('/doctors/<doctor_id>/reviews/<review_id>', methods=['DELETE'])
def delete_doctor_review(doctor_id, review_id):
  doc = Doctor.query.get(doctor_id)
  doc_reviews = doc.reviews
  for i in doc.reviews:
    if i.id == review_id:
      review = doc.reviews.query.get(review_id)
  db.session.delete(doc)
  db.session.commit()
  return "success"

@app.route('/doctors/<doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
  # Doctor.query.filter(Doctor.id == doctor_id).delete()
  doc = Doctor.query.get(doctor_id)
  db.session.delete(doc)
  db.session.commit()
  return "success"

if __name__ == '__main__':
    app.run()