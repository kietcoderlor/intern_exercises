name = input("Nhập tên: ")        
weight = float(input("Cân nặng: "))
height = float(input("Chiều cao: "))
 
bmi = weight / (height * height)
print(f"Chào {name}, BMI của bạn là {bmi:.1f}")
