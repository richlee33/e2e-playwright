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
