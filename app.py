from flask import Flask

app = Flask(__name__)

# INTENTIONAL SECURITY FLAW: Hardcoded database password for Semgrep to catch
DATABASE_PASSWORD = "super_secret_password_123"

@app.route('/')
def hello_world():
    return 'Hello, DevSecOps World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
