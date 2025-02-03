class dad:
    def phone(self):
        print("dad's phone")
class mom:
    def sweet(self):
        print("mom's sweet")
class son(dad,mom):
    def laptop(self):
        print("son's laptop")

ram=son()
ram.phone()
ram.sweet()
