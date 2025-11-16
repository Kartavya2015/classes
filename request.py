test_dic = {'I': 2,'study': 2, 'in': 1, 'vibgyor': 2, 'high': 5, 'school': 5}
print("Orignal Dictionary:"+str(test_dic))
constant = 2
res = 0
for key in test_dic:
    if test_dic[key] == constant:
        res += 1
print("Number of keys with value",constant,"is: "+str(res))