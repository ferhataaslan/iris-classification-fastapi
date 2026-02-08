import pandas as pd
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# 1. Veri setini yükleyelim
iris = load_iris()
X = iris.data  # Özellikler (Yaprak boyutları)
y = iris.target # Hedef (Çiçek türü)

# 2. Veriyi Eğitim ve Test olarak ikiye bölelim (%80 Eğitim, %20 Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Modelimizi seçelim ve eğitelim (Random Forest - Rastgele Orman)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 4. Tahmin yapalım
y_pred = model.predict(X_test)

# Karmaşıklık matrisini oluştur
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)

# 5. Sonuçları değerlendirelim
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: %{accuracy * 100:.2f}")
print("\nSınıflandırma Raporu:\n", classification_report(y_test, y_pred, target_names=iris.target_names))


# Çizdir
disp.plot(cmap=plt.cm.Blues)
plt.title("Modelin Tahmin Başarısı")
plt.show()



# Modeli "iris_model.joblib" adıyla klasöre kaydeder
joblib.dump(model, 'iris_model.joblib')
print("Model başarıyla kaydedildi!")