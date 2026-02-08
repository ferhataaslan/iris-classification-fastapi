import requests

# Hugging Face'deki API linkini buraya yapıştır (sonunda /predict olmalı)
url = "https://ferhataslan-iris-tahmin-projesi.hf.space/predict"

# Test verilerimiz (Hani o konuştuğumuz yaprak boyutları)
veri = {
    "sepal_l": 5.1,
    "sepal_w": 3.5,
    "petal_l": 1.4,
    "petal_w": 0.2
}

# API'ye isteği gönder (GET yöntemiyle)
response = requests.get(url, params=veri)

if response.status_code == 200:
    print("API Cevabı:", response.json()["tahmin_edilen_tur"])
else:
    print("Bir hata oluştu!", response.status_code)