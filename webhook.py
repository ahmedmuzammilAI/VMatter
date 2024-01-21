from flask import Flask, request, jsonify, render_template
from pyngrok import ngrok

app = Flask(__name__)

latest_hits = []

@app.route('/webhook/<message>', methods=['GET'])
def webhook(message):
    latest_hits.append(message)
    # public_url = ngrok.connect(5000).public_url
    # latest_hits.append(public_url)

    return f"Received message: {message}"

@app.route('/latest_hits', methods=['GET'])
def show_latest_hits():
    return render_template('latest_hits.html', hits=latest_hits)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
    
