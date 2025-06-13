import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Path relatif
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data/processed")
model_dir = os.path.join(base_dir, "models")
os.makedirs(model_dir, exist_ok=True)

# Load data
train_df = pd.read_csv(os.path.join(data_dir, "clean_train.csv"))
test_df = pd.read_csv(os.path.join(data_dir, "clean_test.csv"))

# Strip whitespace from column names
train_df.columns = train_df.columns.str.strip()
test_df.columns = test_df.columns.str.strip()

X_train = train_df['Sentence']
y_train = train_df['Emoji']

X_test = test_df['Sentence']
y_test = test_df['Emoji']

# Pipeline: TF-IDF + Classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluasi
y_pred = pipeline.predict(X_test)
print("=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

# Simpan pipeline
joblib.dump(pipeline.named_steps['tfidf'], os.path.join(model_dir, "tfidf.pkl"))
joblib.dump(pipeline.named_steps['clf'], os.path.join(model_dir, "classifier.pkl"))
print("✅ Model dan TF-IDF vectorizer disimpan di folder models/")