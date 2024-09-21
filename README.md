# Grime

Anytime, anywhere. 

### Deployment
View Grime's live website here: [Grime Deployment Page](http://daniel-ferdiansyah-grime.pbp.cs.ui.ac.id/)

### Tugas
[Tugas 2](https://github.com/danferdiansyah/grime/wiki/Tugas-2) - [Tugas 3](https://github.com/danferdiansyah/grime/wiki/Tugas-3)

---

## Tugas 4 - PBP 24/25

### 1. Perbedaan antara HttpResponseRedirect() dan redirect()

**HttpResponseRedirect()**

menghasilkan respon HTTP untuk melakukan redirect ke URL tertentu. Ini mengirimkan status kode HTTP 302 ke browser, yang memberitahu browser untuk mengunjungi URL yang berbeda.

**Parameter**: Memerlukan URL tujuan sebagai argumen (string).

**Penggunaan**: Biasanya digunakan untuk redirect sederhana, di mana URL tujuan sudah ditentukan.

contohnya,

```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/url/')
```

**redirect()**

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

### 2. Cara Kerja Penghubungan Model `MoodEntry` dengan `User`

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

### Perbedaan Authentication dan Authorization

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

### Bagaimana Django mengingat pengguna yang telah login serta kegunaan dan keamanan penggunaan cookies

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

1. **Implementasi Regist, Login, dan Logout**

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

from django.contrib.auth.views import LogoutView

```python
urlpatterns = [
    ...
    path('logout/', LogoutView.as_view(), name='logout'),
]
```
Pada html, tambahkan

```html
<a href="{% url 'logout' %}">Logout</a>
```

