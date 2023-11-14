Product:
    - name
    - description
    - image
    - images *
    - price
    - flag [sale, new, feature]
    - brand 
    - sku
    - reviews: *
        - user
        - rate
        - feedback
        - cration date

    
    - subtitle
    - quantity
brand: *
    - image
    - title
    - product_count
    - rate

orders:
- status[recieved, processed, shipped, deleted]
- code 
- order_time
- delivery_time
- sub_total
- dicount
- delivery_fee
- total
- delivery_location
- product
- brand
- price
- quantity
