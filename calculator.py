def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "لا يمكن القسمة على صفر!"
    return x / y

print("مرحبًا بك في الآلة الحاسبة!")
print("الخيارات:")
print("1. جمع")
print("2. طرح")
print("3. ضرب")
print("4. قسمة")

choice = input("اختر العملية (1/2/3/4): ")

try:
    num1 = float(input("أدخل الرقم الأول: "))
    num2 = float(input("أدخل الرقم الثاني: "))

    if choice == '1':
        print("النتيجة:", add(num1, num2))
    elif choice == '2':
        print("النتيجة:", subtract(num1, num2))
    elif choice == '3':
        print("النتيجة:", multiply(num1, num2))
    elif choice == '4':
        print("النتيجة:", divide(num1, num2))
    else:
        print("خيار غير صالح.")
except ValueError:
    print("يرجى إدخال أرقام صحيحة.")
