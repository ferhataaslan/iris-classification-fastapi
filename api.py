from fastapi import FastAPI
import joblib
import numpy as np

# 1. Uygulamayı ve Modeli Başlat
app = FastAPI(title="Iris Çiçek Tahmin API'si")
model = joblib.load("iris_model.joblib")

# Çiçek isimlerini hatırlayalım
labels = ['Setosa', 'Versicolor', 'Virginica']


@app.get("/")
def ana_sayfa():
    return {"mesaj": "Iris Tahmin API'sine hoş geldin! Tahmin için /docs adresine git."}


@app.get("/predict")
def tahmin_et(sepal_l: float, sepal_w: float, petal_l: float, petal_w: float):
    # Kullanıcıdan gelen verileri modelin anlayacağı formata (liste içinde liste) sokuyoruz
    yeni_veri = np.array([[sepal_l, sepal_w, petal_l, petal_w]])

    # Tahmin yap
    tahmin_indeksi = model.predict(yeni_veri)[0]
    sonuc = labels[tahmin_indeksi]

    return {
        "tahmin_edilen_tur": sonuc,
        "girdi_verileri": {
            "sepal_length": sepal_l,
            "sepal_width": sepal_w,
            "petal_length": petal_l,
            "petal_width": petal_w
        }
    }