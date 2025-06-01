
from flask import Flask, render_template, request, jsonify
import game.main as game_main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wizard')
def wizard():
    return render_template('wizard.html')

@app.route('/api/command', methods=['POST'])
def handle_command():
    user_input = request.json.get('command', '')
    response = game_main.process_command(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
