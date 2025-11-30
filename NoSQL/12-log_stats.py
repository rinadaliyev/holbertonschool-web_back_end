#!/usr/bin/env python3
"""TASK 12"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient(host="127.0.0.1", port=27017)
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for i in methods:
        count = collection.count_documents({"method": i})
        print(f"\tmethod {i}: {count}")

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")
