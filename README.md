# e2e-playwright
Front end automation demo built using [Playwright](https://playwright.dev/python/) on Python 3 using the Page Object Model.   
The website under test is [SauceLabs](https://saucelabs.com)' demo [store](https://www.saucedemo.com/).

## Requirements
Modern version of [python3](https://www.python.org/downloads/), ie. 3.7 or newer.

## Installation
Set up environment:
```sh
$ git clone <repo url>
$ cd e2e-playwright
$ python3 -m venv .
$ source bin/activate
$ pip install -r requirements.txt
$ playwright install
```

## Run
#### Run all tests:
```sh
$ pytest
```

#### Run in headed mode and slow down operations:
```sh
$ pytest --headed --slowmo 1000
```

#### Run with Playwright Inspector:
```sh
$ PWDEBUG=1 pytest -s
```

## Features
#### Data driven tests
Parameterization of arguments in a test function with 
pytest.mark.parameterize [here](https://github.com/richlee33/e2e-playwright/blob/180efd7e131e0f61d5be2dd22002d92255da0c01/tests/test_checkout_2.py#L21).
```shell script
    testcases_item_total = [
        ("bikelight", "backpack", "39.98"),
        ("bolttshirt", "jacket", "65.98"),
    ]

    @pytest.mark.parametrize("item_1, item_2, total", testcases_item_total)
    def test_item_total(self, page: Page, item_1, item_2, total):
```

#### Fixture for shared setup step
Each test function in the test class will call the pytest fixture to go to the
home page and log in as a standard user.  See [here](https://github.com/richlee33/e2e-playwright/blob/180efd7e131e0f61d5be2dd22002d92255da0c01/tests/test_cart.py#L10).
```shell script
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self, page: Page):
        self.go_home_and_login_standard_user(page)
        yield
```
