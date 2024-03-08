from dao.CustomerDAO import CustomerDAO
from dao.ProductDAO import ProductDAO
from dao.CartDAO import CartDAO
from dao.OrderDAO import OrderDAO
from exception.CustomerNotFoundException import CustomerNotFoundException

def main():
    print("\nWelcome to Ecommerce Application!!!")

    try:
        while True:
            print("\nSelect your Preference:")
            print("Press\n1. Register Customer\n2. Create Product\n3. Delete Product\n4. Add To Cart\n5. View Cart\n6. "
                  "Place Order\n7. View Customer Orders\n8. Stop\n")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                c = CustomerDAO()
                cust_id = c.registerCustomer()

                if cust_id != -1:
                    print("\nCustomer created Successfully!!!\n")
                    print(f"Your Customer Id: {cust_id}")
                else:
                    print("\nSorry! Could not complete your request! Please Try Again!")

            elif choice == 2:

                name = input("Enter the Product Name: ")
                price = float(input("Enter the price of the Product: "))
                description = input("Enter the Product Description: ")
                stockQuantity = int(input("Enter the Stock Quantity of the Product: "))

                data = (name, price, description, stockQuantity)
                p = ProductDAO()
                product_id = p.createProduct(data)

                if product_id != -1:
                    print("\nProduct created Successfully!!!\n")
                    print(f"Product Id: {product_id}")
                else:
                    print("\nSorry! Could not complete your request! Please Try Again!")

            elif choice == 3:
                product_id = int(input("Enter the Product Id to delete: "))
                p = ProductDAO()
                p.deleteProduct(product_id)

            elif choice == 4:
                customerId = int(input("Enter your Customer Id: "))
                flag = CustomerDAO().checkCustomerId(customerId)

                if flag is not None:
                    products = ProductDAO().getAllProducts()

                    if products is None:
                        print("Sorry!No Products Available")
                    else:

                        headers = ["Product Id", "Name", "Price", "Description", "Product Quantity", ]

                        header_row = "|".join(f"{header:<27}" for header in headers)
                        print(header_row)
                        print("-" * len(header_row))

                        # Print data rows
                        for row in products:
                            data_row = "|".join(f"{str(item):<27}" for item in row)
                            print(data_row)

                        c = CartDAO()
                        while True:
                            productId = int(input("\nEnter the Product Id: "))
                            quantity = int(input("Enter the Quantity you want: "))

                            c.addToCart(customerId, productId, quantity)

                            cart_choice = input("\nDo you want to add another product ? Yes/No: ")
                            if cart_choice.lower() != "yes":
                                break
                else:
                    raise CustomerNotFoundException(customerId)

            elif choice == 5:
                customerId = int(input("Enter your Customer Id: "))
                flag = CustomerDAO().checkCustomerId(customerId)
                if flag is not None:
                    c = CartDAO()
                    rows = c.getAllFromCart(customerId)

                    if len(rows) > 0:
                        print("\nYour Cart")
                        print("*********\n")

                        headers = ["Product Id", "Name", "Price", "Quantity"]
                        header_row = "|".join(f"{header:<27}" for header in headers)
                        print(header_row)
                        print("-" * len(header_row))

                        # Print data rows
                        for row in rows:
                            data_row = "|".join(f"{str(item):<27}" for item in row)
                            print(data_row)
                    else:
                        print("\nYou have no products in your cart!!!")
                else:
                    raise CustomerNotFoundException(customerId)

            elif choice == 6:
                customerId = int(input("Enter your Customer Id: "))
                flag = CustomerDAO().checkCustomerId(customerId)

                if flag is not None:
                    cartItems = CartDAO().getAllFromCart(customerId)

                    if len(cartItems) != 0:
                        street = input("Enter your Street Name: ")
                        city = input("Enter your City Name: ")
                        state = input("Enter your state Name: ")
                        pincode = input("Enter the pincode: ")

                        data = (customerId, street, city, state, pincode)
                        o = OrderDAO()
                        order = o.placeOrder(data)

                        if order[0] != -1:
                            print("\nOrder created Successfully!!!\n")
                            print(f"Your Order Id: {order[0]}")
                            print(f"Total Price: {order[1]}")
                        else:
                            print("\nSorry! Could not place your order! Please Try Again!")
                    else:
                        print("\nAdd products to your cart to place an Order!!!!")
                else:
                    raise CustomerNotFoundException(customerId)

            elif choice == 7:
                customerId = int(input("Enter your Customer Id: "))
                flag = CustomerDAO().checkCustomerId(customerId)

                if flag is not None:
                    o = OrderDAO()
                    rows = o.getOrdersByCustomer(customerId)

                    if len(rows) > 0:
                        print("\nYour Orders:\n")
                        headers = ["Order Id", "Order Date", "Total Price"]

                        header_row = "|".join(f"{header:<20}" for header in headers)
                        print(header_row)
                        print("-" * len(header_row))

                        # Print data rows
                        for row in rows:
                            data_row = "|".join(f"{str(item):<20}" for item in row)
                            print(data_row)
                    else:
                        print("\nYou haven't placed any order so far!")
                else:
                    raise CustomerNotFoundException(customerId)
            else:
                print("\n******************  Thank You using the application!!!  ******************")
                break

    except CustomerNotFoundException as e:
        print(e)


if __name__ == "__main__":
    main()
