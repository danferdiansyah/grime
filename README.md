# Grime

Anytime, anywhere. 

### Deployment
View Grime's live website here: [Grime Deployment Page](http://daniel-ferdiansyah-grime.pbp.cs.ui.ac.id/)

### Tugas
[Tugas 2](https://github.com/danferdiansyah/grime/wiki/Tugas-2) - [Tugas 3](https://github.com/danferdiansyah/grime/wiki/Tugas-3) - [Tugas 4](https://github.com/danferdiansyah/grime/wiki/Tugas-4)

---

## Tugas 5 - PBP 2024/2025
## Urutan Prioritas CSS Selector
Jika beberapa CSS selector diterapkan pada elemen HTML yang sama, CSS menggunakan aturan spesifisitas (specificity) untuk menentukan selector mana yang akan diprioritaskan. Berikut urutan prioritasnya:

1. **Inline Styles** (contoh `style="color: red;"`) memiliki prioritas paling tinggi.
2. **ID Selector** (contoh `#header`) memiliki prioritas lebih tinggi dibandingkan class atau elemen.
3. **Class Selector** (contoh `.menu`) lebih kuat dibandingkan tag HTML.
4. **Tag Selector** (contoh `h1`, `p`) memiliki prioritas paling rendah.
5. **Important Rule** (`!important`) dapat mengesampingkan semua aturan di atas dan memberikan prioritas tertinggi untuk sebuah properti.

### Contoh:
```html
<div id="header" class="menu">Title</div>
```

Jika ada CSS seperti berikut:
```css
#header { color: black; }
.menu { color: yellow; }
div { color: red; }
```
Maka elemen tersebut akan berwarna **hitam** karena **ID selector** memiliki prioritas tertinggi.


## 2. Mengapa Responsive Design Penting?
**Responsive design** adalah pendekatan dalam desain web di mana tampilan halaman web dapat menyesuaikan dengan berbagai ukuran dan orientasi layar perangkat pengguna. Konsep ini sangat penting karena pengguna mengakses web melalui berbagai perangkat seperti komputer desktop, tablet, dan smartphone.

### Keuntungan Responsive Design:
- Pengalaman pengguna yang lebih baik di berbagai perangkat.
- Aksesibilitas yang lebih luas.
- SEO yang lebih baik karena search machine memberi index lebih kepada situs web yang accessible di berbagai perangkat.

### Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
- **ChatGPT**: Antarmuka pengguna yang responsif di berbagai perangkat.
  
### Contoh Aplikasi yang Belum Menerapkan Responsive Design:
- **SIAK NG**: Hanya nyaman dilihat jika di desktop.

## Perbedaan antara Margin, Border, dan Padding
- **Margin**: Ruang kosong di luar elemen, yang memisahkan elemen tersebut dari elemen lainnya.
- **Border**: Garis yang mengelilingi elemen, terletak di antara margin dan padding.
- **Padding**: Ruang di dalam elemen, yang memisahkan konten dari border.

### Contoh Implementasi:
```css
article {
    margin: 15px;     /* Ruang kosong di luar elemen */
    border: 1px dashed blue;  /* Garis di sekeliling elemen */
    padding: 5px;     /* Ruang di dalam elemen */
}
```

## Pemahaman tentang Flexbox dan Grid Layout

### **Flexbox**
Flexbox (Flexible Box) adalah teknik layout yang dirancang untuk menyusun elemen dalam satu dimensi, baik itu secara horizontal maupun vertikal. Flexbox memudahkan penciptaan desain yang responsif dan dapat beradaptasi dengan baik.

#### Manfaat Flexbox:
- Mengatur elemen secara dinamis dalam satu baris atau satu kolom.
- Memungkinkan elemen untuk memperluas atau menyusut sesuai dengan ruang yang tersedia.

#### Contoh Penggunaan Flexbox:
```css
.box-container {
    display: flex;
    align-items: flex-start; /* Menyelaraskan child element di bagian atas secara vertikal */
    gap: 15px; /* Jarak antara elemen */
}
```

### **Grid Layout**
Grid Layout adalah sistem layout dua dimensi yang memungkinkan pengembang untuk mendesain halaman yang lebih kompleks dengan baris dan kolom. Grid Layout sangat ideal untuk mengatur elemen dalam bentuk grid yang rapi dengan lebar kolom yang konsisten.

#### Manfaat Grid Layout:
- Menciptakan layout dua dimensi (baris dan kolom).
- Sangat cocok untuk desain yang terstruktur dan memerlukan fleksibilitas dalam mengatur ukuran kolom dan baris.

#### Contoh Penggunaan Grid Layout:
```css
.grid-container {
    display: grid;
    grid-template-rows: 100px auto; /* Dua baris, baris pertama setinggi 100px dan baris kedua otomatis */
    grid-template-columns: repeat(3, 1fr); /* Tiga kolom dengan lebar yang sama */
    gap: 20px; /* Jarak antar elemen */
}
``` 

Dengan pendekatan ini, Flexbox dan Grid Layout memberikan cara yang efektif untuk mengatur dan mendesain elemen di halaman web secara responsif dan terstruktur.


---

## Langkah-langkah Implementasi Checklist
## Implementasi Fungsi Edit dan Hapus
Tambahkan fungsi pada views.py untuk fitur  edit     dan    delete   product
  ```python

  # Edit product
  def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form, 
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "crud/edit_product.html", context)

  # Delete product
  def delete_product(request, id):
    product = Product.objects.get(pk = id)

    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))


  ```
## Kustomisasi desain pada template menggunakan CSS framework
Sebelum kita mulai menggunakan Tailwind dalam proyek, langkah pertama yang perlu dilakukan adalah menginisialisasi pemanggilan Tailwind melalui CDN (Content Distribution Network). Dengan menggunakan CDN, kita bisa memanfaatkan fitur-fitur styling yang ditawarkan oleh Tailwind tanpa perlu mengunduh atau mengkonfigurasi Tailwind di dalam direktori proyek. Panggilan CDN biasanya ditempatkan dalam file `base.html`.
```html
  .....
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            {% block meta %} {% endblock meta %}
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
        </html>
    ....
```

Setelah inisiasi, kita dapat melakukan kustomisasi di berbagai page yang kita inginkan seperti pada **Login, Register, Add Product, Edit Product, hingga Card Product**. 
