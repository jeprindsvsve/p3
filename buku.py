class Buku:

  def __init__(self, judul, penulis="tidak diketahui", tahun_terbit=None):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
 
  def info(self):
    print(f"Judul         : {self.judul}")
    print(f"Penulis       : {self.penulis}")
    print(f"tahun_terbit  : {self.tahun_terbit}")

buku1 = Buku("Dasar Pemrograman Python", "Fajar Jeprianto", 2006)
buku2 = Buku("Struktur Data", tahun_terbit=2007)
buku3 = Buku("Basis Data", "Rian Rahmat Hidayat", 2000)
        
buku1.info()
buku2.info()
buku3.info()

