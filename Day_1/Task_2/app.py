from flask import Flask, jsonify, render_template
import random
app = Flask(__name__)


quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different.",
    "Java is to JavaScript what car is to Carpet."
]

@app.route('/api/quote')
def get_quote():
    return jsonify({"Quote" : random.choice(quotes)}), 200

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)