# Grime

Anytime, anywhere. 

### Deployment
View Grime's live website here: [Grime Deployment Page](http://daniel-ferdiansyah-grime.pbp.cs.ui.ac.id/)

---

## Tugas 2 - PBP 24/25

### Langkah Implementasi

**1. Membuat sebuah project Django baru**

Untuk menginisiasi sebuah project baru pada Django, kita dapat menjalankan command berikut `django-admin startproject [nama_project]`. Framework akan menyiapkan berbagai struktur yang diperlukan setelahnya.

**2. Membuat 'main' app pada project**

Setelah berhasil menginiasi project Django, kita dapat membuat `main` app dengan command `python manage.py startapp main`. Kita akan melakukan development back-end dan semua fitur utama pada 'main' app.

**3. Melakukan routing**

Pada direktori project, kita dapat melakukan routing untuk mengarahkan request ke `main` app pada `urls.py`. 

**4. Membuat model Product**

Di dalam direktori `main`, dapat dibuat model baru pada file `models.py`. Dalam tugas ini, model yang diperlukan adalah `Product` dengan atribut wajib sebagai berikut
- `name`        --> CharField
- `price`       --> IntegerField
- `description` --> TextField

**5. Mengembangkan views.py agar dapat diintegrasi pada main.html**

Untuk membuat aplikasi lebih mudah dimaintain, kita dapat memisahkan front-end dengan back-end. Kita dapat membuat fungsi ada `views.py` agar dapat melakukan render template html. Pada tugas ini, template masih berisi nama project, nama, dan kelas mahasiswa.

**6. Membuat routing pada urls.py**

Pada `main` app, kita perlu menambahkan routing yang dapat memetakan URL ke fungsi yang ada pada `views.py` agar pengguna dapat mengakses page melalui URL yang sesuai.

**7. Melakukan Deployment ke PWS**

Jika project sudah cukup baik, maka dapat dilakukan deployment ke [Pacil Web Service](https://pbp.cs.ui.ac.id) sebagai deployment agar dapat diakses melalui internet.

**8. Membuat README.md**

Selanjutnya, dibuat file `README.md` yang berisi deskripsi relevan project, link menuju PWS project terkait, dan jawaban dari pertanyaan-pertanyaan pada Tugas 2 PBP.

### Django workflow

![Django workflow chart](https://github.com/user-attachments/assets/ea09fdf4-3b16-4254-89d2-ed7dcd5d05ad)

### Fungsi Git

Git merupakan Version Control System yang berguna untuk developer melakukan tracking dari perubahan-perubahan setiap code yang telah dilakukan. Selain itu, developer juga dapat bekerja secara kolektif untuk mengembangkan aplikasi mereka secara rapi dan terstruktur menggunakan git. Developer juga dapat kembali ke versi perubahan sebelum-sebelumnya jika ternyata terdapat bug atau kesalahan pada versi terbaru. 

### Mengapa Django digunakan untuk permulaan Software Development?

Beberapa alasan yang cukup relevan adalah

- Framework Lengkap
  Django memiliki banyak fitur bawaan yang cukup lengkap seperti autentikasi user, admin panel,   form handling, dan keamanan yang baik. Hal tersebut memudahkan developer agar tidak melakukan   konfigurasi semuanya dari awal.

- Arsitektur MVT
  Model-View-Template membantu pemula untuk memahami struktur aplikasi web dengan baik dan        memisahkan front-end dengan back-end secara terstruktur.

- Scalability
  Django dirancang agar dapat menangani project kecil hingga besar. Sehingga, framework ini       dapat memberi gambaran nyata mengenai real world project yang kompleks.

## Mengapa model Django disebut ORM

Model pada Django disebut ORM (Object-Relational Mapping) karena model pada Django menghubungkan object dalam kode Python dengan database relational seperti PostgreSQL, MySQL, dan SQLite. Sehingga, kode lebih terstruktur dan lebih baik untuk dimaintain.




