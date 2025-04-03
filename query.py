from app import db, create_app
from app.models.user import User

def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # Create the database tables
        db.create_all()
        
        # Add some sample users
        add_user('john_doe', 'john@example.com')
        add_user('jane_doe', 'jane@example.com')
        print("Sample users added successfully!") 