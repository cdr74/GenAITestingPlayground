# This program runs a simple server that can be connected to by a client.
# I should provide 2 api end points for the client to connect to.
# 1. /api/v1/submit
# 2. /api/v1/results
# submit should contain a json payload with the following fields:
# 1. name
# 2. email
# 3. phone
# 4. address
# 5. dob
# results should return Hello name, your email is email, your phone is phone, your address is address, your dob is dob

import os

from flask import Flask, jsonify, request

app = Flask(__name__)

user_info = {}


@app.route("/api/v1/submit", methods=["POST"])
def submit_info():
    global user_info
    user_info = request.get_json()
    return jsonify({"message": "Information submitted"}), 201


@app.route("/api/v1/results", methods=["GET"])
def get_results():
    global user_info
    message = f"Hello {user_info.get('name')}, your email is {user_info.get('email')}, your phone is {user_info.get('phone')}, your address is {user_info.get('address')}, your dob is {user_info.get('dob')}"
    return jsonify({"message": message})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)


# ### User
# create some curl commands I can use to test the apis
#
# ### Copilot
#
# Sure, here are some curl commands you can use to test the APIs:
#
# To submit information, use the following command:
#
# ```bash
# curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","email":"johndoe@example.com","phone":"123-456-7890","address":"123 Main St, Anytown, USA","dob":"01-01-2000"}' http://localhost:5000/api/v1/submit
# ```
#
# To get the results, use the following command:
#
# ```bash
# curl -X GET http://localhost:5000/api/v1/results
# ```


### User
# provide a JSON data template

### Copilot

# Sure, here's a JSON data template that matches the fields expected by the Python program:
# ```json
# {
#     "name": "John Doe",
#     "email": "johndoe@example.com",
#     "phone": "123-456-7890",
#     "address": "123 Main St, Anytown, USA",
#     "dob": "01-01-2000"
# }
