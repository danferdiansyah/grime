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

   Selanjutnya, kita dapat mengimpelentasikan form untuk modal tersebut sebagai berikut

   ```html
      <div id="product_cards"></div>
        <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
          <div id="crudModalContent" class="relative bg-gray-200 rounded-[25px] shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 border-b rounded-t">
              <h3 class="text-xl font-semibold text-gray-900">
                Add New Product
              </h3>
              <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <span class="sr-only">Close modal</span>
              </button>
            </div>
            <!-- Modal body -->
            <div class="px-6 py-4 space-y-6 form-style">
                <form id="productForm" enctype="multipart/form-data">
      
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- Name -->
                  <div class="space-y-4">
                    <div class="mb-4">
                        <label for="name" class="block text-sm font-medium text-gray-700 mb-2">Name</label>
                        <input type="text" id="name" name="name" class="block w-full px-3 py-2 text-center border border-[#05e500] hover:border-white text-black bg-white rounded-[15px] focus:outline-white focus:outline-[2px] focus:outline-offset-0 focus:ring-0 focus:bg-opacity-100 focus:placeholder-opacity-100 text-opacity-50 transition duration-200 ease-in-out shadow-lg focus:text-opacity-100 focus:shadow-[0px_0px_10px_5px_rgba(255,255,255,0.4)]" placeholder="Enter product name" required>
                    </div>
                    
                    <!-- Price -->
                    <div class="mb-4">
                        <label for="price" class="block text-sm font-medium text-gray-700 mb-2">Price</label>
                        <input type="number" id="price" name="price" class="block w-full px-3 py-2 text-center border border-[#05e500] hover:border-white text-black bg-white rounded-[15px] focus:outline-white focus:outline-[2px] focus:outline-offset-0 focus:ring-0 focus:bg-opacity-100 focus:placeholder-opacity-100 text-opacity-50 transition duration-200 ease-in-out shadow-lg focus:text-opacity-100 focus:shadow-[0px_0px_10px_5px_rgba(255,255,255,0.4)]" placeholder="Enter product price" required>
                    </div>
                    
                    <!-- Quantity -->
                    <div class="mb-4">
                        <label for="quantity" class="block text-sm font-medium text-gray-700 mb-2">Quantity</label>
                        <input type="number" id="quantity" name="quantity" class="block w-full px-3 py-2 text-center border border-[#05e500] hover:border-white text-black bg-white rounded-[15px] focus:outline-white focus:outline-[2px] focus:outline-offset-0 focus:ring-0 focus:bg-opacity-100 focus:placeholder-opacity-100 text-opacity-50 transition duration-200 ease-in-out shadow-lg focus:text-opacity-100 focus:shadow-[0px_0px_10px_5px_rgba(255,255,255,0.4)]" min="1" placeholder="Enter available quantity" required>
                    </div>
                  </div>
                  
                  <div class="space-y-4">
                    <!-- Description -->
                    <div class="mb-4">
                        <label for="description" class="block text-sm font-medium text-gray-700 mb-2">Description</label>
                        <textarea id="description" name="description" rows="3" class="block w-full px-3 py-2 text-center border border-[#05e500] hover:border-white text-black bg-white rounded-[15px] focus:outline-white focus:outline-[2px] focus:outline-offset-0 focus:ring-0 focus:bg-opacity-100 focus:placeholder-opacity-100 text-opacity-50 transition duration-200 ease-in-out shadow-lg focus:text-opacity-100 focus:shadow-[0px_0px_10px_5px_rgba(255,255,255,0.4)]" placeholder="Enter product description" required></textarea>
                    </div>
      
                    <!-- Image -->
                    <div class="mb-4">
                        <label for="image" class="block text-sm font-medium text-gray-700 mb-2">Product Image</label>
                        <input type="file" id="image" name="image" class="block w-full px-3 py-2 text-center border border-[#05e500] hover:border-white text-black bg-white rounded-[15px] focus:outline-white focus:outline-[2px] focus:outline-offset-0 focus:ring-0 focus:bg-opacity-100 focus:placeholder-opacity-100 text-opacity-50 transition duration-200 ease-in-out shadow-lg focus:text-opacity-100 focus:shadow-[0px_0px_10px_5px_rgba(255,255,255,0.4)]" accept="image/*">
                    </div>
                  </div>
                </div>
      
                </form>
            </div>
            <!-- Modal footer -->
            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
              <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
              <button type="submit" id="submitproduct" form="productForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
            </div>
          </div>
        </div>
   ```

   Agar modal dapat muncul ketika button ditekan, kita perlu menambahkan script berikut pada file html di antara `<script>...</script>`
   ```javascript
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');
      
      function showModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');
      
            modal.classList.remove('hidden'); 
            setTimeout(() => {
              modalContent.classList.remove('opacity-0', 'scale-95');
              modalContent.classList.add('opacity-100', 'scale-100');
            }, 50); 
      }
      
      function hideModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');
      
            modalContent.classList.remove('opacity-100', 'scale-100');
            modalContent.classList.add('opacity-0', 'scale-95');
      
            setTimeout(() => {
              modal.classList.add('hidden');
            }, 150); 
      }
      
      document.getElementById("cancelButton").addEventListener("click", hideModal);
      document.getElementById("closeModalBtn").addEventListener("click", hideModal);
   ```

3. Membuat fungsi `view` baru untuk menambahkan product ke database. Hal ini dapat dilakukan dengan menambah import berikut pada `views.py`
   ```python
   from django.views.decorators.csrf import csrf_exempt
   from django.views.decorators.http import require_POST
   ```
   Lalu, kita buat sebuah fungsi untuk menerima data produk baru dari sebuah permintaan AJAX menggunakan metode `POST` seperti berikut
   ```python
   @csrf_exempt
   @require_POST
   def add_product_ajax(request):
       name = strip_tags(request.POST.get("name"))
       price = request.POST.get("price")
       description = strip_tags(request.POST.get("description"))
       quantity = request.POST.get("quantity")
       image = request.FILES.get("image")
       user = request.user
       
       new_product = Product(
           name=name, 
           price=price,
           description=description,
           quantity=quantity,
           image=image,
           user=user
       )
       new_product.save()
   
       return HttpResponse(b"CREATED", status=201)
   ```

4. Lalu, kita perlu menambahkan path di `urls.py` yang mengarah ke fungsi `add_product_ajax()` dengan cara mengimport fungsi yang telah dibuat serta menambahkan path pada `urlpatterns`
   ```python
   from main.views import

   urlpatterns = [
    ...
    path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
   ]
   ```

5. Menghubungkan form di dalam modal dengan path `add_product_ajax`, hal ini dapat dilakukan dengan menambahkan script berikut pada file `main.html`
   ```javascript
      function addProduct() {
       fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#productForm')),
          })
          .then(response => refreshProducts())
        
          document.getElementById("productForm").reset(); 
          document.querySelector("[data-modal-toggle='crudModal']").click();
        
          return false;
      }
      
      document.getElementById("productForm").addEventListener("submit", (e) => {
          e.preventDefault();
          addProduct();
      })
   ```

6. Membuat function untuk merefresh halaman secara asinkronus untuk menampilkan data product tanpa reload dengan cara menambahkan script berikut pada file `main.html`
   ```javascript
   async function getProducts(){
       return fetch("{% url 'main:show_json' %}").then((res) => res.json())
   }
   ```
   Lalu kita juga perlu menambahkan fungsi berikut pada script (sesuai dengan style product card yang dibuat)
   ```javascript
      async function refreshProducts() {
       document.getElementById("product_cards").innerHTML = "";
       document.getElementById("product_cards").className = "";
       const Products = await getProducts();
       let htmlString = "";
       let classNameString = "";
   
       if (Products.length === 0) {
           classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
           htmlString = `
               <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                   <p class="text-center text-gray-600 mt-4">No product yet.</p>
               </div>
           `;
       }
       else {
         classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 w-full max-w-7xl mx-auto"
         Products.forEach((item) => {
             const name = DOMPurify.sanitize(item.fields.name);
             const description = DOMPurify.sanitize(item.fields.description);
             const imageUrl = item.fields.image ? `/media/${item.fields.image}` : '/path/to/placeholder-image.png';
             htmlString += `
             <div class="relative break-inside-avoid" onclick="openPopup('${name}', ${item.fields.quantity}, '${item.fields.price}', '${description}', '${imageUrl}', '${item.pk}')">
             <div class="relative top-5 bg-white shadow-lg rounded-[24px] mb-6 break-inside-avoid flex flex-col items-center border-2 border-gray-200 hover:shadow-[0px_0px_15px_5px_rgba(255,255,255,0.4)] hover:transform hover:scale-105 transition-transform duration-300 cursor-pointer"
                 style="width: 300px; height: 320px;"> <!-- Fixed height for the card -->
   
               <div class="bg-gray-200 w-[100%] h-[100%] flex justify-center items-center rounded-[20px] mt-4 overflow-hidden">
               ${item.fields.image ? `<img src="${imageUrl}" alt="Product Image" class="rounded-lg object-cover w-full h-full" />` : `<div class="flex items-center justify-center w-full h-full text-gray-500">No Image Available</div>`}
               </div>
   
               <!-- Product Name and Price -->
               <div class="p-3 text-center w-full h-[40%] flex flex-col justify-end">
                 <h3 class="font-bold text-lg mb-2 text-gray-800">${name}</h3>
                 <div class="flex justify-center items-center space-x-2">
                   <span class="bg-gray-100 rounded-full px-3 py-1 text-gray-800 text-sm">${item.fields.price}</span>
                   <span class="text-gray-600 text-xs">IDR</span>
                 </div>
               </div>
             </div>
   
             <!-- Popup Modal for Product Details -->
             <div id="productPopup-${item.pk}" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" onclick="closePopup('${item.pk}')">
               <!-- Modal Content -->
               <div class="bg-white p-6 rounded-[24px] shadow-lg max-w-md w-full mx-auto relative" onclick="event.stopPropagation()" style="width: 400px;">
                 <h3 id="popupName-${item.pk}" class="font-bold text-lg mb-2 text-black text-center"></h3>
   
                 <!-- Gray Placeholder (Removed Image) -->
                 <div class="bg-gray-200 flex justify-center items-center rounded-[20px] overflow-hidden mb-4 w-[100%] h-[100%] mx-auto">
                   <div class="flex justify-center items-center w-full h-full text-gray-500">
                       <img id="popupImage-${item.pk}" src="" alt="Product Image" class="rounded-lg object-cover w-full h-full" style="aspect-ratio: 1/1; max-width: 100%; max-height: 100%;" />
                   </div>
                 </div>
   
                 <p id="popupQuantity-${item.pk}" class="text-gray-600 text-sm mb-4 text-center"></p>
                 <p id="popupDescription-${item.pk}" class="text-gray-700 mb-4 text-center"></p>
                 <p id="popupPrice-${item.pk}" class="text-gray-900 font-semibold text-center mb-6"></p>
   
                 <!-- Edit and Delete Buttons -->
                 <div class="flex justify-center space-x-4 mb-4">
                   <a href="/edit-product/${item.pk}"  class="edit-button bg-white hover:bg-[#c9c9c9] text-black rounded-full p-2 transition duration-300 shadow-md">
                     <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                         <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                     </svg>
                   </a> 
                   <a href="/delete-product/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                     <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                       <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                     </svg>
                   </a>
                 </div>
   
                 <!-- Close Button -->
                 <button onclick="closePopup('${item.pk}')" class="absolute top-2 right-2 bg-[#05e500] hover:bg-[#04b600] text-white py-1 px-3 rounded-full font-bold">close</button>
               </div>
             </div>
           </div>
               `;
           });
       }
       document.getElementById("product_cards").className = classNameString;
       document.getElementById("product_cards").innerHTML = htmlString;
     }
     refreshProducts();
   ```
