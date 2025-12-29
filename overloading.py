class  A:
    def __init__ (self, a):
        self.a = a
    def It (self, other):
        if (self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob1 is not less than ob2"
    def __eq__ (self, other):
        if (self.a==other.a):
            return "ob1 is equal to ob2"
        else:
            return "ob1 is not equal to ob2"
        
ob1 = A(5)
ob2 = A(10)
print("passed number:", ob1.a, ob2.a)
print(ob1.It(ob2))

ob3 = A(78876445767876787656765678767876787656787656765434567898765432123456789098765432345678909876543234567890)
ob4 = A(78876445767876787656765678767876787656787656765434567898765432123456789098765432345678909876543234567890)
print("passed number:", ob3.a, ob4.a)
print(ob3.__eq__(ob4))