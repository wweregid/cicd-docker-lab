from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv('APP_VERSION', '1.0.0')
    return f'''
    <h1>Hello from Docker!</h1>
    <p>Version: {version}</p>
    <p>CI/CD Lab with GitHub Actions</p>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
