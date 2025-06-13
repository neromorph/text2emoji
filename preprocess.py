import pandas as pd
import re
import os

# Ambil direktori file ini (bukan lokasi run terminal)
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data/")
output_dir = os.path.join(data_dir, "processed")

# Fungsi cleaning teks
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

original = pd.read_csv(os.path.join(data_dir, "train.csv"), skipinitialspace=True)
extra = pd.read_csv(os.path.join(data_dir, "extra_data.csv"), skipinitialspace=True)

train_df = pd.concat([original, extra], ignore_index=True)
train_df.to_csv(os.path.join(data_dir, "train.csv"), index=False)
# Load file
# train_df = pd.read_csv(os.path.join(data_dir, "train.csv"), skipinitialspace=True)
test_df = pd.read_csv(os.path.join(data_dir, "test.csv"), skipinitialspace=True)

# Ambil hanya emoji pertama (gunakan setelah load)
train_df['Emoji'] = train_df['Emoji'].astype(str).apply(lambda x: x.strip()[0])
test_df['Emoji'] = test_df['Emoji'].astype(str).apply(lambda x: x.strip()[0])

# Remove all whitespace from column names
train_df.columns = train_df.columns.str.replace(r"\s+", "", regex=True)
test_df.columns = test_df.columns.str.replace(r"\s+", "", regex=True)

# Bersihkan teks
train_df['Sentence'] = train_df['Sentence'].astype(str).apply(clean_text)
test_df['Sentence'] = test_df['Sentence'].astype(str).apply(clean_text)

# Buat direktori jika belum ada
os.makedirs(output_dir, exist_ok=True)

# Simpan hasil
train_df.to_csv(os.path.join(output_dir, "clean_train.csv"), index=False)
test_df.to_csv(os.path.join(output_dir, "clean_test.csv"), index=False)

print("✅ Preprocessing selesai. File tersimpan di data/processed/")