class Catalogue:

    products = []
    def __init__(self, name):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, letter):
        products_listed = []
        for product in Catalogue.products:
            if product[0] == letter:
                products_listed.append(product)
        return products_listed


    def __repr__(self):
        sorted_products = sorted(Catalogue.products)
        string = f"Items in the {self.name} catalogue:"

        for i in range(len(sorted_products)):
            string += f"\n{sorted_products[i]}"
        return string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
