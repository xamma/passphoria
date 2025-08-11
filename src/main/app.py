from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/passphrase', methods=['POST'])
def post_passphrase():
    return jsonify({
        'passphrase': 'example-passphrase'})