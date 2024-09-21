# Grime

Anytime, anywhere. 

### Deployment
View Grime's live website here: [Grime Deployment Page](http://daniel-ferdiansyah-grime.pbp.cs.ui.ac.id/)

### Tugas
[Tugas 2](https://github.com/danferdiansyah/grime/wiki/Tugas-2) - [Tugas 3](https://github.com/danferdiansyah/grime/wiki/Tugas-3)

---

## Tugas 4 - PBP 24/25

## Perbedaan antara HttpResponseRedirect() dan redirect()

**`HttpResponseRedirect()`**

menghasilkan respon HTTP untuk melakukan redirect ke URL tertentu. Ini mengirimkan status kode HTTP 302 ke browser, yang memberitahu browser untuk mengunjungi URL yang berbeda.

**Parameter**: Memerlukan URL tujuan sebagai argumen (string).

**Penggunaan**: Biasanya digunakan untuk redirect sederhana, di mana URL tujuan sudah ditentukan.

contohnya,

```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/url/')
```

**`redirect()`**

Lebih mudah digunakan karena bisa menerima berbagai jenis argumen, seperti URL, nama view, atau objek model, dan secara otomatis mengonversinya ke URL yang benar.

**Parameter**: Sebuah string URL (seperti HttpResponseRedirect()). Nama view (sebagai argumen pertama), yang kemudian akan di-resolve menjadi URL. Sebuah instance object model yang memiliki method get_absolute_url().

**Penggunaan**: Lebih umum digunakan karena fleksibilitasnya dan kemampuannya untuk menangani berbagai jenis argumen.

contohnya,

```python
from django.shortcuts import redirect

def my_view(request):
    return redirect('/url/')  # Redirect ke URL spesifik
    
def my_view_with_name(request):
    return redirect('view_name')  # Redirect ke view berdasarkan nama URL

def my_view_with_object(request, obj):
    return redirect(obj)  # Redirect ke URL berdasarkan method get_absolute_url() dari objek

```

## Cara Kerja Penghubungan Model `MoodEntry` dengan `User`

Model `MoodEntry` dapat dihubungkan dengan `User` menggunakan **ForeignKey**, sehingga `MoodEntry` akan dialokasikan berbeda untuk setiap user yang telah login.

```python
from django.db import models
import uuid
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()
```
Cara kerjanya:

- Setiap kali pengguna membuat mood entry, entry tersebut dikaitkan dengan user yang login.
- ForeignKey digunakan untuk membuat relasi many-to-one antara `MoodEntry` dan `User`, di mana banyak entri bisa dimiliki oleh satu pengguna.
- `on_delete=models.CASCADE` artinya jika pengguna dihapus, maka semua MoodEntry yang terkait juga akan dihapus.

## Perbedaan Authentication dan Authorization

1. **Authentication**

Proses untuk memverifikasi identitas pengguna dengan memastikan bahwa pengguna yang mencoba mengakses suatu aplikasi adalah valid dan sah.

**Proses**: Dalam Django, autentikasi biasanya dilakukan melalui login, di mana pengguna memasukkan credential mereka (seperti username dan password), yang kemudian diverifikasi oleh sistem.

Contohnya, Django menggunakan middleware authentication untuk memeriksa apakah pengguna telah masuk atau belum. Jika pengguna berhasil diverifikasi, informasi pengguna disimpan dalam object `request.user`.
Fungsi seperti `authenticate()` dan `login()` digunakan untuk autentikasi. 

```python
from django.contrib.auth import authenticate, login

def my_view(request):
    user = authenticate(username='john', password='secret')
    if user is not None:
        login(request, user)
        # Pengguna berhasil diautentikasi
    else:
        # Gagal autentikasi
```

2. **Authorization**

Proses untuk menentukan hak akses pengguna yang sudah terautentikasi dengan menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna, misalnya apakah pengguna memiliki izin untuk mengakses halaman tertentu atau melakukan tindakan tertentu (seperti menambah, mengubah, atau menghapus data).

**Proses**: Setelah pengguna berhasil diautentikasi, Django akan memeriksa izin (permissions) mereka untuk memastikan apakah mereka memiliki hak untuk melakukan aksi tertentu atau mengakses bagian tertentu dari aplikasi.

Contohnya, Django menggunakan permissions (izin) dan groups untuk mengelola authorization. Fungsi seperti `has_perm()` dan `permission_required()` decorator digunakan untuk memeriksa otorisasi.

```python
def my_view(request):
    if request.user.has_perm('app_name.permission_code'):
        # Pengguna memiliki izin
    else:
        # Pengguna tidak diizinkan
```

## Bagaimana Django mengingat pengguna yang telah login serta kegunaan dan keamanan penggunaan cookies

Django mengingat pengguna yang telah login dengan cara berikut

**Session**: Ketika pengguna berhasil melakukan login, Django membuat sebuah session untuk pengguna tersebut. Informasi session ini disimpan di server dan diidentifikasi dengan sebuah ID sesi yang unik.

**Cookies**: Django mengirimkan ID session tersebut kepada browser pengguna dalam bentuk cookie. Cookie ini akan disimpan di sisi klien (browser) dan dikirim kembali ke server dalam setiap request berikutnya.

**Verifikasi Session**: Pada setiap request, Django memeriksa cookie yang diterima untuk menemukan ID session. Jika ID session valid dan masih aktif, Django akan mengidentifikasi pengguna berdasarkan informasi sesi yang disimpan di server.

**Kegunaan Lain dari Cookies**

- Cookies dapat digunakan untuk menyimpan preferensi pengguna, seperti bahasa yang dipilih atau tema tampilan, sehingga pengguna tidak perlu mengaturnya kembali setiap kali mereka mengunjungi situs.
- Cookies digunakan untuk melacak aktivitas pengguna di situs web, seperti halaman yang dikunjungi atau barang yang ditambahkan ke keranjang belanja, yang dapat membantu dalam analisis data dan meningkatkan user experience.
- Selain digunakan untuk sesi login, cookies dapat menyimpan token otentikasi untuk API dan aplikasi web, memudahkan pengguna untuk tetap terautentikasi saat browsing.

**Apakah Semua Cookies Aman Digunakan?**
Tidak semua cookies aman karena cookies dapat dieksploitasi jika tidak dikonfigurasi dengan benar, seperti dalam kasus pencurian session, di mana penyerang dapat mengambil cookie suatu session dan mengakses akun pengguna. Cookies yang tidak aman dapat menyebabkan kebocoran informasi pribadi jika tidak disimpan dalam security yang baik.

## Step by step implementasi

### 1. Implementasi Regist, Login, dan Logout

**Registrasi**

- Buat form untuk register dengan `UserCreationForm`.
- Buat view untuk menghandle user yang registrasi ke dalam database.
- Redirect user ke halaman login setelah registrasi berhasil.

```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
```

**Login**

- Gunakan `LoginView` untuk menghandle proses login.
- Routing URL yang mengarah ke `LoginView`

```python
from django.contrib.auth.views import LoginView

urlpatterns = [
    ...
    path('login/', LoginView.as_view(), name='login'),
]
```

**Logout**

- Gunakan `LogoutView` untuk menghandle proses logout.
- Routing URL mengarah ke `LogoutView` dan sesuaikan template html

```python
from django.contrib.auth.views import LogoutView
urlpatterns = [
    ...
    path('logout/', LogoutView.as_view(), name='logout'),
]
```

Pada html, tambahkan

```html
<a href="{% url 'logout' %}">Logout</a>
```

### 2. Membuat dua akun pengguna, masing-masing tiga dummy data

Masuk ke Django Shell, lalu jalankan code berikut
```python
from django.contrib.auth.models import User
from main.models import Product  
import uuid

# Buat dua akun dummy
user1 = User.objects.create_user(username='dummy1', password='password123')
user2 = User.objects.create_user(username='dummy2', password='password123')

# Simpan kedua user
user1.save()
user2.save()

```
Selanjutnya, untuk menambahkan 3 dummy data untuk tiap akun, jalankan code berikut
```python
# Tambahkan 3 produk untuk user1
Product.objects.create(user=user1, name='Product 1A', price=10000, description='Deskripsi produk 1A', quantity=5)
Product.objects.create(user=user1, name='Product 1B', price=20000, description='Deskripsi produk 1B', quantity=3)
Product.objects.create(user=user1, name='Product 1C', price=15000, description='Deskripsi produk 1C', quantity=10)

# Tambahkan 3 produk untuk user2
Product.objects.create(user=user2, name='Product 2A', price=5000, description='Deskripsi produk 2A', quantity=8)
Product.objects.create(user=user2, name='Product 2B', price=25000, description='Deskripsi produk 2B', quantity=4)
Product.objects.create(user=user2, name='Product 2C', price=30000, description='Deskripsi produk 2C', quantity=2)
```
Dengan demikian, dummy account dan dummy data berhasil dibuat pada local project dan bisa digunakan dengan semestinya.

### 3. Menghubungkan model `Product` dengan `User`

Pada `models.py`, import
```python
from django.contrib.auth.models import User
```
Lalu, pada class `Product`, tambahkan atribut
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Selanjutnya, ubah `create_product` menjadi seperti berikut
```python
def create_product(request):
    
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form,
               'name' : 'Daniel Ferdiansyah',
               'class' : 'PBP F'}
    return render(request, "create_product.html", context)
```

Dengan demikian, `Product` telah diintegrasi dengan `User`. Sehingga, tiap user punya alokasi object Product berbeda dengan user lainnya.

### 4. Menampilkan detail informasi pengguna yang sedang logged in seperti `username` dan menerapkan cookies seperti `last login` 

- **Username**
Untuk menampilkan username pada `main.html`, kita dapat menambahkan key baru pada `context` yang ada pada `show_main` di `views.py` seperti berikut
```python
context = {
        ...
        'login_user' : request.user.username,
        ...
}
```
serta memperbarui `main.html` dengan menambahkan block code berikut
```html
<p> Hi <b>{{ login_user }}</b>, welcome to</p>
```

- **Login**
Untuk menampilkan last login session user, pada `views.py`, import beberapa modul berikut
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
Lalu pada `login_user`, tambahkan cookie bernama `last_login` dengan mereplace code block `if form.is_valid()` menjadi
```python
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Lalu tambah `context` pada `show_main` seperti berikut
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```
Selanjutnya, ubah `logout_user` menjadi seperti berikut
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Dan finally, pada `main.html`, tambahkan code block
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
