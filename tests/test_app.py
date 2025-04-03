import unittest
from app import create_app, db
from app.models.user import User

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_users_route(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_user_model(self):
        user = User(username='test_user', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        
        queried_user = User.query.filter_by(username='test_user').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, 'test@example.com')

if __name__ == '__main__':
    unittest.main() 