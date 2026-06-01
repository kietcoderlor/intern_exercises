doan_van = input("Nhập đoạn văn: ")

tan_suat = {}
for tu in doan_van.split():
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")
