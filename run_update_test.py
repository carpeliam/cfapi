import os
# import run_update
import unittest
import tempfile

class RunUpdateTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['DATABASE_URL'] = 'postgres://postgres@localhost/civic_json_worker_test'
        os.environ['SECRET_KEY'] = '123456'

        from app import db

        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.drop_all()

    def testNothin(self):
        pass

if __name__ == '__main__':
    unittest.main()