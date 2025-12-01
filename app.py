from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>VIP Daily Web App</h1><p>Render deployment successful.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)