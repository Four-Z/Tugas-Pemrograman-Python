import string


class User():
    def __init__(self, user_name, tipe):
        self.__user_name = user_name
        self.__tipe = tipe

    @property
    def get_name(self):
        return self.__user_name

    @property
    def get_tipe(self):
        return self.__tipe


class Seller(User):
    def __init__(self, user_name, tipe):
        super().__init__(user_name, tipe)
        self.list_barang_jual = []
        self.__pemasukkan = 0

    def getName(self):
        return self.get_name

    def getPemasukan(self):
        return self.__pemasukkan

    def setPemasukan(self, pemasukkan):
        self.__pemasukkan = pemasukkan

    def tambah_product(self, produk, harga, stock, seller):
        temp = Product(produk, harga, stock, seller)
        self.list_barang_jual.append(temp)
        list_product.append(temp)

    def lihat_produk_jualan_saya(self):

        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        self.list_barang_jual.sort
        for product in self.list_barang_jual:
            # TODO : cetak tiap product dengan urutan alphabetical
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(
                f"{product.getNama_barang} {product.getHarga} {product.getStock}")
        print("-------------------------------------\n")

    def menu(self):
        print("\nSelamat datang", self.get_name)
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")
        print(f"Pemasukkan anda {self.__pemasukkan}")
        masukkan = input("Apa yang ingin Anda lakukan? ")
        return masukkan


# TODO : implementasikan class Buyer
class Buyer(User):
    def __init__(self, user_name, tipe, saldo):
        self._saldo = int(saldo)
        self._riwayat_beli = []
        super().__init__(user_name, tipe)

    def getName(self):
        return self.getName

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = int(saldo)

    def lihat_semua_produk(self):
        print("\nBerikut merupakan daftar produk di Dekpedia")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock  | Penjual ")
        print("-----------------------------------------------")
        for i in list_product:
            print(f"{i.getNama_barang} {i.getHarga} {i.getStock} {i.getSeller}")
        print("-----------------------------------------------\n")

    def beli_produk(self, nama_produk):
        saldo_now = self.get_saldo()
        check = True
        for i in list_product:
            if i.getNama_barang == nama_produk:
                check = False
                if i.getHarga <= saldo_now and i.getStock > 0:
                    i.setStock(i.getStock-1)
                    tempSaldo = saldo_now-i.getHarga
                    self.set_saldo(tempSaldo)
                    print(f"Berhasil membeli {nama_produk} dari {i.getSeller}")
                    self._riwayat_beli.append(i)
                    for j in list_user:
                        if j.getName() == i.getSeller:
                            j.setPemasukan(j.getPemasukan()+i.getHarga)
                elif i.getStock <= 0:
                    print("“Maaf, stok produk telah habis.")

                elif i.getHarga > saldo_now:
                    print(
                        f"Maaf, saldo Anda tidak cukup untuk membeli {nama_produk}")

        if check:
            print(
                f"Barang dengan nama {nama_produk} tidak ditemukan dalam Dekdepedia")

    def riwayat_beli(self):
        print("\nBerikut merupakan barang yang saya beli")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Penjual ")
        print("-----------------------------------------------")

        for i in self._riwayat_beli:
            print(f"{i.getNama_barang} {i.getHarga} {i.getSeller}")

    def menu(self):
        print("\nSelamat datang", self.get_name)
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")
        print(f"Saldo anda {self._saldo},")
        masukkan = input("Apa yang ingin Anda lakukan? ")
        return masukkan


class Product():
    def __init__(self, nama_barang, harga, stock, seller):
        self._nama_barang = nama_barang
        self._harga = int(harga)
        self._stock = int(stock)
        self._seller = seller

    @property
    def getNama_barang(self):
        return self._nama_barang

    @property
    def getHarga(self):
        return self._harga

    @property
    def getStock(self):
        return self._stock

    @property
    def getSeller(self):
        return self._seller

    def setStock(self, stock):
        self._stock = stock


def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """

    for user in list_user:
        if user.get_name == name:
            return user
    return None


def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name == name:
            return product
    return None


list_user = []
list_product = []


def main():
    while(True):
        print("\nSelamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah: ")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        pilih = input("Pilihan Anda: ")

        if (pilih == "1"):
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))

            print("Data akun: ")
            # TODO : implementasikan sign up
            for i in range(banyak_user):
                try:
                    data_user = input(str(i+1)+". ")
                    for j in list_user:
                        tipe, username = data_user.split()
                        if j.getName() == username:
                            print("Username sudah terdaftar.")
                            break

                    if 'SELLER ' in data_user:
                        tipe, username = data_user.split()
                        user = Seller(username, tipe)
                        list_user.append(user)
                    elif 'BUYER ' in data_user:
                        tipe, username, saldo = data_user.split()
                        if int(saldo) < 0 or not set(username).issubset(string.ascii_letters+string.digits+'-_'):
                            print("Akun tidak valid.")
                        else:
                            user = Buyer(username, tipe, saldo)
                            list_user.append(user)
                    else:
                        print("Akun tidak valid.")
                except:
                    print("Akun tidak valid.")

        elif (pilih == "2"):
            user_name_login = input("user_name : ")
            user_logged_in = get_user(user_name_login, list_user)
            # TODO : implementasikan log in
            if user_logged_in is None:
                print(
                    f"Akun dengan username {user_name_login} tidak ditemukan")
            elif user_logged_in.get_tipe == 'SELLER':
                print(
                    f"Anda telah masuk dalam akun {user_logged_in.get_name} sebagai {user_logged_in.get_tipe}")

                seller = user_logged_in
                while(True):
                    menu = seller.menu()

                    if menu == '1':
                        product = input("Masukkan data produk :")
                        produk, harga, stock = product.split()
                        seller.tambah_product(
                            produk, harga, stock, seller.get_name)

                    elif menu == '2':
                        seller.lihat_produk_jualan_saya()

                    elif menu == '3':
                        break

            elif user_logged_in.get_tipe == 'BUYER':
                print(
                    f"Anda telah masuk dalam akun {user_logged_in.get_name} sebagai {user_logged_in.get_tipe}")

                buyer = user_logged_in

                while(True):
                    menu = buyer.menu()

                    if menu == '1':
                        buyer.lihat_semua_produk()
                    elif menu == '2':
                        bought = input("Masukkan barang yang ingin dibeli: ")
                        buyer.beli_produk(bought)
                    elif menu == '3':
                        buyer.riwayat_beli()
                    elif menu == '4':
                        break

        elif (pilih == "3"):
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()


if __name__ == "__main__":
    main()
