# Grime

Anytime, anywhere. 

### Deployment
View Grime's live website here: [Grime Deployment Page](http://daniel-ferdiansyah-grime.pbp.cs.ui.ac.id/)

### Tugas
[Tugas 2](https://github.com/danferdiansyah/grime/wiki/Tugas-2) - [Tugas 3](https://github.com/danferdiansyah/grime/wiki/Tugas-3)

---

## Tugas 3 - PBP 24/25

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian sebuah platform karena memastikan bahwa data dapat diakses dan diproses secara efisien dari sumber ke tujuan, baik itu antar server, perangkat, atau pengguna akhir. Ini penting untuk menjaga performa platform, memberikan respon yang cepat, serta memastikan integritas dan keamanan data. Selain itu, mekanisme data delivery yang andal memungkinkan platform untuk mendukung berbagai fungsionalitas seperti real-time processing, analisis data, sinkronisasi antar sistem, dan pengalaman pengguna yang optimal. Tanpa data delivery yang efektif, platform bisa mengalami bottleneck, latensi, dan inkonsistensi data.

### Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON umumnya dianggap lebih baik daripada XML untuk banyak kasus, terutama dalam pengembangan web dan aplikasi modern. Ada beberapa alasan mengapa JSON lebih populer dibandingkan XML:

1. **Struktur Sederhana dan Ringkas**

JSON menggunakan format yang lebih sederhana dengan struktur data berbasis objek, yang mudah dipahami dan diintegrasikan dengan bahasa pemrograman modern seperti JavaScript, Python, dan lainnya. XML, di sisi lain, lebih verbose dengan tag pembuka dan penutup, yang membuatnya lebih panjang dan sulit dibaca.
  
2. **Kinerja**

Karena lebih ringan dan tidak memiliki overhead seperti tag XML yang berlebihan, JSON lebih cepat diproses dan ditransfer, sehingga lebih efisien untuk pengiriman data dalam aplikasi berbasis web.

3. **Native Support dalam JavaScript**

JSON terintegrasi langsung dengan JavaScript, yang merupakan bahasa pemrograman paling umum di web development. Hal ini membuat parsing dan manipulasi data JSON sangat mudah tanpa perlu library tambahan, sedangkan XML memerlukan pemrosesan tambahan.

4. **Human-Readable**

JSON lebih mudah dibaca oleh manusia karena strukturnya yang menyerupai objek dalam pemrograman, sementara XML terlihat lebih kompleks karena tag-tag yang digunakan.

Overall, JSON lebih cocok untuk aplikasi modern yang mengutamakan kecepatan, simplicity, dan efisiensi.

### Fungsi dari method `is_valid()` pada form Django

Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang di-submit ke form memenuhi validasi yang telah ditentukan. Method ini melakukan beberapa hal penting:

1. **Memeriksa Input Pengguna**: `is_valid()` akan mengecek apakah data yang di-inputkan pengguna sesuai dengan aturan validasi form, seperti apakah tipe data benar, apakah field yang diperlukan terisi, dan apakah aturan validasi lainnya terpenuhi.
   
2. **Membersihkan Data**: Jika data valid, method ini juga memanggil proses *cleaning*, di mana input yang valid akan diproses lebih lanjut dan disimpan dalam atribut `cleaned_data` sebagai data yang bersih dan siap digunakan.

3. **Error Handling**: Jika data tidak valid, `is_valid()` mengembalikan nilai `False` dan menyimpan pesan error dalam atribut `errors`, yang bisa ditampilkan kepada pengguna untuk memberi tahu mereka tentang kesalahan yang terjadi.

Kita membutuhkan method ini untuk memastikan bahwa data yang dikirim oleh pengguna tidak mengandung kesalahan atau input yang tidak sesuai sebelum diproses lebih lanjut, misalnya sebelum menyimpan data ke database. Validasi ini mencegah terjadinya error atau kerusakan data di sistem.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF). CSRF adalah jenis serangan di mana penyerang mencoba memaksa pengguna yang sudah terautentikasi di suatu situs untuk melakukan aksi yang tidak diinginkan tanpa sepengetahuan mereka.

**`csrf_token` penting karena:**

1. **Mencegah CSRF**: Django menggunakan token CSRF sebagai mekanisme untuk memverifikasi bahwa permintaan yang dikirim ke server berasal dari sumber yang sah. Token ini unik untuk setiap session pengguna dan disematkan ke setiap form atau permintaan POST.
   
2. **Validasi Permintaan**: Saat form dikirim, Django memverifikasi apakah token CSRF yang dikirim sesuai dengan token yang disimpan di sisi server untuk memastikan bahwa permintaan tersebut sah dan bukan berasal dari pihak ketiga yang berbahaya.

**Apa yang terjadi jika kita tidak menambahkan `csrf_token`?**
Jika `csrf_token` tidak ditambahkan pada form Django, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan kondisi ini dengan mengirimkan permintaan yang terlihat sah ke server melalui pengguna yang sudah terautentikasi, misalnya, dengan menyisipkan form berbahaya di situs atau email yang mengarahkan pengguna untuk mengirimkan data tanpa sepengetahuan mereka.

**Bagaimana penyerang dapat memanfaatkannya?**

1. **Eksekusi Aksi yang Tidak Sah**: Penyerang dapat membuat pengguna yang sudah login untuk mengirimkan permintaan POST yang tidak diinginkan, seperti mengubah pengaturan akun, melakukan transaksi, atau menghapus data tanpa persetujuan pengguna.
   
2. **Mengelabui Pengguna**: Dengan CSRF, penyerang bisa membuat permintaan dari situs yang mereka kontrol ke aplikasi Django tanpa pengguna menyadarinya, memanfaatkan sesi pengguna yang valid untuk melakukan aksi berbahaya.

Dengan menggunakan `csrf_token`, Django memastikan bahwa setiap permintaan form POST berasal dari sumber yang sah dan mencegah eksploitasi semacam ini.

## Implementasi step by step

**1. Membuat Input Form untuk Menambahkan Objek Model**

Buat form Product menggunakan ModelForm

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'quantity']
```

Buat View untuk Input Form: Buat view untuk menampilkan dan memproses form input.

```python
def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main:show_model')
    
    context = {'form': form }
    return render(request, 'add/create_product.html', context)
```

Buat template `html` untuk merender form yang telah dibuat

```python
...
<div class="container">
        <!-- Center the heading -->
        <h1>Add New Product</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                <tr>
                    <td><label for="id_name">Product Name:</label></td>
                    <td>{{ form.name }}</td>
                </tr>
                <tr>
                    <td><label for="id_price">Price:</label></td>
                    <td>{{ form.price }}</td>
                </tr>
                <tr>
                    <td><label for="id_description">Description:</label></td>
                    <td>{{ form.description }}</td>
                </tr>
                <tr>
                    <td><label for="id_quantity">Quantity:</label></td>
                    <td>{{ form.quantity }}</td>
                </tr>
                <tr>
                    <td colspan="2"> <!-- Merge the table cells -->
                      <div class="button-container">
                        <input type="submit" value="Add Product" />
                      </div>
                    </td>
                </tr>
            </table>
        </form>
    </div>
...
```

Tambah URL untuk form tersebut di `urls.py`

```python
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    ...
]
```

### Menambahkan 4 Fungsi Views

1. XML

```python
def show_all_xml(_):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

2. XML by ID

```python
def show_id_xml(_, id: str):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

3. JSON

```python
def show_all_json(_):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

4. JSON by ID

```python
def show_id_json(_, id: str):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Lalu buat routing untuk masing-masing views ke dalam `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', show_model, name='show_model'),
    path('add/', create_product_form, name='create_product_form'),
    path('xml/', show_all_xml, name='show_all_xml'),
    path('xml/<str:id>/', show_id_xml, name='show_id_xml'),
    path('json/', show_all_json, name='show_all_json'),
    path('json/<str:id>/', show_id_json, name='show_id_json'),
]
```

## API Call menggunakan Postman

**XML**
![XML](https://github.com/user-attachments/assets/c133ce99-b3e4-4973-9dd2-001bebc7c4fb)

**XML by ID**
![XML by ID](https://github.com/user-attachments/assets/1457eca3-2e9b-4d23-803a-e59411711353)

**JSON**
![JSON](https://github.com/user-attachments/assets/9636d9a8-bae7-4bf3-a7d3-734e0a87945a)

**JSON by ID**
![JSON by ID](https://github.com/user-attachments/assets/b27896bc-6d5b-46f2-8ba2-3a1cc0470512)

