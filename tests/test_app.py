from flask import url_for
from flask_testing import TestCase
from application import app, db, routes
from application.models import Items

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.drop_all()
        db.create_all()
        item = Items(description="new item")
        db.session.add(item)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()