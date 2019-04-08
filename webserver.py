from flask import Flask, request, render_template, jsonify
from lib.text_to_speech import reload_voice_files

app = Flask(__name__


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/herbs')
def herbs():
    return render_template('herbs.html')


@app.route('/pin-voices')
def pinVoices():
    return render_template('pin-voices.html')


@app.route('/update-pins', methods=['POST'])
def updatePins():
    req_data = request.get_json()
    print(req_data)
    # Restart audios
    reload_voice_files(req_data)
    return jsonify({"error": False, "data": req_data})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
