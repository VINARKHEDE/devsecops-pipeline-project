import os
from flask import Flask

app = Flask(__name__)

# SECURE: Read database password from environment variable instead of hardcoding
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "default_safe_value")

@app.route('/')
def hello_world():
    return 'Hello, DevSecOps World! The application is secure.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
