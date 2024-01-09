from flask import Flask, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    return username == 'user' and password == 'password'

@app.route('/multiply', methods=['POST'])
@auth.login_required
def multiply_numbers():
    data = request.get_json()
    if 'numbers' in data:
        result = 1
        for num in data['numbers']:
            result *= num
        return {'result': result}
    else:
        return {'error': 'Invalid input'}, 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)