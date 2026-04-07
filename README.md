# 🎓 Alumni Tracking System (Daily Project 3)

## 📌 Deskripsi

Alumni Tracking System merupakan aplikasi berbasis web yang dikembangkan untuk membantu pencarian data alumni secara efisien.
Sistem ini memungkinkan pengguna melakukan pencarian alumni berdasarkan beberapa parameter seperti nama, NIM, tahun masuk, tanggal lulus, fakultas, dan program studi.

Proyek ini dibuat sebagai bagian dari **Daily Project 3** pada mata kuliah Rekayasa Kebutuhan.

---

## 🎯 Tujuan

* Mengimplementasikan sistem berbasis web dari hasil perancangan sebelumnya
* Menyediakan fitur pencarian data alumni
* Membangun sistem dengan arsitektur sederhana menggunakan Flask

---

## ⚙️ Teknologi yang Digunakan

* Python (Flask)
* HTML, CSS (Bootstrap)
* SQLite (Database)

---

## ✨ Fitur Utama

* 🔍 Pencarian alumni berdasarkan:

  * Nama Lulusan
  * NIM
  * Tahun Masuk
  * Tanggal Lulus
  * Fakultas
  * Program Studi
* 📊 Menampilkan hasil pencarian dalam bentuk tabel
* 💻 Antarmuka web sederhana dan responsif

---

## 📁 Struktur Project

```
alumni-tracking-system/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
```

---

## ▶️ Cara Menjalankan Project

### 1. Clone Repository

```
git clone https://github.com/username/alumni-tracking-system.git
cd alumni-tracking-system
```

### 2. Install Dependency

```
pip install -r requirements.txt
```

atau (Mac):

```
pip3 install -r requirements.txt
```

### 3. Jalankan Aplikasi

```
python app.py
```

atau:

```
python3 app.py
```

### 4. Buka di Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Pengujian Sistem

| No | Fitur               | Skenario               | Hasil yang Diharapkan        | Hasil Aktual | Status |
| -- | ------------------- | ---------------------- | ---------------------------- | ------------ | ------ |
| 1  | Akses Halaman Utama | Membuka URL aplikasi   | Halaman tampil               | Berhasil     | ✅      |
| 2  | Input Nama          | Mengisi nama alumni    | Data sesuai ditampilkan      | Berhasil     | ✅      |
| 3  | Input NIM           | Mengisi NIM            | Data sesuai ditampilkan      | Berhasil     | ✅      |
| 4  | Multi Filter        | Mengisi beberapa field | Data terfilter               | Berhasil     | ✅      |
| 5  | Data Kosong         | Tidak ada hasil        | Muncul pesan tidak ditemukan | Berhasil     | ✅      |

---

## ⚠️ Catatan

* Pada tahap **Daily Project 3**, sistem hanya berfokus pada fitur pencarian
* Data alumni belum diintegrasikan (akan dilakukan pada Daily Project 4 menggunakan file Excel)

---

## 🚀 Pengembangan Selanjutnya

* Import data alumni dari Excel
* Upload file Excel melalui web
* Dashboard statistik alumni
* Fitur autentikasi pengguna

---

## 👨‍💻 Developer

**Aldi Saputra**
NIM: 202110370311044

---
