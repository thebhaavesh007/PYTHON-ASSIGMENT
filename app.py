from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data
users = [
    {"id": 1, "first_name": "John", "last_name": "Doe"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith"},
    # Add more user data
]

@app.route('/api/users', methods=['GET'])
def get_users():
    first_name = request.args.get('first_name')
    if not first_name:
        return jsonify({"error": "Missing 'first_name' parameter"}), 400

    matching_users = [user for user in users if user["first_name"] == first_name]
    return jsonify(matching_users)

if __name__ == '__main__':
    app.run(debug=True)
