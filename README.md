## Overview
This project is a robust testing framework developed with Python to assist Quality Assurance (QA) engineers in automating both API and UI testing. This framework integrates widely-used libraries and tools, offering a complete solution for test automation. The project provides a thorough testing suite covering various aspects of a web application, such as API endpoints, database operations, and user interface interactions. It employs Python as the main programming language, with pytest for test execution and Selenium for UI automation, ensuring a reliable and efficient testing process.

## Features
* API Testing: The project includes testing of APIs using the requests library to interact with the API endpoints and validate the responses.
* Database Testing: Database testing is performed using Python libraries such as pytest and SQL connectors to ensure data integrity and accuracy.
* UI Testing: UI testing is conducted using Selenium WebDriver to automate interactions with web applications and validate their behavior.

## Project Structure
```
IvakhniukQAAuto/
├── modules/
│   ├── api/
│   │   └── clients/
│   │       ├── github.py 
│   ├── common/
│   │   └── database.py
│   └── ui/
│       └── page_object/ 
│           ├── cosibella/
│           │   ├── cart_page.py
│           │   ├── item_page.py
|           |   ├── main_page.py
|           |   └──  search_result.py
│           ├── base_page.py
│           ├── github_sign_in_page.py
├── tests/
│   ├── api/
│   │   ├── test_api.py
│   │   ├── test_fixtures.py 
│   │   ├── test_github_api.py 
│   │   ├── test_http.py 
│   ├── database/
│   │   └── test_database.py
│   └── ui/
|       ├── cosibella_tests/
│       │   ├── test_cart_page.py
│       ├── test_ui.py
│       ├── test_ui_page_object.py
├── .gitignore
├── README.md
├── conftest.py
├── pytest.ini
└── become_qa_auto.db
```
## Installation
To use this framework, you need to have Python 3.12.1 or higher installed.

## Running Tests
The framework uses pytest for running tests. Below are examples of how to run different types of tests.

### Run All Tests
To run all tests, execute the following command:
```
pytest
```
### Run Tests by Marker
You can run tests by specific markers. Here are some examples:

- Run API Tests:
```
pytest -m api
```
- Run Database Tests:
```
pytest -m database
```
### Running UI Tests
To run the UI tests in this framework, you need to have pytest and selenium installed. You can install them via pip if you haven't already:
```
pip install pytest selenium
```
### Running UI Tests by Markers
* Run GitHub UI Tests:
```
pytest -m ui
```
* Run Cosibella UI Tests:
```
pytest -m ui_card
```
