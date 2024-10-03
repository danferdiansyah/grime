# Grime

Anytime, anywhere. 

### Deployment
View Grime's live website here: [Grime Deployment Page](http://daniel-ferdiansyah-grime.pbp.cs.ui.ac.id/)

### Tugas
[Tugas 2](https://github.com/danferdiansyah/grime/wiki/Tugas-2) - [Tugas 3](https://github.com/danferdiansyah/grime/wiki/Tugas-3) - [Tugas 4](https://github.com/danferdiansyah/grime/wiki/Tugas-4) - [Tugas 5](https://github.com/danferdiansyah/grime/wiki/Tugas-5)

---

## Tugas 6 - PBP 24/25

## **Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web**
   JavaScript memiliki banyak manfaat dalam pengembangan aplikasi web, antara lain:

   - **Interaktif**: JavaScript memungkinkan pembuatan elemen interaktif di halaman web, seperti dropdown, sliders, form validation, dan modal windows, yang meningkatkan pengalaman pengguna.
     
   - **Manipulasi DOM**: JavaScript dapat memanipulasi elemen-elemen di halaman web (DOM) secara dinamis, seperti menambah, menghapus, atau mengubah konten tanpa perlu memuat ulang halaman.
     
   - **Asynchronous Communication**: Dengan fitur seperti `XMLHttpRequest` atau `fetch()`, JavaScript memungkinkan komunikasi asinkron dengan server (AJAX), yang membuat aplikasi lebih responsif tanpa reload halaman.
     
   - **Cross-platform**: JavaScript berjalan di hampir semua browser modern, sehingga kode yang ditulis dapat dijalankan di berbagai perangkat dan platform.
     
   - **Mendukung Pengembangan SPA (Single Page Application)**: JavaScript framework/library seperti React, Angular, dan Vue memungkinkan pengembangan aplikasi web yang cepat dan efisien dengan konsep SPA, di mana aplikasi berjalan lebih cepat karena hanya sebagian halaman yang di-refresh.

## **Fungsi dari Penggunaan `await` dengan `fetch()`**
   `await` digunakan untuk menunggu hasil dari fungsi asynchronous seperti `fetch()`. Fungsi ini memblokir eksekusi baris kode berikutnya sampai permintaan `fetch()` selesai dan respons diterima.
   
   - **Fungsi utama `await`**: Mengubah perilaku asynchronous menjadi seperti synchronous. Dengan `await`, kode setelahnya tidak akan dieksekusi sampai proses `fetch()` selesai. Ini membuat kode lebih mudah dipahami karena tidak perlu menggunakan callback atau `.then()` chaining.
   
   - **Jika `await` tidak digunakan**: Jika kita tidak menggunakan `await`, fungsi `fetch()` akan mengembalikan *Promise* yang belum selesai. Kode selanjutnya akan langsung dieksekusi tanpa menunggu hasil dari `fetch()`. Hal ini bisa menyebabkan masalah, seperti data yang diharapkan belum tersedia saat ingin diproses.

   Contoh:
   ```javascript
   const response = fetch('url'); // Mengembalikan Promise
   const data = response.json();   // Ini akan dieksekusi sebelum response selesai
   ```

   Dengan `await`:
   ```javascript
   const response = await fetch('url');
   const data = await response.json(); // Menunggu response selesai
   ```

## **Penggunaan Decorator `csrf_exempt` pada View untuk AJAX POST**
   Decorator `@csrf_exempt` digunakan untuk mengecualikan view dari mekanisme perlindungan **Cross-Site Request Forgery (CSRF)**. Dalam Django, mekanisme CSRF digunakan untuk mencegah serangan di mana pengguna secara tidak sengaja mengirimkan permintaan yang tidak valid (malicious request).

   Namun, dalam beberapa kasus seperti ketika menggunakan AJAX untuk POST request, token CSRF tidak selalu dikirim secara otomatis, sehingga kita mungkin mengalami kesalahan (error) saat melakukan POST tanpa token CSRF yang valid. Dengan menambahkan `@csrf_exempt` pada view tersebut, kita memberi tahu Django untuk tidak memeriksa token CSRF pada request tersebut.

   **Perlu dicatat**, menonaktifkan CSRF harus dilakukan dengan hati-hati dan hanya jika benar-benar diperlukan, karena dapat membuka celah keamanan. Alternatif yang lebih aman adalah menyertakan token CSRF dalam header AJAX request.

## **Mengapa Pembersihan Data Input Pengguna Dilakukan di Backend**
   Pembersihan data input pengguna sebaiknya tetap dilakukan di backend untuk alasan keamanan dan keandalan. Alasan utama adalah:
   
   - **Keamanan**: Validasi di frontend dapat dimanipulasi oleh pengguna dengan mematikan JavaScript atau mengubah kode halaman, sehingga hanya mengandalkan validasi di frontend bisa berisiko tinggi terhadap serangan seperti injeksi kode atau pengiriman data yang tidak valid. Validasi di backend memastikan bahwa setiap data yang diterima dari pengguna sudah bersih dan aman.
     
   - **Reliabilitas**: Frontend adalah lapisan yang lebih mudah diubah oleh pengguna, sehingga backend perlu memiliki lapisan validasi tersendiri agar aplikasi tetap bekerja dengan benar meskipun ada modifikasi di sisi frontend.
     
   - **Standar**: Dalam pengembangan aplikasi yang baik, validasi seharusnya dilakukan di kedua sisi (frontend dan backend) untuk memberikan pengalaman pengguna yang baik (dengan validasi cepat di frontend) serta menjaga keamanan dan integritas data di backend.

## **Step by Step Implementasi**

## AJAX `GET`



## AJAX `POST`

1. Membuat button form untuk menambahkan product dapat diimplementasikan dengan menambahkan code berikut setelah button yang mengarah ke halaman `create-product`.

   ```html
      <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="w-auto ml-4 flex justify-center py-2 px-4 text-sm font-medium rounded-[15px] text-black bg-white hover:bg-gray-200 focus:outline-none focus:ring-0 transition duration-200 ease-in-out
      hover:shadow-[0px_0px_15px_5px_rgba(255,255,255,0.4)]" onclick="showModal();">
        Add New Product by AJAX
      </button>
   ```

   
