# Simpan kode ini sebagai '01_explore_data.py' atau di Jupyter Notebook
import pandas as pd

# Baca dataset
df = pd.read_csv('/Users/macos/Study_burhanudin_2025/Data Science/churn-prediction-google/dataset/customer_subscription_churn_usage_patterns.csv')

# Lihat informasi umum
print("===== SHAPE DATASET =====")
print(f"Jumlah baris: {df.shape[0]}")
print(f"Jumlah kolom: {df.shape[1]}")
print("\n")

print("===== 5 BARIS PERTAMA =====")
print(df.head())
print("\n")

print("===== INFO DATASET =====")
print(df.info())
print("\n")

print("===== STATISTIK DESKRIPTIF =====")
print(df.describe())
print("\n")

print("===== CEK MISSING VALUES =====")
print(df.isnull().sum())