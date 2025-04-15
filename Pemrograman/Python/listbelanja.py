#list belanja
listbelanja = []
ditambahkan = []

while True:
    print("Daftar Belanja \n1. Tambahkan Barang \n2. Lihat Catatan \n3. Hapus Barang \n4. Ganti Urutan \n5. Hapus Selururh Daftar \n6. Keluar")
    opsi =input("Pilih salah satu opsi: ")

    if opsi == "1":
        barangbaru = input("Masukan nama barang: ")
        listbelanja.append(barangbaru)
        ditambahkan.append(barangbaru)
        print(barangbaru + " telah ditambahkan")
        a = input("Tekan Enter untuk melanjutkan...")

    elif opsi == "2":
        if not listbelanja:
            print("Tidak ada barang apapun saat ini")
        else:
            for i, barang in enumerate(listbelanja, 1):
               print(f"{i}. {barang}")
        a = input("Tekan Enter untuk melanjutkan...")

    elif opsi == "3":
        if not listbelanja:
            print("Tidak ada barang apapun saat ini")
        else:
            hapus = input("Pilih barang yang ingin dihapus (bisa menggunakan nama atau indeks): ")
            if hapus.isdigit():
                indeks = int(hapus) - 1
                if indeks >= 0:
                    listbelanja.pop(indeks)
                else:
                    print("Barang tidak ada di daftar")
            else:
                if hapus in listbelanja:
                    listbelanja.remove(hapus)
                else:
                    print("Barang tidak ada di daftar")

        a = input("Tekan Enter untuk melanjutkan...")

    elif opsi == "4":
        print("1. Berdasarkan alfabet \n2. Berdasarkan waktu ditambahkan")
        sorttype = input("Pilih opsi: ")

        if sorttype == "1":
            listbelanja = sorted(ditambahkan)
        elif sorttype == "2":
            listbelanja = ditambahkan.copy()
        a = input("Tekan Enter untuk melanjutkan...")

    elif opsi == "5":
        confirm = input("Apakah anda yakin? (y/N): ")
        if confirm.upper() == "Y":
            listbelanja = []
            ditambahkan = []
            print("Daftar berhasil dihapus")
            a = input("Tekan Enter untuk melanjutkan...")
        else:
            print("Daftar tidak dihapus")
            a = input("Tekan Enter untuk melanjutkan...")

    elif opsi == "6":
        break
    else:
        print("Opsi invalid/salah, coba lagi")
        a = input("Tekan Enter untuk melanjutkan...")
        continue


