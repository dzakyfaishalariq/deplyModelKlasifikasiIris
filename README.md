# Dokumentasi API Klasifiksi bunga iris
untuk mengakses API klasifikasi bunga iris cukup kunjungi link API berikut ini. `catatan harus download **postman**`
karena untuk mengakses api ini lebih enak menggunkan hal tersebut karena dapat mengkases secara leluasa dari api yang bersangkutan. berikut link untuk mendwonload postman: [postman](https://www.postman.com/) jikalau bingun cara menggunakan lakukan akses link youtube untuk mempelajari postman tersebut : [link pembelajaran](https://www.youtube.com/watch?v=bBUNP2YVIQA)

- pada pertama kali ini kita melakukan reques untuk mengkases dengan menggunkana  tool GET pada link akses API nya dengan sintaks berikut ini:
```
GET:https://klasifikasi-iris.onrender.com/
```
pada tampilan diatas akan menampilkan tampilan utama dengan bentuk seperti berikut.

```
{
    "Pembuat": "Dzaky Faishalariq",
    "Tema": "Klasifikasi Bunga Iris"
}
```
Dilihat dari tampilanya pertama kali kita akan disampaikan beberapa informasi JSON yang mana ada pembuat dan tema yang ada pada API tersebut.

- penggunaan POST untuk mengkases klasifikasiIRSI atau menggunakan model yang akan di klasifikasi nantinya oleh kita dengan memasikan kode berikut.
```
POST:https://klasifikasi-iris.onrender.com/klasifikasiIRIS
```
pada penggunaan diatas kita nanti akan menggunakan postman dan akses pada body nya dan kelik raw dan tukar format penulisan JSON. Sebelum mengkelik send/panggil kita akan menuliskan isian yang akan kita riques untuk kita predikis nantinya pada model klasifikasiIRIS ini berikut contoh sintaks nya:

```
{
    "sL": ...,
    "sW": ...,
    "pL": ...,
    "pW": ...
}
```
keterangan:
- sL = kita harus mengisi panjang untuk sepal length yang mana nilai harus bertype float
- sW = kita harus mengisi panjang untuk sepal width yang mana nilai harus bertype float
- pL = kita harus mengisi panjang untuk petal length yang mana nilai harus bertype float
- pW = kita harus mengisi panjang untuk petal width yang mana nilai harus bertype float

sesudah kita mengisi parameter yang akan kita kirim untuk reques post maka kita kelik send dan akan memberikan tampilan seperti berikut

```
{
    "predikis": {
        "akurasi": 0.7954522371292114,
        "class": "Iris Setosa",
        "inisial": {
            "0": "Iris Setosa",
            "1": "Iris Versicolor",
            "2": "Iris Verginica"
        },
        "predikisIndex": 0
    }
}
```
maka dia akan memberikan beberapa informasi seperti
- akurasi
- class
- inisial
- prediksi index

jikalau ada kekurangan harap berikan tanggapan anda terhadap API ini semoga nanti dapat di perbaiki dan diperbarui.
Salam dari saya...