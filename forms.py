from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, FloatField, DateField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional

class SaleForm(FlaskForm):
    date = DateField('Date', validators=[Optional()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit_price = FloatField('Unit Price', validators=[DataRequired()])
    total_amount = FloatField('Total Amount', validators=[DataRequired()])
    submit = SubmitField('Submit Sale')

class ExpenseForm(FlaskForm):
    date = DateField('Date', validators=[Optional()])
    category = SelectField('Category', choices=[
        ('maize_brand', 'Maize Brand'),
        ('concentrate', 'Concentrate'),
        ('diesel', 'Diesel'),
        ('gasoline', 'Gasoline'),
        ('labor', 'Labor'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    quantity = FloatField('Quantity', validators=[Optional()])
    unit_price = FloatField('Unit Price', validators=[Optional()])
    total_amount = FloatField('Total Amount', validators=[DataRequired()])
    submit = SubmitField('Submit Expense')

class ProductionForm(FlaskForm):
    date = DateField('Date', validators=[Optional()])
    good_eggs = IntegerField('Good Eggs', validators=[DataRequired()])
    cracked_eggs = IntegerField('Cracked Eggs', validators=[DataRequired()])
    trays_collected = FloatField('Trays Collected', validators=[DataRequired()])
    submit = SubmitField('Submit Production')

class MedicalRecordForm(FlaskForm):
    date = DateField('Date', validators=[Optional()])
    diagnosis = StringField('Diagnosis', validators=[DataRequired()])
    treatment = StringField('Treatment', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    submit = SubmitField('Submit Medical Record')

