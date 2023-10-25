def load_categories():
    return [{
        'id': 1,
        'name': "Mobile"
    }, {
        'id': 2,
        'name': "Tablet"
    }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': "iPhone 15 Pro Max",
        'price': 20000000,
        'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_5.png"
    }, {
        'id': 2,
        'name': "Samsung Galaxy S23",
        'price': 23000000,
        'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/a/samsung-galaxy-s23-ultra.png"
    }, {
        'id': 3,
        'name': "Xiaomi Redmi Note 12",
        'price': 5000000,
        'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-redmi-note-12-8gb-128gb_1__1_2.png"
    }, {
        'id': 4,
        'name': "OnePlus Nord",
        'price': 7000000,
        'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/e/d/edobfefy-doc-quy.jpg"
    }, {
        'id': 5,
        'name': "TECNO POVA",
        'price': 4000000,
        'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/t/e/tecno-pova-5_2_.png"
    }, {
        'id': 6,
        'name': "OPPO Find N3 Flip",
        'price': "Liên hệ",
        'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/o/p/oppo-find-n3-flip_8_.png"
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products
