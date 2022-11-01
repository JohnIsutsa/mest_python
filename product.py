from abc import ABC, abstractmethod

class Product():
    product_id = 0
    name = ''
    sku  = 0
    quantity = 0
    image_url = ''

    def __init__(self, product_id, name, sku, quantity, image_url):
        self.product_id = product_id
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.image_url = image_url

list = []

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def edit_product(self, product: Product):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self, product, product_image):
        pass

    @abstractmethod
    def delete_product(self, product):
        pass

class ProductManager(ProductAbstract):
    def create_product(self):
        prod_id = input('Enter product ID:')
        prod_name  = input('Enter product name:')
        prod_sku = input('Enter product SKU:')
        prod_quantity = input('Enter product quantity:')
        prod_url = input('Enter product URL:')

        list.append(Product(prod_id, prod_name, prod_sku, prod_quantity, prod_url))

    def edit_product(self):
        prod_id = input("Enter product ID:")
        new_name = input("Enter new name:")
        for obj in list:
            if obj.product_id == prod_id:
                obj.name = new_name
                print(f"Name: {obj.name}\t SKU: {obj.sku} Quantity: {obj.quantity}\t Image: {obj.image_url}")       
    
    def get_product_by_id(self, product_id):
        for obj in list:
            if obj.product_id == product_id:
                print(f"Name: {obj.name}\t SKU: {obj.sku} Quantity: {obj.quantity}\t Image: {obj.image_url}")

    def get_all_products(self):
        for obj in list:
            print(f"Prod ID: {obj.product_id}\t Name: {obj.name}\t SKU: {obj.sku} Quantity: {obj.quantity}\t Image: {obj.image_url}")

    def upload_product_image(self, product: Product):
        print('Product image uploaded')
    
    def delete_product(self):
        print('Product deleted from the database')

#List to store product objects
list.append(Product(1001, 'Pens', 238950, 500, 'http://image_url.com' ))
list.append(Product(1002, 'Books', 2389040, 400, 'http://book_url.com'))
list.append(Product(1003, 'Pencils', 34920343, 50, 'http://pencil_url.com'))

product_manager = ProductManager()
# product_manager.create_product()
product_manager.get_product_by_id(1001)
product_manager.get_all_products()
# product_manager.edit_product()
product_manager.upload_product_image(list[0])
product_manager.delete_product()

for obj in list:
    print(obj.name)









# product = Product('Pens')
# product_manager = ProductManager() 

# product_manager.create_product(product)
# product_manager.edit_product(product)
    