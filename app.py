from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from config import Config
from forms import SaleForm, ExpenseForm, ProductionForm, MedicalRecordForm
from models import db, Sale, Expense, Production, MedicalRecord

app = Flask(__name__)
app.config.from_object(Config) 
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales', methods=['GET', 'POST'])
def sales():
    form = SaleForm()
    if form.validate_on_submit():
        sale = Sale(
            date=form.date.data or datetime.utcnow(),
            quantity=form.quantity.data,
            unit_price=form.unit_price.data,
            total_amount=form.total_amount.data
        )
        db.session.add(sale)
        db.session.commit()
        flash('Sale record added successfully!', 'success')
        return redirect(url_for('sales'))
    return render_template('sales_form.html', form=form)

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(
            date=form.date.data or datetime.utcnow(),
            category=form.category.data,
            quantity=form.quantity.data,
            unit_price=form.unit_price.data,
            total_amount=form.total_amount.data
        )
        db.session.add(expense)
        db.session.commit()
        flash('Expense record added successfully!', 'success')
        return redirect(url_for('expenses'))
    return render_template('expenses_form.html', form=form)

@app.route('/production', methods=['GET', 'POST'])
def production():
    form = ProductionForm()
    if form.validate_on_submit():
        production = Production(
            date=form.date.data or datetime.utcnow(),
            good_eggs=form.good_eggs.data,
            cracked_eggs=form.cracked_eggs.data,
            trays_collected=form.trays_collected.data
        )
        db.session.add(production)
        db.session.commit()
        flash('Production record added successfully!', 'success')
        return redirect(url_for('production'))
    return render_template('production_form.html', form=form)

@app.route('/medical', methods=['GET', 'POST'])
def medical():
    form = MedicalRecordForm()
    if form.validate_on_submit():
        record = MedicalRecord(
            date=form.date.data or datetime.utcnow(),
            diagnosis=form.diagnosis.data,
            treatment=form.treatment.data,
            cost=form.cost.data
        )
        db.session.add(record)
        db.session.commit()
        flash('Medical record added successfully!', 'success')
        return redirect(url_for('medical'))
    return render_template('medical_form.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

