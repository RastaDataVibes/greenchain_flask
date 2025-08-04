from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=True)
    unit_price = db.Column(db.Float, nullable=True)
    total_amount = db.Column(db.Float, nullable=False)

class Production(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    good_eggs = db.Column(db.Integer, nullable=False)
    cracked_eggs = db.Column(db.Integer, nullable=False)
    trays_collected = db.Column(db.Float, nullable=False)

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    diagnosis = db.Column(db.String(100), nullable=False)
    treatment = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)

