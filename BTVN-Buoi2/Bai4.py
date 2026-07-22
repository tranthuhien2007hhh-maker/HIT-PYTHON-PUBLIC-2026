n = int(input("Nhập số tiền : "))
chai = n//28
tongchai = chai
vo = chai
while vo>=3:
    doi = vo//3
    tongchai += doi
print(f"Số chai bia có thể uống được là:", tongchai)