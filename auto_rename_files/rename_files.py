import os

# تحديد المسار للمجلد اللي فيه الملفات
folder_path = r"C:\Users\HP\Documents\Todo_app\my_files"

# الحصول على قائمة كل الملفات في المجلد
files = os.listdir(folder_path)

# ترتيب الملفات أبجدياً
files.sort()

# إعادة التسمية
for index, filename in enumerate(files):
    file_ext = os.path.splitext(filename)[1]
    new_name = f"file_{index+1}{file_ext}"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)
    print(f"Renamed: {filename} → {new_name}")

print("✅ تم إعادة تسمية الملفات بنجاح.")
