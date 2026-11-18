Student Assignment: Banking REST API Using FastAPI
Beginner Level
 Hands-on Development

1. Problem Statement
Develop a simple Banking REST API application using Python and FastAPI.

The application should allow customers to create bank accounts, check account details, deposit money, withdraw money, and transfer money between accounts.

The application should expose REST API endpoints that can be tested using Swagger UI or Postman.

For this assignment, use an in-memory Python data structure (dictionary or list) to store account information. Database integration is not required.
2. Functional Requirements
Students must implement the following functionalities.
Module	Requirement
Create Account	Create a new bank account
View Account	Retrieve account details using account number
View All Accounts	Display all registered bank accounts
Deposit Money	Add money to an account
Withdraw Money	Deduct money from an account
Check Balance	Display the current account balance
Transfer Money	Transfer money between two accounts
Delete Account	Delete an existing bank account

3. API Requirements
Students should develop the following REST API endpoints.
HTTP Method	Endpoint	Description
POST	/accounts	Create a new account
GET	/accounts	Get all accounts
GET	/accounts/{account_id}	Get account details
POST	/accounts/{account_id}/deposit	Deposit money
POST	/accounts/{account_id}/withdraw	Withdraw money
GET	/accounts/{account_id}/balance	Check account balance
POST	/accounts/transfer	Transfer money
DELETE	/accounts/{account_id}	Delete account

4. Account Information Requirements
Each bank account should contain the following information:
- Account ID (Unique)
- Customer Name
- Email Address
- Account Type (Savings / Current)
- Initial Deposit
- Current Balance
- Account Status (Active / Inactive)
5. Business Validation Requirements
Implement the following validations:
1. Account ID must be unique.
2. Customer name cannot be empty.
3. Email address must be valid.
4. Initial deposit must be greater than or equal to zero.
5. Deposit amount must be greater than zero.
6. Withdrawal amount must be greater than zero.
7. Withdrawal should not exceed the available balance.
8. Transfer should not be allowed if the source account has insufficient balance.
9. Source and destination accounts must exist during a transfer.
10. An account should not be transferred to itself.
11. Deleted or inactive accounts should not allow financial transactions.
12. Return meaningful error messages for invalid requests.
6. Technical Requirements
Students must use the following technologies:
Technology	Purpose
Python	Programming language
FastAPI	REST API development
Pydantic	Request validation
Uvicorn	Application server
Pytest	API testing
Swagger UI	API documentation
GitHub Copilot	AI-assisted development

Note: Database integration, authentication, JWT, and frontend development are not required.
7. Testing Requirements
Students must create test cases using Pytest and FastAPI TestClient.

Test the following scenarios:
Test ID	Test Scenario	Expected Result
TC01	Create a valid account	Account created successfully
TC02	Create duplicate account	Validation error
TC03	Get existing account	Account details returned
TC04	Get invalid account	404 error
TC05	Deposit valid amount	Balance increased
TC06	Deposit negative amount	Validation error
TC07	Withdraw valid amount	Balance decreased
TC08	Withdraw more than balance	Insufficient balance error
TC09	Transfer valid amount	Both balances updated
TC10	Transfer to invalid account	Error returned
TC11	Delete existing account	Account deleted successfully
TC12	Deposit into deleted account	Transaction rejected

Students should also test appropriate HTTP status codes, response messages, and account balance calculations.
8. Troubleshooting Requirements
Students should identify and resolve common development issues.
Issue	Expected Troubleshooting
ModuleNotFoundError	Check package installation and virtual environment
Uvicorn command not found	Install Uvicorn in the active environment
404 Not Found	Verify API endpoint and HTTP method
422 Unprocessable Entity	Check request body and Pydantic validation
500 Internal Server Error	Inspect application logs and identify the exception
Incorrect balance	Verify deposit, withdrawal, and transfer calculations
Test failures	Analyze assertion errors and fix implementation
Import errors	Verify module names and project structure

Students must maintain a record of at least five troubleshooting scenarios, including the issue, root cause, solution, and verification.
9. README.md Requirements
Create a README.md file containing the following sections:
1. Project Title
2. Project Overview
3. Features
4. Technologies Used
5. Project Structure
6. Installation Instructions
7. Virtual Environment Setup
8. Dependency Installation
9. Application Execution Steps
10. API Endpoint Details
11. Swagger UI Access Instructions
12. Sample API Requests and Responses
13. Testing Instructions
14. Troubleshooting Guide
10. Python Docstring Requirements
Students must add meaningful docstrings to all functions.

Each docstring should explain:
- Purpose of the function.
- Function arguments.
- Return value.
- Exceptions raised, wherever applicable.
Example requirement:
def deposit_money(account_id: int, amount: float):    """Deposit money into a customer's bank account.    Args:        account_id: Unique identifier of the bank account.        amount: Amount to be deposited.    Returns:        Updated bank account details.    Raises:        HTTPException: If the account does not exist            or the deposit amount is invalid.    """



Students should use GitHub Copilot to generate and review docstrings.
11. Suggested Project Structure
Students should organize their project with the following structure:
banking-rest-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── banking_service.py
│
├── tests/
│   ├── __init__.py
│   └── test_banking.py
│
├── README.md
├── requirements.txt
└── .gitignore


12. GitHub Copilot Usage Requirements
Students must use GitHub Copilot during development.

They should use Copilot for the following activities:
Activity	Expected Work
Code Generation	Generate FastAPI endpoints
Model Creation	Generate Pydantic models
Business Logic	Implement deposit, withdrawal, and transfer
Testing	Generate Pytest test cases
Troubleshooting	Analyze and resolve errors
Documentation	Generate README.md
Docstrings	Generate function docstrings

Important: Students should understand every generated code block. They must review, execute, test, and modify the generated code rather than blindly accepting Copilot suggestions.