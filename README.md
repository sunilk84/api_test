README.md - API Test Framework

# API Test Framework with Pytest & Requests

This is a lightweight and modular API test framework built using **Python**, **Pytest**, and **Requests**. It targets the [https://restful-api.dev](https://restful-api.dev) endpoint and includes automated tests for the `PATCH /objects/{id}` API.

# Folder Structure
api_test_framework/ 
├── tests/ 
│ └── test_patch_scenarios.py # Test cases for PATCH endpoint 
├── utils/ │ └── http_utils.py # Reusable HTTP methods (GET, POST, PUT, PATCH, DELETE) 
├── conftest.py # Shared fixtures for base URL and HTTP client 
├── requirements.txt # Python dependencies 
└── .github/ └── workflows/ └── api-tests.yml # GitHub Actions CI pipeline
---


## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repo)
- Internet connection (to hit the public API)

---

## Setup Instructions

1. **Clone the repository**

bash
git clone https://github.com/your-username/API_Test_Using_Python.git
cd API_Test_Using_Python

2. **Create a virtual environment (optional but recommended)**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
pip install -r requirements.txt

4. **To run all tests:**
pytest -v

5. **To run a specific test file:**
pytest tests/test_patch_object.py

6 **Utility Functions**
The HttpClient class in **utils/http_utils.py** provides reusable methods:
client.get(endpoint)
client.post(endpoint, json=payload)
client.put(endpoint, json=payload)
client.patch(endpoint, json=payload)
client.delete(endpoint)

7. **CI CD Pipeline (GitHub Actions)**
The framework includes a GitHub Actions workflow that: 
- Runs tests on every push or pull request to main
- Installs dependencies 
- Executes all Pytest cases
- Provides feedback in the GitHub UI

.github/workflows/api-tests.yml

name: API Tests using Python

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  run-tests:
    runs-on: windows-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run API tests
      run: |
        pytest --maxfail=1 --disable-warnings -v



Observations
1. Valid PATCH returns updated object with status 200
2. Invalid ID returns 404 or 400
3. Empty payload behavior may vary depending on API design


