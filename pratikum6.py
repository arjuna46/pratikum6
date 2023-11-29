def tambah(nama, nilai):
    data_mahasiswa.append({"nama": nama, "nilai": nilai})

def tampilkan():
    for mahasiswa in data_mahasiswa:
        print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [mahasiswa for mahasiswa in data_mahasiswa if mahasiswa['nama'] != nama]

def ubah(nama, nilai):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = nilai
            break  

data_mahasiswa = []

tambah("Alice", 85)
tambah("Bob", 90)
tambah("Charlie", 78)

tampilkan()

hapus("Bob")

tampilkan()

ubah("Charlie", 82)

tampilkan()
