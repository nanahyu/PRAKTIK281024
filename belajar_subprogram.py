def mencari_luas_lingkaran(jari-jari):
	luas_lingkaran = 3.14 *jari-jari*jari-jari
	return luas_lingkaran

def mencari_luas_persegi_panjang(panjang,lebar):
	luas_persegi_panjang = panjang*lebar
	return luas_persegi_panjang

persegi_panjang_pertama=mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

lingkaran_pertama=mencari_luas_lingkaran
print(lingkaran_pertama)