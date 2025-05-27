# 🔧 Port Araçları - Tarayıcı | Dinleyici | Bağlantı Testi

Bu uygulama, ağ üzerinde temel bağlantı testleri ve port analizleri yapmak amacıyla geliştirilmiş bir **Tkinter GUI** tabanlı Python programıdır. Program; port taraması, TCP dinleyici ve bağlantı testi gibi 3 ana işlevi bir arada sunar.

## 🚀 Özellikler

- 🔍 **Port Tarayıcı:** Belirtilen IP adresi ve port aralığında tarama yaparak açık portları listeler.
- 📡 **TCP Dinleyici:** Belirtilen port üzerinden gelen TCP bağlantılarını dinler ve loglar.
- 🔗 **Bağlantı Testi:** IP ve port kombinasyonuna anlık bağlantı testi gerçekleştirir.
- 📝 **Loglama:** Tüm işlemler ekran loglarına ve dinleyici özelinde `logs/listener_log.txt` dosyasına kaydedilir.
- 🧵 **Çoklu İş Parçacığı (Threading):** İşlemler arka planda çalışır, arayüz donmaz.

## 🖥️ Ekran Görüntüsü

> (Buraya ekran görüntüsü ekleyebilirsin)

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

```bash
git clone https://github.com/kullanici-adin/port-araclari.git
cd port-araclari
python port_araclari.py
(İsteğe bağlı: .exe derlemek istersen aşağıdaki gibi pyinstaller kullanabilirsin)
pip install pyinstaller
pyinstaller --noconsole --onefile --icon=icon.ico port_araclari.py
📁 Dosya Yapısı
port-araclari/
├── port_araclari.py        # Ana Python dosyası
├── icon.ico                # (İsteğe bağlı) Arayüz ikonu
├── logs/
│   └── listener_log.txt    # TCP dinleyici logları
└── README.md               # Bu belge
📜 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
________________________________________
✨ Katkıda Bulun
Pull request’lere ve önerilere her zaman açığım. İletişim kurmak veya katkıda bulunmak istersen çekinmeden yaz!

---
