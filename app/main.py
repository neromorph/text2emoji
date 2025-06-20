from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model & vectorizer
base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, "..", "models")
tfidf_path = os.path.join("models", "tfidf.pkl")
clf_path = os.path.join("models", "classifier.pkl")

tfidf = joblib.load(tfidf_path)
model = joblib.load(clf_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sentence = data.get('sentence')

    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400

    # Preprocessing minimal
    sentence_clean = sentence.lower()

    # Vectorize
    X = tfidf.transform([sentence_clean])

    # Predict
    emoji = model.predict(X)[0]

    return jsonify({
        "input": sentence,
        "emoji": emoji
    })

@app.route('/health', methods=['GET'])
def home():
    return "Text-to-Emoji Prediction API is running!"

if __name__ == '__main__':
    app.run(debug=True)
