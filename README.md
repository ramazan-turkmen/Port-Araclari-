# 🔧 Port Araçları - Tarayıcı | Dinleyici | Bağlantı Testi

Bu uygulama, ağ üzerinde temel bağlantı testleri ve port analizleri yapmak amacıyla geliştirilmiş bir **Tkinter GUI** tabanlı Python programıdır. Program; port taraması, TCP dinleyici ve bağlantı testi gibi 3 ana işlevi bir arada sunar.

## 🚀 Özellikler

- 🔍 **Port Tarayıcı:** Belirtilen IP adresi ve port aralığında tarama yaparak açık portları listeler.
- 📡 **TCP Dinleyici:** Belirtilen port üzerinden gelen TCP bağlantılarını dinler ve loglar.
- 🔗 **Bağlantı Testi:** IP ve port kombinasyonuna anlık bağlantı testi gerçekleştirir.
- 📝 **Loglama:** Tüm işlemler ekran loglarına ve dinleyici özelinde `logs/listener_log.txt` dosyasına kaydedilir.
- 🧵 **Çoklu İş Parçacığı (Threading):** İşlemler arka planda çalışır, arayüz donmaz.

## 🖥️ Ekran Görüntüsü

![1](https://github.com/user-attachments/assets/d045c715-de78-4d07-a5c9-8390d7897b0f)


## 🔧 Gereksinimler

- Python 3.7 veya üzeri

Ek kütüphane yoktur, sadece standart kütüphaneler kullanılmıştır:
- `socket`
- `threading`
- `queue`
- `datetime`
- `tkinter`
- `os`

## ⚙️ Kurulum

https://github.com/ramazan-turkmen

📁 Dosya Yapısı
port-araclari/

├── port_araclari.py        # Ana Python dosyası

├── icon.ico                # (İsteğe bağlı) Arayüz ikonu

├── logs/

│   └── listener_log.txt    # TCP dinleyici logları

└── README.md               # Bu belge

________________________________________
✨ Katkıda Bulun
Pull request’lere ve önerilere her zaman açığım. İletişim kurmak veya katkıda bulunmak istersen çekinmeden yaz!

---
