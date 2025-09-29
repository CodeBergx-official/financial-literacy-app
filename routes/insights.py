from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.salary import Salary
from models.expense import Expense

insights_bp = Blueprint('insights', __name__, url_prefix='/insights')

@insights_bp.route('/')
@login_required
def insights():
    salary = Salary.query.filter_by(user_id=current_user.id).first()
    expenses = Expense.query.filter_by(user_id=current_user.id).all()

    total_expenses = sum(e.amount for e in expenses)
    savings = (salary.net_salary if salary else 0) - total_expenses

    categories = {}
    for e in expenses:
        categories[e.category] = categories.get(e.category, 0) + e.amount

    top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]
    overspending = any(val > (salary.net_salary * 0.5 if salary else 0) for val in categories.values())
    saving_positive = savings > 0

    return render_template(
        'insights.html',
        savings=savings,
        top_categories=top_categories,
        overspending=overspending,
        saving_positive=saving_positive
    )
