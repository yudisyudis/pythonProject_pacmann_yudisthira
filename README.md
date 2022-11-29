# Super Cashier
Sebuah project personal yang dikembangkan untuk menyelesaikan course modul Python di Pacmann Academy

## Background Project

Aplikasi **Super Cashier** dikembangkan untuk mempermudah transaksi dari customer supermarket atau tempat-tempat belanja lainnya, aplikasi ini menghubungkan antara customer dan tempat belanja sehingga customer dapat dengan mudah melakukan aktifitas belanja langsung dengan memanfaatkan berbagai macam fitur seperti memilih barang yang hendak dibeli, jumlah pembelian, dan harga per itemnya. Aplikasi **Super Cashier** pun kemudian dapat menyediakan ringkasan pembayaran yang perlu diselesaikan oleh customer setelah mereka yakin telah menyelesaikan proses pemilihan barang belanja.

## Feature Requirements

Dalam pengembangannya, aplikasi **Super Cashier** memiliki beberapa permintaan fitur yang perlu ditindaklanjuti diantaranya:

1. Customer memperoleh customer id setiap mengakses class transaksi.
2. Customer bisa melakukan input nama, jumlah, dan harga barang yang ingin dibeli
3. Customer bisa melakukan edit data baik mengedit nama, jumlah, maupun harga barang yang telah diinput sebelumnya
4. Customer dapat membatalkan daftar barang yang telah diinput sebelumnya, baik membatalkan salah satu barang, maupun membatalkan seluruh daftar belanjaannya
5. Setelah Customer selesai menginput barang, terdapat fitur review apakah ada pesanan yang salah atau tidak, dilengkapi pula dengan total harga per item yang dibeli
6. Jika Customer selesai mereview belanjaannya, maka dilanjutkan dengan menampilkan total harga seluruh belanjaan, dengan secara otomatis sudah menerapkan diskon yang diatur sesuai dengan kebijakan Toko

## Flowchart

![image](https://user-images.githubusercontent.com/91902011/204457324-75b01784-8b17-4cf0-9bdb-c48f141acc53.png)

Secara garis besar, alur proses algoritma aplikasi **Super Cashier** dapat dilihat pada gambar di atas. 

- Aplikasi dimulai dengan melakukan instantiasi Class transaksi yang secara otomatis mengenerate customer id
- Kemudian aplikasi secara otomatis menawarkan customer apakah hendak memulai proses belanja, jika iya, maka customer dipersilahkan menginput nama, jumlah, dan harga barang
- Kemudian muncul halaman konfirmasi, apakah pesanan sudah final atau belum
  - Jika sudah, aplikasi langsung mengarahkan ke rekap pesanan
    + Lalu setelah selesai direkap, aplikasi langsung mengarahkan ke total harga seluruh belanjaan dengan juga menerapkan diskonnya
    + Pembayaran dan proses aplikasi selesai
  - Jika belum, maka aplikasi menawarkan apakah customer hendak mengganti, menambah, atau menghapus data
    + Jika customer hendak menambahkan barang, maka akan kembali dipersilahkan menambahkan nama, jumlah, dan harga barang
    + Jika customer hendak mengganti barang, maka akan masuk ke alur edit data yang terdiri dari mengubah nama, jumlah, atau harga barang, lalu setelah itu aplikasi akan mengarah ke halaman review belanjaan kembali.
    + Jika customer hendak menghapus daftar barang, maka akan diminta untuk memilih hendak menghapus salah satu atau seluruh daftar belanjaan, dan setelah itu aplikasi kembali ke halaman awal

## Code and Feature Explanation

1. Bagian awal code berisi import modul, deklarasi Class Transaksi, deklarasi variabel globa, serta tampilan awal aplikasi yang berupa pesan selamat datang, serta pilihan untuk memulai kegiatan belanja

```
from random import randint

class Transaksi:
    id = randint(10000, 99999)
    belanjaan = {}
    nama = str
    jumlah = str
    harga = int
    total = []
    gabung_harga = []
    gabung_jumlah = []
    total_harga = int
    total_belanjaan = int
    
    def __init__(self):
        print(f"Selamat Datang Customer {self.id} di Toko Online")
        wel = input("siap memulai belanja? (Y/N) ")
        if wel.lower() == 'y':
             self.add_item()
        else:
            pass
``` 
Penjelasan:
- modul random digunakan untuk mengenerate random number untuk keperluan customer id
- deklarasi Class Transaksi dengan variabel global berupa id yang digunakan untuk identitas customer, nama, jumlah, harga dideklarasikans ecara global agar bisa diakses dan diedit oleh berbagai method yang tersedia. Lalu dideklarasikan pula dictionary belanjaan untuk menampung data belanjaan yang terdiri dari nama barang sebagai key dan values berupa list yang berisi jumlah dan harga barang. Kemudian ada dua variabel yaitu total_harga dan total_belanjan, total_harga kelak akan diisi hasil perkalian jumlah dan harga per barang, melambangkan total harga per nama barang, sementara total_belanjaan merupakan penjumlahan seluruh total_harga per nama barang atau melambangkan jumlah total yang perlu dibayarkan oleh customer
- pada bagian bawah disediakan fitur selamat datang dan pertanyaan untuk memulai proses belanja atau tidak

2. Bagian kedua yaitu method add_item yang berfungsi untuk menambahkan nama, jumlah, dan harga barang yang hendak dibeli:
```
    def add_item(self):
        nama = input("mau beli apa: ")
        jumlah = int(input("masukkan jumlah pembelian: "))
        harga = int(input("masukkan harga per itemnya: "))
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        self.belanjaan[self.nama] = [self.jumlah, self.harga]
        self.gabung_harga.append(self.harga)
        self.gabung_jumlah.append(self.jumlah)
        print(f'belanjaan anda {self.belanjaan}')
        cek = input("apakah data sudah final? (Y/N): ")
        if cek.lower() == "y":
            return self.check_item()
        elif cek.lower() == "n":
            cek2 = input(f'tulis 1 untuk nambah barang, 2 untuk rubah barang, 3 untuk hapus barang: ')
            if cek2.lower() == '1':
                return self.add_item()
            elif cek2.lower() == '2':
                return self.update_item()
            elif cek2.lower() == '3':
                return self.delete_item()
            else:
                print("keyword salah")
```               
Penjelasan:
- nama, jumlah, dan harga digunakan untuk menampung input yang diberikan oleh customer
- nilai dari nama, jumlah, dan harga lalu digunakan untuk membuat format sturktur dictionary bernamaa belanjaan, dengan nama sebagai key-nya
- setelah format dictonary tergenerate, lalu muncul prompt yang menanyakan finalisasi data.
  + jika sudah final maka akan langsung dilanjutkan ke fungsi check_item
  + jika belum final, maka customer diberikan 3 pilihan yaitu menambah belanjaan, merubah belanjaan, atau menghapus belanjaan. Jika memilih menambah belanjaan, maka akan kembali diarahkan ke method add_item, sedangkan merubah dan menghapus belanjaan akan mengarahkan ke method lain.
  
3. Bagian ketiga, method update, berfungsi ketika pada bagian kedua Customer memutuskan untuk mengubah daftar belanjaan:
```
    def update_item(self):
        cek = input(f'tulis 1 untuk ubah barang, 2 untuk ubah jumlah, 3 untuk ubah harga: ')
        if cek.lower() == "1":
            nama2 = input("masukkan barang yang mau diganti: ")
            nama3 = input("masukkan barang pengganti: ")
            for i in self.belanjaan:
                if i == nama2:
                    self.belanjaan[nama3] = self.belanjaan[i]
                    del self.belanjaan[nama2]
                    print(f'daftar belanja baru anda {self.belanjaan}')
                    cek2 = input("apakah data sudah final? (Y/N): ")
                    if cek2.lower() == "y":
                        return self.check_item()
                    elif cek2.lower() == "n":
                        cek3 = input(f'tulis 1 untuk nambah barang, 2 untuk rubah barang, 3 untuk hapus barang: ')
                        if cek3.lower() == '1':
                            return self.add_item()
                        elif cek3.lower() == '2':
                            return self.update_item()
                        elif cek3.lower() == '3':
                            return self.delete_item()
                        else:
                            print("keyword salah")

                    break
                else:
                    continue
```
Penjelasan:
Method update memiliki 3 cabang fungsi yang teknis code-nya mirip, yaitu mengganti nama, jumlah, atau harga barang, dengan mekanisme sebagai berikut:
- melakukan input nama/jumlah/harga mana yang hendak diganti
- memasukkan nama/jumlah/harga barang pengganti
- nama/jumlah/harga yang baru kemudian di-assign ke dictionary yang merupakan variabel global sehingga bisa langsung diakses di tiap method dan diganti salah satu dari key atau value nya sesuai dengan yang diinginkan user.
- daftar belanjaan baru hasil update kemudian ditampilkan dan logika pemrograman finalisasi barang seperti yang terdapat di bagian dua kembali diterapkan.

4. Bagian keempat, method delete, berfungsi ketika pada bagian kedua, cystomer memutuskan untuk menghapus barang belanjaan:
```
    def delete_item(self):
        cek = input(f'hapus semua? (Y/N): ')
        if cek.lower() == 'y':
            return self.reset()
        else:
            nama = input(f'masukkan nama barang yang hendak dihapus: ')
            del self.belanjaan[nama]
            print(f'daftar belanja baru anda {self.belanjaan}')
            return self.check_item()
```

Penjelasan:
- Pada method delete, terdapat dua branching tambahan, apakah Customer hendak menghapus seluruh daftar belanjaan atau hanya salah satunya saja:
  + Jika Customer memutuskan menghapus seluruh daftar belanjaan, maka akan diarahkan ke method lain yaitu reset yang akan menghapus seluruh daftar belanjaan.
  + Jika Customer memutuskan tidak menghapus semuanya, makan akan diminta memasukkan nama barang yang hendak dihapus, nama yang pada dictionary belanjaan berfungsi sebagai key, akan menghapus secara spesifik anggota dictionary belanjaan sesuai dengan key yang diinputkan Customer. Setelah menghapus salah satu barang belanjaan selesai, maka akan ditampilkan daftar belanja terbaru dan diarahkan ke fungsi check_item

5. Bagian kelima, method check_item, yang akan berfungsi ketika Customer memutuskan daftar belanjaan sudah final pada bagian kedua:
```
    def check_item(self):
        for i in self.belanjaan:
            total_harga = self.belanjaan[i][0] * self.belanjaan[i][1]
            self.belanjaan[i].append(total_harga)
        print(f'total harga tiap item yang anda beli: {self.belanjaan}')
        cek = input("ingin lanjut ke ringkasan pembayaran? (Y/N): ")
        if cek.lower() == "y":
            return self.ringkasan()
        else:
            return self.pilihan()
```
Penjelasan:
- Setelah Customer memutuskan bahwa daftar belanjaan sudah final, maka akan dijalankan method check_item yang berisikan fungsi untuk mengalikan jumlah dan harga barang tiap jenis barangnya kemudian total harga barang tersebut dimasukkan ke dalam dictionary sehingga value dictionary ditahap ini bertambah menjadi 3 jenis item yaitu jumlah, harga, dan total harga barang. 
- Dictionary yang telah terupdate tersebut kemudian ditampilkan untuk Customer, dan Customer diberi pilihan kembali apakah ingin lanjut menuju tahap ringkasan belanja atau ada sesuatu yang ingin dilakukan kembali berkenaan dengan proses belanja
  + Jika memilih lanjut ringkasan, maka akan diarahkan ke method ringkasan
  + Jika memilih tidak lanjut, maka akan diarahkan ke method pilihan
 
6. Bagian keenam, method ringkasan, yang akan dijalankan ketika Customer memilih ringkasan di bagian kelima:
```
    def ringkasan(self):
        for i in self.belanjaan:
            self.total_belanjaan += self.belanjaan[i][2]
        if self.total_belanjaan > 200000:
            self.total_belanjaan = self.total_belanjaan - (0.05*self.total_belanjaan)
            return print(f'total belanjaan anda seharga: Rp.{self.total_belanjaan}')
        elif self.total_belanjaan > 300000:
            self.total_belanjaan = self.total_belanjaan - (0.08 * self.total_belanjaan)
            return print(f'total belanjaan anda seharga: Rp.{self.total_belanjaan}')
        elif self.total_belanjaan > 500000:
            self.total_belanjaan = self.total_belanjaan - (0.1 * self.total_belanjaan)
            return print(f'total belanjaan anda seharga: Rp.{self.total_belanjaan}')
        else:
            return print(f'total belanjaan anda seharga: Rp.{self.total_belanjaan}')
```
Penjelasan:
- Keitka customer memiih ringkasan, makan method ringkasan akan berjalan dengan menotalkan seluruh total harga di dictionary belanjaan dan menginputnya ke variabel global total_belanjaan dengan iterasi penjumlahan
- Setelah total_belanjaan dirampungkan, lalu dilakukan pengecekan diskon sesuai kebijakan Toko, dengan aturan total_belanjan di atas 200000 mendapatkan diskon 5%, di atas 300000 mendapatkan diskon 8%, dan di atas 500000 mendapatkan diskon 10%.
- Method ringkasan mengeluarkan nilai akhir berupa total harga belanjaan customer

7. Bagian ketujuh, method pilihan, yang aktif ketika pada bagian kelima Customer memilih untuk tidak dulu melanjutkan ke peringkasan daftar belanjaan:
```
    def pilihan(self):
        cek = input(f'tulis 1 jika ada yang diubah, 2 untuk batal belanja, 3 lanjut pembayaran: ')
        if cek.lower() == '1':
            return self.update_item()
        elif cek.lower() == '2':
            return self.reset()
        elif cek.lower() == '3':
            return self.ringkasan()
        else:
            print("keyword yang dimasukkan salah")
            return self.pilihan()
```
Penjelasan:
- Method pilihan menawarkan beberapa opsi untuk Customer yang belum mau merekap belanjaannya yaitu opsi untuk mengubah data belanjaan, membatalkan belanjaan, atau juga melanjutkan proses belanjan ke bagian total_pembayaran
  + Jika customer memilih mengubah data, maka akan diarahkan kembali ke method update_item
  + Jika customer memilih membatalkan belanja, maka akan diarahkan ke method reset
  + Jika customer memilih melanjutkan pembayaran, maka akan diarahkan ke method ringkasan
  
 8. Bagian kedelapan, method reset, yang akan aktif ketika Customer memilih membatalkan belanja di bagian keempat, atau ketujuh:
 ```
     def reset(self):
        self.belanjaan.clear()
        print("belanjaan anda telah direset")
        return self.add_item()
 ```
 Penjelasan:
 - Method reset berisikan built-in function clear() yang berguna untuk menghapus seluruh isi dictionary dalam hal ini dictionary belanjaan
