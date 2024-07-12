# Bai 1
dien_tich = [9.224, 43.35, 12.04, 9.96, 10.09]
dan_so = [247100, 333300, 266800, 420900, 318000]
mat_do_dan_so = []
for i in range(0, len(dan_so), 1):
    a = dan_so[i]
    b = dien_tich[i]
    c = a/b
    mat_do_dan_so.append(c)
quan = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
for i in range(0, len(quan), 1):
    print(quan[i], ":" , mat_do_dan_so[i])
# Bai 2
print("Mat do dan so trung binh: ", sum(mat_do_dan_so)/len(quan))
