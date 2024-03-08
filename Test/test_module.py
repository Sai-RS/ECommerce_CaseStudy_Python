import pytest
from exception.ProductNotFoundException import ProductNotFoundException
from dao.ProductDAO import ProductDAO
from dao.CartDAO import CartDAO
from dao.OrderDAO import OrderDAO

def test_product_not_found_exception():
    with pytest.raises(ProductNotFoundException) as info:
        ProductDAO().checkProductId(9)
    assert str(info.value) == 'No products available with this product id'

def test_create_product():
    data = ("Eraser", 5, "Smooth", 20)
    product_dao = ProductDAO()

    product_id = product_dao.createProduct(data)

    assert product_id > 0

def test_add_to_cart(capfd):
    cart_dao = CartDAO()
    cart_dao.addToCart(1,1,2)

    captured = capfd.readouterr()

    assert "Product Added to your cart!!!" in captured.out

def test_place_order():
    order_dao = OrderDAO()
    data = (1,"South","Chennai","Tamil Nadu",609100)
    order = order_dao.placeOrder(data)

    assert order[0] > 0