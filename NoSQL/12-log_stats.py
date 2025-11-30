#!/usr/bin/env python3
"""
12-log_stats.py
Script that provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def main():
    """ adhslkfhbasdlfk jh dkflhs dgshf"""
    client = MongoClient()  # default connection to localhost:27017
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})
    if total_logs == 0:
        print("Collection nginx is empty")
        return
    print(f"{total_logs} logs")

    # HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET requests to /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()
