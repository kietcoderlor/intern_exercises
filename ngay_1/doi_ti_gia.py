ti_gia = float(input("Nhập tỉ giá (1 USD = ? VND): "))

print("1. VND → USD")
print("2. USD → VND")
opt = input("Chọn hướng đổi (1 hoặc 2): ")

sum = float(input("Nhập số tiền cần đổi: "))

if opt == "1":
    res = sum / ti_gia
    print(f"{sum:,.0f} VND = {res:.2f} USD")
elif opt == "2":
    res = sum * ti_gia
    print(f"{sum:.2f} USD = {res:,.0f} VND")
else:
    print("Lựa chọn không hợp lệ")
