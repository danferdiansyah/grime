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

**Django workflow**
https://github.com/danferdiansyah/grime/issues/1#issue-2515338197


