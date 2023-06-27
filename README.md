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
