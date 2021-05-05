import unittest
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Games

port = 5000

class TestBase(LiveServerTestCase):
    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            DEBUG=True
        )

        return app

    def setUp(self):
        chrome_options = Options()

        chrome_options.binary_location = "/usr/bin/chromium-browser"

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9222")

        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)

        db.create_all()

        self.driver.get(f'http://localhost:{port}')

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{port}')
        self.assertEqual(response.code, 200)

class TestCreate(TestBase):
    def test_create(self):
        pass

if __name__=='__main__':
    unittest.main(port=port)