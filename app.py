from flask import Flask, request, render_template, jsonify
import pyotp
from flask_cors import CORS
CORS(app)
app = Flask(__name__)

# Generate a new random secret key
# The secret key should be shared between the user and the server
secret_key = pyotp.random_base32()

@app.route('/generate/', methods=['POST'])
def generate_otp():
    # Generate a new OTP for the current time
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()

    # Return the OTP to the client as a JSON object
    response = jsonify({'otp': otp})
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route('/')
def gen():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
