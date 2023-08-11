# PYTHON-ASSIGMENT
Welcome to the User Restful API
This repository contains the implementation of a RESTful API for managing user information. The API is built using Flask, a Python web framework, and utilizes SQLite as the database for storing user records.

Features
Search for users based on the beginning of their first name.
If no local matches are found, the API fetches users from an external API and returns them.
Getting Started
Clone the repository to your local machine using git clone.
Install the required dependencies using pip install -r requirements.txt.
Run the Flask app using python app.py.
Access the API endpoints using tools like Postman or your web browser.
API Endpoints
GET /api/users/search: Search for users with the beginning of their first name matching the provided parameter.
Example: /api/users/search?first_name=John
Contributing
Contributions are welcome! If you have ideas for improvements or find any issues, feel free to open an issue or create a pull request.
