from . import db

class Salary(db.Model):
    __tablename__ = 'salaries'
    id = db.Column(db.Integer, primary_key=True)
    gross_salary = db.Column(db.Float, nullable=False)
    deductions = db.Column(db.JSON, nullable=True)
    net_salary = db.Column(db.Float, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship('User', back_populates='salary')

    def __repr__(self):
        return f'<Salary User {self.user_id} Gross {self.gross_salary}>'
