class Customer:
    def __init__(self, _fname, _lname):
        self.fname = _fname
        self.lname = _lname

    def sayName(self):
        print("Full NAME " + self.fname + " " + self.lname)


customer = Customer("Hassan", "Chaudhry")
customer.sayName()