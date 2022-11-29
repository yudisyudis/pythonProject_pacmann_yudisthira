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
    total_harga = int(0)
    total_belanjaan = int(0)

    def __init__(self):
        print(f"Selamat Datang Customer {self.id} di Toko Online")
        wel = input("siap memulai belanja? (Y/N) ")
        if wel.lower() == 'y':
             self.add_item()
        else:
            pass


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
            cek2 = input(f'tulis 1 untuk nambah barang, 2 untuk merubah barang, 3 untuk hapus barang: ')
            if cek2.lower() == '1':
                return self.add_item()
            elif cek2.lower() == '2':
                return self.update_item()
            elif cek2.lower() == '3':
                return self.delete_item()
            else:
                print("keyword salah")
                return self.add_item()
        else:
            print("keyword salah")
            return self.add_item()

    def update_item(self):
        cek = input(f'tulis 1 untuk ubah nama, 2 untuk ubah jumlah, 3 untuk ubah harga: ')
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
        elif cek.lower() == "2":
            nama = input("masukkan barang yang jumlahnya mau diganti: ")
            jumlah2 = int(input("masukkan jumlah baru: "))
            self.belanjaan[nama] = [jumlah2, self.harga]
            print(f'daftar belanja baru anda {self.belanjaan}')
            cek4 = input("apakah data sudah final? (Y/N): ")
            if cek4.lower() == "y":
                return self.check_item()
            elif cek4.lower() == "n":
                cek5 = input(f'tulis 1 untuk nambah barang, 2 untuk rubah barang, 3 untuk hapus barang: ')
                if cek5.lower() == '1':
                    return self.add_item()
                elif cek5.lower() == '2':
                    return self.update_item()
                elif cek5.lower() == '3':
                    return self.delete_item()
                else:
                    print("keyword salah")
        elif cek.lower() == "3":
            nama = input("masukkan barang yang harganya mau diganti: ")
            harga2 = int(input("masukkan harga baru: "))
            self.belanjaan[nama] = [self.jumlah, harga2]
            print(f'daftar belanja baru anda {self.belanjaan}')
            cek6 = input("apakah data sudah final? (Y/N): ")
            if cek6.lower() == "y":
                return self.check_item()
            elif cek6.lower() == "n":
                cek7 = input(f'tulis 1 untuk nambah barang, 2 untuk rubah barang, 3 untuk hapus barang: ')
                if cek7.lower() == '1':
                    return self.add_item()
                elif cek7.lower() == '2':
                    return self.update_item()
                elif cek7.lower() == '3':
                    return self.delete_item()
                else:
                    print("keyword salah")
        else:
            print("keyword yang dimasukkan salah")
            return self.update_item()

    def delete_item(self):
        cek = input(f'hapus semua? (Y/N): ')
        if cek.lower() == 'y':
            return self.reset()
        else:
            nama = input(f'masukkan nama barang yang hendak dihapus: ')
            del self.belanjaan[nama]
            print(f'daftar belanja baru anda {self.belanjaan}')
            return self.check_item()

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

    def reset(self):
        self.belanjaan.clear()
        print("belanjaan anda telah direset")
        return self.add_item()











