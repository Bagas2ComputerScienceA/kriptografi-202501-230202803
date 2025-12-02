# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Bagas Enggar Prasetyo]  
NIM: [230202803]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
---

Diffie–Hellman adalah sebuah protokol pertukaran kunci yang memungkinkan dua pihak menciptakan sebuah kunci rahasia bersama tanpa perlu mengirimkan kunci tersebut secara langsung melalui jaringan. Protokol ini bekerja dengan memanfaatkan kesulitan Discrete Logarithm Problem, yaitu masalah matematika yang sangat sulit dipecahkan ketika bilangan yang digunakan berukuran besar. Mekanismenya dimulai ketika kedua pihak menyepakati dua nilai publik, yaitu sebuah bilangan prima besar p dan sebuah generator g. Setelah itu, masing-masing pihak memilih sebuah nilai rahasia pribadi: Alice memilih a dan Bob memilih b. Alice kemudian menghitung nilai publiknya A = g^a mod p, sementara Bob menghitung B = g^b mod p. Kedua nilai publik ini kemudian ditukar melalui jaringan.

Setelah menerima nilai publik lawan, masing-masing pihak menghitung kunci rahasia bersama menggunakan nilai rahasia sendiri dan nilai publik yang diterima. Alice menghitung K = B^a mod p, dan Bob menghitung K = A^b mod p. Secara matematis, keduanya akan menghasilkan nilai yang sama, yaitu K = g^(ab) mod p. Nilai inilah yang menjadi shared secret key yang hanya diketahui oleh Alice dan Bob, meskipun nilai-nilai publik seperti g, p, A, dan B dapat dilihat oleh siapa saja. Penyerang tidak dapat mengetahui K tanpa mengetahui nilai rahasia a atau b, dan untuk menebaknya mereka harus memecahkan discrete logarithm, yang sangat sulit secara komputasional. Dengan mekanisme ini, Diffie–Hellman menjadi salah satu teknik dasar paling penting dalam keamanan modern, terutama dalam pembuatan kunci enkripsi simetris pada komunikasi yang aman.


---

## 3. Alat dan Bahan
- Python 3.12 
- Visual Studio Code 
- Git dan akun GitHub 

---

## 4. Langkah Percobaan
1. Membuat file `diffie_hellman.py` di folder `praktikum/week7-diffie-hellman/src/diffie_hellman.py`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python diffie_hellman.py`.
4. Menganalisis Serangan MITM (Man-in-the-Middle)

---

## 5. Source Code


```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B).
```

---

## 6. Hasil dan Pembahasan

Hasil eksekusi program diffie-hellman menunjukkan bahwa nilai ```shared_secret_A``` dan ```shared_secret_B``` sama. 

![Hasil Eksekusi](screenshots/hasil_sebelum_MITM.png)

Hasil Eksekusi Analisa MITM

![Hasil Eksekusi](screenshots/hasil_saat_diuji_MITM.png)



---

## 7. Jawaban Pertanyaan
Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Diffie-Hellman memungkinkan pertukaran kunci melalui saluran publik karena protokol ini tidak pernah mengirimkan kunci rahasia secara langsung. Yang dikirim hanyalah nilai publik yang dihasilkan dari operasi eksponensiasi modulo bilangan prima besar, sehingga meskipun dilihat oleh siapa pun, nilai tersebut tidak dapat digunakan untuk menurunkan nilai rahasia. Keamanan protokol bergantung pada kesulitan Discrete Logarithm Problem, sehingga pihak luar tidak bisa dengan mudah menebak nilai eksponen rahasia yang digunakan dua pihak untuk menghasilkan kunci bersama.
- Pertanyaan 2: Kelemahan utama protokol Diffie-Hellman murni adalah bahwa protokol ini tidak menyediakan autentikasi. Artinya, dua pihak yang bertukar nilai publik tidak dapat memastikan apakah mereka benar-benar berkomunikasi dengan pihak yang dimaksud. Hal ini membuka peluang terjadinya serangan Man-in-the-Middle (MITM), dimana penyerang dapat menyisipkan diri di antara dua pihak, membuat dua kunci terpisah, dan meneruskan pesan dengan seolah-olah mereka adalah pihak asli. 
- Pertanyaan 3: Serangan MITM pada Diffie-Hellman dapat dicegah dengan menambahkan mekanisme autentikasi. Cara yang paling umum adalah memadukan Diffie-Hellman dengan sertifikat digital atau tanda tangan digital yang dikeluarkan oleh otoritas tepercaya. Dengan autentikasi tersebut, setiap pihak dapat memverifikasi bahwa nilai publik yang diterima benar-benar milik pihak lawan yang sah. Selain itu, protokol modern seperti TLS menggunakan varian Authenticated Diffie-Hellman untuk memastikan integritas dan keaslian nilai yang dipertukarkan, sehingga penyerang tidak dapat menyamar atau menyisipkan diri dalam proses pertukaran kunci.

---

## 8. Kesimpulan
Diffie-Hellman adalah protokol yang sangat penting dalam keamanan modern karena memungkinkan dua pihak menghasilkan kunci rahasia bersama meskipun menggunakan saluran komunikasi yang terbuka. Keamanannya bergantung pada kesulitan memecahkan Discrete Logarithm Problem, sehingga nilai publik yang ditukar tidak dapat digunakan untuk menebus kunci rahasia. Namun, protokol Diffie-Hellman murni memiliki kelemahan serius karena tidak menyediakan autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle. Untuk mengatasi kelemahan tersebut, mekanisme autentikasi seperti sertifikat digital atau tanda tangan digital perlu ditambahkan agar identitas kedua pihak dapat dipastikan dan proses pertukaran kunci berlangsung aman.

---

## 9. Daftar Pustaka


---

## 10. Commit Log

```
commit week7-diffie-hellman
Author: Bagas Enggar Prasetyo <bagasenggarp42@gmail.com>
Date:   2025-12-02

    week7-diffie-hellman: Key Exchange
```
