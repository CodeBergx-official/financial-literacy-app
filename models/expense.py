from . import db
from datetime import datetime

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(256))
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='expenses')

    def __repr__(self):
        return f'<Expense {self.category} {self.amount}>'
