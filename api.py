from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as stop_words

app = Flask(__name__)

# load trained model and label encoder
model = joblib.load('cefr_level_predictor.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# vectorizer
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# clean input data
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # assuming the JSON data is in the format: {"text": "Your text here"}
    text = data['text']
    # clean and vectorize the text input
    text = clean_text(text)
    text_vectorized = vectorizer.transform([text])
    
    # predict with the model
    prediction = model.predict(text_vectorized)
    # decode the numerical prediction back to the original label
    decoded_prediction = label_encoder.inverse_transform(prediction)
    
    # return prediction as a JSON response
    return jsonify({'cefr_level': decoded_prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)