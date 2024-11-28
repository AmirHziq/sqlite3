from pymongo import MongoClient
import sqlite3
import pprint as pprint

sqlite_conn = sqlite3.connect("customer_order.db")
sqlite_cursor = sqlite_conn.cursor()

db_name = 'customer_order'
client = MongoClient("mongodb://localhost:27017/customer_order.db")


db = client.get_database(db_name)
movies = db.get_collection('product')

mongodb = client["productcol"]
review_collection = mongodb["product_review"]
review_collection.delete_many({})
'''
sqlite_cursor.execute("SELECT product_id, product_name FROM PRODUCTS")
products  = sqlite_cursor.fetchall()

for product in products:
    product_id , product_name = product
    reviews = review_collection.find({"product_id": product_id})
    print(f"Product: {product_name}")
    for review in reviews:
        print(f" - Review: {review['comment']} (Rating: {review['rating']})")
'''


#Insert data to collection
review_collection.insert_one({
    "review_id": "1",
    "customer_id": 101,
    "product_id": 101,
    "rating": 4.5,
    "comment": "Excellent product quality",
    "review_date": "2024-11-26"
})

#Print the collection data
print("MongoDB Data:")
for doc in review_collection.find():
    print(doc)

#Close the sql
sqlite_conn.close()
client.close()