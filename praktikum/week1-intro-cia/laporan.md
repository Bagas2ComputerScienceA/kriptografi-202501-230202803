# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: [intro-cia]
Nama: [Bagas Enggar Prasetyo]  
NIM: [230202803]  
Kelas: [5IKRB]  

---

## Tujuan
1. Membuat ringkasan tentang sejarah kriptografi dari masa klasik, modern, dan kontemporer
2. Menjelaskan prinsip-prinsip dari CIA
3. Menjawab Quiz singkat

---

## Langkah 1 — Ringkasan Sejarah Kriptografi
kriptografi adalah ilmu dan seni untuk menjaga keamanan informasi dengan cara menyamarkan pesan (plaintext) menjadi bentuk yang tidak dapat dibaca (ciphertext), sehingga hanya pihak yang memiliki kunci tertentu yang dapat membacanya kembali. Dalam perkembangannya, kriptografi telah melewati tiga era besar, yaitu: klasik, modern dan kontemporer.

1. Era Kriptografi Klasik
Pada era ini penggunaan kriptografi digunakan untuk menyembunyikan pesan. Kriptografi masih sederhana dan dilakukan secara manual dengan teknik substitusi dan transposisi huruf. Contohnya adalah Caesar Cipher yaitu dengan menggeser huruf dalam alfabet sejumlah posisi tertentu. Misalnya, A diganti dengan D (geser 3 huruf). Selanjutnya adalah, Cipher Vigenère yaitu dengan menggunakan kata kunci untuk melakukan penggeseran huruf secara bergantian, menjadikannya lebih sulit dipecahkan daripada Caesar Cipher.

2. Era Kriptografi Modern
Perkembangan komputer dan teori matematika menjadikan kriptografi lebih ilmiah dan sistematis. Fokusnya berpindah dari teknik substitusi huruf menjadi algoritma matematis yang kuat. Pada tahun 1976, Whitfield Diffie dan Martin Hellman memperkenalkan konsep kriptografi kunci publik (public-key cryptography), yang menjadi fondasi utama kriptografi modern. Salah satu algoritma paling terkenal adalah RSA (Rivest-Shamir-Adleman) Munculnya kriptografi kunci publik (asymmetric encryption), yang memungkinkan dua pihak berkomunikasi aman tanpa harus berbagi kunci rahasia sebelumnya. Selain itu ada pula, AES (Advanced Encryption Standard) dikembangkan sebagai algoritma enkripsi simetris yang sangat aman dan efisien, banyak digunakan dalam komunikasi digital seperti jaringan internet, email, dan penyimpanan data.

3. Era Kriptografi Kontemporer
Kebutuhan keamanan digital meningkat pesat seiring munculnya internet, e-commerce, dan blockchain. Kriptografi kini menjadi bagian integral dari sistem keamanan global. Dalam konteks ini, kriptografi tidak hanya digunakan untuk menjaga kerahasiaan, tetapi juga untuk menjamin integritas, keaslian, dan transparansi transaksi. Teknologi seperti blockchain menggunakan kriptografi untuk memverifikasi transaksi secara transparan dan aman. Cryptocurrency menggunakan prinsip ini untuk membangun jaringan keuangan digital yang tidak bergantung pada otoritas pusat.

---

## Langkah 2 — Prinsip CIA
1. Confidentiality (Kerahasiaan)
Prinsip Confidentiality atau kerahasiaan adalah dasar pertama dalam keamanan informasi yang bertujuan untuk menjaga agar informasi hanya dapat diakses oleh pihak yang berwenang. Prinsip ini mencegah terjadinya kebocoran atau penyalahgunaan data yang bisa menimbulkan kerugian, baik bagi individu maupun organisasi. Dalam kehidupan sehari-hari, penerapan prinsip kerahasiaan dapat kita temukan dalam berbagai bentuk. Misalnya, seseorang menggunakan kata sandi (password) yang kuat dan tidak membagikannya kepada siapa pun untuk melindungi akun media sosial atau perbankan online. Aplikasi pesan seperti WhatsApp dan Signal juga menerapkan enkripsi end-to-end, yang memastikan pesan hanya dapat dibaca oleh pengirim dan penerima. Dengan demikian, Confidentiality memastikan bahwa informasi tetap bersifat pribadi dan hanya dapat digunakan sesuai otoritas yang ditetapkan.

2. Integrity (Integritas)
Prinsip Integrity atau integritas berkaitan dengan upaya menjaga keaslian, keutuhan, dan konsistensi data agar tidak diubah, dimodifikasi, atau dirusak tanpa izin. Prinsip ini menjamin bahwa data tetap dapat dipercaya sebagai dasar pengambilan keputusan, baik oleh individu maupun organisasi. Dalam kehidupan sehari-hari, integritas data diterapkan misalnya saat seseorang mengirim file melalui email, di mana sistem menggunakan hash function seperti SHA-256 untuk memastikan file tidak mengalami perubahan. Di dunia bisnis, transaksi keuangan online menggunakan tanda tangan digital (digital signature) untuk memastikan bahwa data pembayaran tidak dimodifikasi oleh pihak ketiga. Dalam konteks akademik, menjaga integritas berarti memastikan dokumen seperti laporan penelitian atau tugas kuliah tidak diubah tanpa sepengetahuan penulis. Penerapan prinsip ini menjamin bahwa data yang digunakan adalah akurat, otentik, dan bebas dari manipulasi.

3. Availability (Ketersediaan)
Prinsip Availability atau ketersediaan berfokus pada memastikan bahwa informasi dan sistem selalu dapat diakses oleh pengguna yang berhak kapan pun dibutuhkan. Sebuah sistem keamanan informasi tidak akan berarti apabila data tidak bisa diakses ketika diperlukan. Oleh karena itu, Availability menekankan pentingnya menjaga kestabilan, keandalan, dan ketahanan sistem agar tidak mudah terganggu oleh kerusakan, bencana, maupun serangan siber seperti Denial of Service (DoS). Dalam praktik sehari-hari, prinsip ini terlihat pada upaya seseorang atau organisasi dalam melakukan backup data secara rutin ke media penyimpanan cadangan seperti cloud storage atau hard disk eksternal. Layanan digital seperti perbankan online, e-commerce, dan aplikasi belajar daring juga menerapkan sistem redundansi server dan pemeliharaan rutin (maintenance) untuk memastikan layanan tetap bisa diakses tanpa gangguan. Dengan menerapkan prinsip Availability, pengguna dapat memastikan bahwa data dan layanan informasi selalu siap digunakan kapan pun dibutuhkan.

---

## Langkah 3 — Dokumentasi
Ringkasan Materi= Laporan.md
! (screenshots/repo_setup.png)


---

## Langkah 4 — QUIZ
1. Tokoh yang dianggap sebagai bapak kriptografi modern adalah Whitfield Diffie dan Martin Hellman. Pada tahun 1976, mereka memperkenalkan konsep kriptografi kunci publik (public-key cryptography). Konsep ini menjadi landasan utama bagi sistem keamanan digital modern, termasuk komunikasi terenkripsi di internet.

2. Beberapa algoritma kunci publik yang populer adalah:

-RSA (Rivest–Shamir–Adleman)

-Diffie–Hellman Key Exchange

-Elliptic Curve Cryptography (ECC)

Ketiganya digunakan secara luas dalam keamanan data, komunikasi internet (HTTPS/TLS), dan tanda tangan digital.

3. Kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transposisi huruf, serta dilakukan secara manual. Sementara kriptografi modern berbasis pada algoritma matematis dan komputer, menggunakan konsep kunci digital (symmetric & asymmetric) untuk menjamin keamanan data secara ilmiah dan efisien.
