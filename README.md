# Iris Flower Classification API





##### Bu proje, makine öğrenmesi dünyasının klasiklerinden olan Iris veri seti kullanılarak eğitilmiş bir modelin, modern web teknolojileri ile canlıya alınmış bir örneğidir. Proje kapsamında model eğitimi, API geliştirme ve bulut tabanlı dağıtım (deployment) süreçleri uçtan uca uygulanmıştır.

###### 

## 🚀 Kullanılan Teknolojiler



###### Machine Learning: Scikit-learn (Random Forest Classifier)

###### 

###### Backend: FastAPI (Python)

###### 

###### Deployment \& Containerization: Docker \& Hugging Face Spaces

###### 

###### Model Management: Joblib



###### 

## 🛠️ Proje Özellikleri



###### Model Eğitimi: Iris çiçeklerinin yaprak özelliklerine (sepal/petal length/width) göre 3 farklı türü sınıflandırabilen bir model eğitildi.

###### 

###### FastAPI Entegrasyonu: Eğitilen model, asenkron yapıda çalışan yüksek performanslı bir FastAPI sunucusuna bağlandı.

###### 

###### Dockerization: Uygulama, platform bağımsız çalışabilmesi için Dockerfile ile konteyner haline getirildi.

###### 

###### Canlı Uygulama: Proje, Hugging Face Spaces üzerinde Docker altyapısı kullanılarak başarıyla yayına alındı.

###### 



## 📝 Nasıl Çalıştırılır?



###### Bu projeyi yerel bilgisayarınızda çalıştırmak için:

###### 

###### Depoyu klonlayın: git clone https://github.com/ferhataaslan/iris-classification-fastapi.git

###### 

###### Gerekli kütüphaneleri yükleyin: pip install -r requirements.txt

###### 

###### Uygulamayı başlatın: uvicorn api:app --reload

###### 

###### Tarayıcınızdan http://127.0.0.1:8000/docs adresine giderek etkileşimli API dokümantasyonuna ulaşabilirsiniz.

