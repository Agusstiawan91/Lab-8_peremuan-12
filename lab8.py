class DaftarNilaiMahasiswa:
    def __init__(self):
        # Menyimpan data mahasiswa dalam bentuk list
        self.mahasiswa = []

    def tambah(self, nama, nilai):
        # Method untuk menambah data mahasiswa
        self.mahasiswa.append({'nama': nama, 'nilai': nilai})
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        # Method untuk menampilkan semua data mahasiswa
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for mhs in self.mahasiswa:
                print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        # Method untuk menghapus data mahasiswa berdasarkan nama
        for mhs in self.mahasiswa:
            if mhs['nama'] == nama:
                self.mahasiswa.remove(mhs)
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama):
        # Method untuk mengubah data mahasiswa berdasarkan nama
        for mhs in self.mahasiswa:
            if mhs['nama'] == nama:
                nilai_baru = input(f"Masukkan nilai baru untuk {nama}: ")
                mhs['nilai'] = nilai_baru
                print(f"Data nilai mahasiswa {nama} berhasil diubah.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")


# Contoh penggunaan program
if __name__ == "__main__":
    daftar_nilai = DaftarNilaiMahasiswa()

    # Menambah data
    daftar_nilai.tambah('Budi', 80)
    daftar_nilai.tambah('Siti', 90)
    daftar_nilai.tambah('Aji', 85)

    # Menampilkan data
    daftar_nilai.tampilkan()

    # Mengubah data
    daftar_nilai.ubah('Budi')

    # Menampilkan data setelah perubahan
    daftar_nilai.tampilkan()

    # Menghapus data
    daftar_nilai.hapus('Siti')

    # Menampilkan data setelah penghapusan
    daftar_nilai.tampilkan()
