# Bai 1
quan = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dan_so = [247100, 333300, 266800, 420900, 318000]
# Bai 2
print("Most populated dist. : ", dan_so.index(max(dan_so)))
print("Least populated dist. : ", dan_so.index(min(dan_so)))
# Bai 3
print("Most populated dist. : ", quan[dan_so.index(max(dan_so))])
print("Least populated dist. : ", quan[dan_so.index(min(dan_so))])

