from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.expense import Expense
from datetime import datetime

expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')

DEFAULT_EXPENSE_CATEGORIES = [
    "Food & Dining", "Transportation", "Housing", "Utilities", "Healthcare",
    "Entertainment", "Clothing", "Education", "Personal Care", "Miscellaneous"
]

@expenses_bp.route('/', methods=['GET', 'POST'])
@login_required
def expenses():
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form.get('description', '')
        date_str = request.form['date']
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            date = datetime.utcnow().date()

        expense = Expense(
            category=category, amount=amount,
            description=description, date=date,
            user_id=current_user.id
        )
        db.session.add(expense)
        db.session.commit()
        flash('Expense added')
        return redirect(url_for('expenses.expenses'))

    expenses_list = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()
    return render_template('expenses.html', expenses=expenses_list, default_categories=DEFAULT_EXPENSE_CATEGORIES, current_date=datetime.utcnow().strftime('%Y-%m-%d'))

@expenses_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.description = request.form.get('description', '')
        date_str = request.form['date']
        try:
            expense.date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            pass
        db.session.commit()
        flash('Expense updated')
        return redirect(url_for('expenses.expenses'))
    return render_template('edit_expense.html', expense=expense)

@expenses_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted')
    return redirect(url_for('expenses.expenses'))
