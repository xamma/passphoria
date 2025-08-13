from flask import Flask, render_template, jsonify, request
from models import PassphraseRequest
import diceware

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/passphrase', methods=['POST'])
def post_passphrase():
    if request.method != 'POST':
        return jsonify({'error': 'Method not allowed'}), 405
    
    data = request.get_json(silent=True) or {}
    req = PassphraseRequest(**data)

    options = diceware.handle_options(args=[])

    options.num = req.num
    options.delimiter = req.delimiter
    options.specials = req.specials
    options.caps = req.caps

    passphrase = diceware.get_passphrase(options=options)

    return jsonify({'passphrase': passphrase}), 200
