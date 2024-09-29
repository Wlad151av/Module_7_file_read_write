from pprint import pprint
class Product:
    def __init__(self,nam,wgt,cat):
        self.name = nam
        self.weight = wgt
        self.category = cat
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
class Shop:
    __file_name = "products.txt"
    def __init__(self):
        fname = open(self.__file_name, 'a')
        fname.write('')
        fname.close()
    def get_products(self):
        product_list = []
        self.fname = open(self.__file_name, 'r')
        str_ = self.fname.read()
        self.fname.close()
        return str_


    def add(self, *products):
        list_ = []
        str_ = self.get_products().split('\n')
        for _str in str_:
            list_.append(_str.split(', ')[0])
        for p in products:  # перебираем объекты класса Product
            if p.name not in list_:
                self.fname = open(self.__file_name, 'a')
                self.fname.write(str(p)+'\n')
                self.fname.close()
            else:
                print(f"Продукт {p.name} уже есть в магазине")



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
