from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.salary import Salary

salary_bp = Blueprint('salary', __name__, url_prefix='/salary')

DEFAULT_DEDUCTIONS = {
    'Tax': 0.10,
    'Provident Fund': 0.12,
    'Insurance': 0.05,  # Added default insurance deduction at 5%
    'Other': 0.03
}


@salary_bp.route('/', methods=['GET', 'POST'])
@login_required
def manage_salary():
    salary = Salary.query.filter_by(user_id=current_user.id).first()
    
    if request.method == 'POST':
        gross = float(request.form['gross_salary'])
        
        deductions = {}
        # Fixed deductions (except 'Other')
        for key in DEFAULT_DEDUCTIONS:
            if key != 'Other':
                try:
                    rate = float(request.form.get(f'deductions[{key}]', DEFAULT_DEDUCTIONS[key]))
                except ValueError:
                    rate = DEFAULT_DEDUCTIONS[key]
                deductions[key] = rate
        
        # Add dynamic deductions from form
        names = request.form.getlist('deduction_name[]')
        rates = request.form.getlist('deduction_rate[]')
        for n, r in zip(names, rates):
            if n.strip() and r.strip():
                try:
                    rate_val = float(r)
                    if rate_val >= 0:
                        deductions[n.strip()] = rate_val
                except ValueError:
                    continue
        
        # Always add 'Other' deduction without tooltip
        other_rate = salary.deductions.get('Other', DEFAULT_DEDUCTIONS['Other']) if salary and salary.deductions else DEFAULT_DEDUCTIONS['Other']
        try:
            other_form_val = float(request.form.get('deductions[Other]', other_rate))
            deductions['Other'] = other_form_val
        except ValueError:
            deductions['Other'] = other_rate

        net = gross - sum(gross * rate for rate in deductions.values())
        
        if not salary:
            salary = Salary(user_id=current_user.id)
            db.session.add(salary)
        
        salary.gross_salary = gross
        salary.deductions = deductions
        salary.net_salary = net
        db.session.commit()
        
        flash("Salary updated.")
        return redirect(url_for('salary.manage_salary'))
    
    # Initialize defaults if no salary record
    if not salary:
        salary = Salary(gross_salary=0, deductions=DEFAULT_DEDUCTIONS.copy(), net_salary=0)
    
    if not salary.deductions:
        salary.deductions = DEFAULT_DEDUCTIONS.copy()

    return render_template('salary.html', salary=salary, defaults=DEFAULT_DEDUCTIONS)
