from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.salary import salary_bp
from routes.expenses import expenses_bp
from routes.insights import insights_bp

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(salary_bp)
app.register_blueprint(expenses_bp)
app.register_blueprint(insights_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
