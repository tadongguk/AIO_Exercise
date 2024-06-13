def count(string, text):
    count = 0
    for i in string:
        if text in i:
            count += 1
    return count


string = "smiles"
# LẤY RA CÁC KÝ TỰ KHÔNG TRÙNG NHAU
a = set(string)
# ĐẾM SỐ LẦN XUẤT HIỆN CỦA KÝ TỰ TRONG CHUỖI

# IN RA SỐ LẦN XUẤT HIỆN CỦA TỪNG KÝ TỰ TRONG CHUỖI
for i in a:
    print(f"{i} : {count(string, i)}")
