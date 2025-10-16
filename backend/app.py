from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

app = Flask(__name__)
CORS(app)

# Load model dan TF-IDF Vectorizer
model = pickle.load(open('model_logreg.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Inisialisasi StopWordRemover dan Stemmer
factory_stopwords = StopWordRemoverFactory()
stopwords = factory_stopwords.get_stop_words()
factory_stem = StemmerFactory()
stemmer = factory_stem.create_stemmer()

# Fungsi clean_text (sama seperti sebelumnya)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  
    text = ' '.join([word for word in text.split() if word not in stopwords])
    text = stemmer.stem(text)
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    judul = data['judul']
    narasi = data['narasi']

    # Gabungkan judul dan narasi
    text = judul + " " + narasi

    # Pra-proses teks
    cleaned_text = clean_text(text)
    text_tfidf = tfidf_vectorizer.transform([cleaned_text])  

    # Prediksi
    prediction = model.predict(text_tfidf)[0]  
    # Tentukan hasil prediksi
    if prediction == 0:
        result = "Not Hoax"
    else:
        result = "Hoax"

    # Kembalikan hasil prediksi sebagai JSON
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
