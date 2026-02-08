import joblib

# Kaydettiğin dosyayı geri çağır
yuklenen_model = joblib.load('iris_model.joblib')

# Artık bu modelle direkt tahmin yapabilirsin
tahmin = yuklenen_model.predict([[5.1, 3.5, 1.4, 0.2]])
print(f"Tahmin Edilen Çiçek Türü: {tahmin}")