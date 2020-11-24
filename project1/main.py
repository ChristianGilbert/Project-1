from os import system
from datetime import datetime
from json import load, dump

def view_menu():
	system("cls")
	menu = """
	APLIKASI KONTAK KITA BERSAMA
	[A] - PENDAFTARAN SISWA
	[B] - DAFTAR SISWA
	[C] - CARI SISWA BERDASARKAN NAMA
	[I] - TENTANG SEKOLAH
	[Q] - KELUAR
	"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def create_id_contact():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_contact)+1
	id_contact = str("%4d%02d%02d-C%03d" % (year, month, hari, counter))
	return id_contact

def print_data_contact(id_contact = None, all_fields = False):
	if id_contact != None and all_fields == False:
		print(f"""
		-DATA DITEMUKAN-
	ID \t: {id_contact}
	Nama \t:{data_contact[id_contact]["nama"]}
	Telp \t:{data_contact[id_contact]["telp"]}
	Tanggal Lahir \t:{data_contact[id_contact]["tanggal lahir"]}
	Jenis Kelamin \t:{data_contact[id_contact]["jenis kelamin"]}
			""")
	elif all_fields == True:
		for id_contact in data_contact:
			nama = data_contact[id_contact]["nama"]
			telp = data_contact[id_contact]["telp"]
			tanggal_lahir = data_contact[id_contact]["tanggal lahir"]
			jenis_kelamin = data_contact[id_contact]["jenis kelamin"]
			print(f"ID:{id_contact}\tNAMA:{nama}\tTELP:{telp}\tTANGGAL LAHIR:{tanggal_lahir}\tJENIS KELAMIN:{jenis_kelamin}")

def add_to_contact():
	print_header("-MEMASUKKAN DAFTAR KONTAK BARU-")
	nama = input("NAMA\t:")
	telp = input("TELP\t:")
	tanggal_lahir = input("TANGGAL LAHIR\t:")
	jenis_kelamin = input("JENIS KELAMIN\t:")

	user_ans = input("Tekan Y untuk menyimpan(Y/N) : ")

	if verify_ans(user_ans):
		id_contact = create_id_contact()
		print("Menyiman Data ...")
		data_contact[id_contact] = {
			"nama" : nama,
			"telp" : telp,
			"tanggal lahir" : tanggal_lahir,
			"jenis kelamin" : jenis_kelamin
		}
		save_data_apps()
		print("Data Tersimpan")
	else:
		print("Data batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")


def print_contact():
	print_header("-SEMUA KONTAK-")
	if len(data_contact) == 0:
		print("<BELUM ADA KONTAK YANG DISIMPAN>")
	else:
		print_data_contact(all_fields=True)
	input("Tekan ENTER untuk kembali ke MENU")


def searching_by_name(contact):
	for id_contact in data_contact:
		if data_contact[id_contact]["nama"] == contact:
			print_data_contact(id_contact=id_contact)
			return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def get_id_contact_from_name(contact):
	for id_contact in data_contact:
		if data_contact[id_contact]["nama"] == contact:
			return id_contact

def searching_by_id(id_contact):
	if id_contact in data_contact:
		print_data_contact(id_contact=id_contact)
		return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def find_contact():
	print_header("-CARI KONTAK-\n")
	nama = input("Nama Kontak Yang Dicari : ")
	result = searching_by_name(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		add_to_contact()
	elif char == "B":
		print_contact()
	elif char == "C":
		find_contact()

def load_data_apps():
	with open(file_path, 'r') as document:
		data_contact = load(document)
	return data_contact

def save_data_apps():
	with open(file_path, 'w') as document:
		dump(data_contact, document)


file_path = 'data.json'
data_contact = None
stop = False

data_contact = load_data_apps()

while not stop:
	view_menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)