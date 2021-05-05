## Overview

Integration testing is a type of software testing in which we test the application as a whole, rather than mocking the application to it's routes as we do in unit testing.  

We will use the Python package `selenium` to simulate a user interacting with our application directly, and test the results are as expected.  

### Setup

We can use the `LiveServerTestCase` class to create a live instance of our application for our integration tests to use, so we don't need the application to be running for the tests to work.

```py
from flask_testing import LiveServerTestCase
```

We must create a subclass of this, and define the following methods:

1. `create_app`: run once, at the very start of testing - here, we overwrite the app's config
2. `setUp`: run before every test case - here, we setup the driver and create our test database
3. `tearDown`: run after every test case - here, we quit the driver and drop the test database

<details>
<summary>Example</summary>

```py
from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db" # change to a test sqlite database
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless') # must be headless

        self.driver = webdriver.Chrome(options=chrome_options) 

        db.create_all() # create schema before we try to get the page
        self.driver.get(f'http://localhost:5000/')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()
```


*Note: in order to use Selenium, we must have a browser and driver installed. See the tutorial for installation steps.*

</details>
<br/>


### Test Cases

Once we have set-up a `TestBase` class, which inherits from the `LiveServerTestCase` class, we can define some test cases using the driver we instantiated.

Each test case must be defined within a class which inherits from `TestBase`. It should look something like this:

```py
class TestBase(LiveServerTestCase):
    ...

class TestCase(TestBase):
    def test_case_1(self):
        ...
```


### Selenium

#### XPaths

XPaths are essentially a way to find any element, such as an input field or button, on any HTML or XML document. 

Selenium can use this XPath to find the element we want to manipulate in our testing.

<details>
<summary>Finding the XPath of an element in Chrome</summary>

1. Right click on the element, and click `Inspect`. The HTML for the element should pop up.
2. Right click on the HTML for the element in the inspect tab, it should be highlighted.
3. Choose `Copy`, and then `Copy XPath`.

[![Image from Gyazo](https://i.gyazo.com/a51aa3f28708f1754a7ffc13f269a384.gif)](https://gyazo.com/a51aa3f28708f1754a7ffc13f269a384)

</details>
<br/>

#### Elements

We can use the `selenium` driver to find elements on a page, and do *things* with these elements.

We use the following syntax to find an element on the page:
```py
element = self.driver.find_element_by_xpath('<XPath>')
```

We can then use any of the following methods on this element:
```py
element.click()
element.send_keys('<any string>') # simulates typing
element.clear()
```

We can also inspect the text inside the element using
```py
element.text
```

<details>
<summary>Example</summary>

Let's assume our application has an input box on the `/create` route. When this box is submitted, the user is directed to `/index`.

```py
from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db

class TestBase(LiveServerTestCase):
    ...

class TestCreate(TestBase):
    def test_create(self):
        self.driver.get(f'http://localhost:5000/create') # go to /create route

        input_box = self.driver.find_element_by_xpath('//*[@id="name"]')
        input_box.send_keys('Hello World')

        self.driver.find_element_by_xpath('//*[@id="submit"]').click() # submit field

        assert self.driver.current_url == 'http://localhost:5000/index'
```

*Note: `LiveServerTestCase` has built in methods for `assertEqual`, `assertIn`, etc. that we may choose to use instead of `assert`.*
</details>

<br/>


## Tutorial

### Requirements

An **Ubuntu 18.04** VM with Python installed. This is unlikely to work on Ubuntu 20.04.

### Setup

Run the following commands to install `chromium-browser` and `chromedriver`:

Installing the browser
```bash
sudo apt install chromium-browser -y
```

Installing the driver
```
sudo apt install wget unzip -y
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip
```



