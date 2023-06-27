# Analisis Algoritma Pengurutan (Bubble Sort dan Insertion Sort):

# Bubble Sort:
Worst Case: Pada kondisi terburuk, ketika array dalam keadaan terbalik, Bubble Sort akan melakukan maksimal (n-1) * n / 2 perbandingan, di mana n adalah jumlah elemen dalam array. Ini terjadi ketika setiap elemen harus bergeser dari posisi awalnya ke posisi akhirnya.
Best Case: Pada kondisi terbaik, ketika array sudah terurut secara membesar, Bubble Sort akan melakukan hanya 0 perbandingan tambahan. Ini terjadi ketika tidak ada pasangan elemen yang perlu ditukar.
Average Case: Rata-rata, Bubble Sort akan melakukan sekitar (n-1) * n / 4 perbandingan. Ini dapat dianggap sebagai kasus tengah antara worst case dan best case.

# Insertion Sort:
Worst Case: Pada kondisi terburuk, ketika array dalam keadaan terbalik, Insertion Sort akan melakukan maksimal (n-1) * n / 2 perbandingan dan pergeseran elemen. Ini terjadi ketika setiap elemen harus dimasukkan ke posisinya yang tepat dengan menggeser elemen-elemen sebelumnya.
Best Case: Pada kondisi terbaik, ketika array sudah terurut secara membesar, Insertion Sort akan melakukan hanya n-1 perbandingan tambahan. Ini terjadi ketika setiap elemen sudah berada di posisinya yang tepat.
Average Case: Rata-rata, Insertion Sort akan melakukan sekitar (n-1) * n / 4 perbandingan dan pergeseran elemen. Ini dapat dianggap sebagai kasus tengah antara worst case dan best case.

Dalam kedua algoritma pengurutan ini, perbandingan adalah operasi dominan yang mempengaruhi kompleksitas waktu. Kedua algoritma memiliki kompleksitas waktu O(n^2) dalam worst case dan average case, di mana n adalah jumlah elemen dalam array. Namun, dalam best case, baik Bubble Sort maupun Insertion Sort memiliki kompleksitas waktu O(n), karena tidak ada perbandingan atau pergeseran yang dilakukan jika array sudah terurut.

Sebagai catatan, kedua algoritma ini termasuk dalam kategori algoritma pengurutan dengan kompleksitas waktu yang lebih tinggi. Untuk dataset yang sangat besar, algoritma pengurutan seperti Quick Sort atau Merge Sort biasanya lebih disukai karena memiliki kompleksitas waktu yang lebih baik, yaitu O(n log n).

# Analisis Algoritma Pencarian Rute Terpendek (TSP) dan Dijkstra:

# TSP (Traveling Salesman Problem):
Worst Case: TSP memiliki kompleksitas waktu eksponensial, sehingga tidak ada solusi efisien yang diketahui untuk kasus terburuknya. Jumlah iterasi dalam TSP adalah (n-1)!, di mana n adalah jumlah node dalam grafik. Jadi, jumlah permutasi yang mungkin sangat besar dan meningkat secara eksponensial dengan pertambahan node. Oleh karena itu, tidak ada kasus terburuk yang spesifik untuk TSP.
Best Case: Dalam TSP, tidak ada kasus terbaik yang spesifik karena setiap iterasi memeriksa semua permutasi yang mungkin. Namun, jika ada batasan atau struktur tertentu dalam grafik yang memungkinkan eliminasi sejumlah permutasi, itu bisa menjadi kasus terbaik.
Average Case: Tidak ada kasus rata-rata yang spesifik untuk TSP karena kompleksitas waktu eksponensial membuat sulit untuk memperkirakan jumlah iterasi secara pasti. Namun, dalam beberapa kasus, teknik optimasi atau heuristik yang cerdas dapat menghasilkan solusi yang baik secara efisien secara rata-rata.

# Dijkstra:
Worst Case: Dalam Dijkstra, jika grafik tidak memiliki batasan terkait bobot, maka dalam kasus terburuk semua node akan dikunjungi dan semua edge akan diuji, menghasilkan kompleksitas waktu O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah edge dalam grafik. Jadi, ketika jumlah edge mendekati V^2 atau ketika grafik terhubung lengkap, ini bisa menjadi kasus terburuk.
Best Case: Dalam Dijkstra, ketika hanya ada satu node dalam grafik atau ketika start node dan end node sama, maka Dijkstra akan menghasilkan solusi dengan kompleksitas waktu O(1). Ini adalah kasus terbaik karena tidak ada perluasan pencarian yang perlu dilakukan.
Average Case: Rata-rata, Dijkstra memiliki kompleksitas waktu O((V + E) log V). Namun, jika grafik memiliki struktur tertentu seperti grafik acyclic atau grafik yang sangat terhubung, maka beberapa operasi dapat dihindari dan kompleksitas waktu dapat berkurang.

Dalam kedua algoritma ini, kompleksitas waktu dipengaruhi oleh ukuran grafik dan struktur grafik itu sendiri. Dalam kasus terbaik, di mana tidak ada perluasan pencarian yang diperlukan, algoritma dapat menyelesaikan dengan cepat. Namun, dalam kasus terburuk, algoritma memeriksa semua kemungkinan dan membutuhkan waktu yang signifikan. Analisis lebih lanjut tentang kasus-kasus khusus dan struktur grafik yang mungkin terjadi dapat memberikan wawasan lebih lanjut tentang kinerja algoritma ini.
