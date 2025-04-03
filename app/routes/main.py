from flask import Blueprint, render_template
from app.models.user import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('base.html')

@main_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users) 