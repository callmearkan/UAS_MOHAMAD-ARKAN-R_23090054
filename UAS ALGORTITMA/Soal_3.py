class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' ditambahkan ke dalam antrian.")

    def dequeue(self):
        if len(self.antrian) > 0:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' dihapus dari antrian.")
            return pesanan
        else:
            print("Tidak ada pesanan dalam antrian untuk dihapus.")
            return None

    def tampilkan_antrian(self):
        if len(self.antrian) > 0:
            print("Antrian saat ini:", self.antrian)
        else:
            print("Antrian kosong.")

if __name__ == "__main__":
    antrian_restoran = AntrianRestoran()
    
    antrian_restoran.enqueue("Pesanan 1")
    antrian_restoran.enqueue("Pesanan 2")
    antrian_restoran.enqueue("Pesanan 3")
    
    antrian_restoran.tampilkan_antrian()
    antrian_restoran.dequeue()
    antrian_restoran.tampilkan_antrian()
    
    
    antrian_restoran.dequeue()
    antrian_restoran.dequeue()
    antrian_restoran.dequeue()  

    antrian_restoran.tampilkan_antrian()
