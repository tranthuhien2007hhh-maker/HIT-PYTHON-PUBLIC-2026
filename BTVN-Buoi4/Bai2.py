chuyen_doi_nhiet_do = lambda c: c * 9 / 5 + 32

kiem_tra_chan_le = lambda x: "Chẵn" if x % 2 == 0 else "Lẻ"

tinh_tien_tip = lambda hoa_don, tip: hoa_don * tip / 100

rut_gon_ten = lambda ten: ten.upper()


print(chuyen_doi_nhiet_do(30))
print(kiem_tra_chan_le(15))
print(tinh_tien_tip(500000,10))
print(rut_gon_ten("trần thị b"))