#!/usr/bin/env python3
"""
Module for providing enhanced stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides enhanced stats about Nginx logs stored in MongoDB.
    
    Displays:
    - Total logs
    - Methods count (GET, POST, PUT, PATCH, DELETE)
    - Status check count (path=/status)
    - Top 10 most present IPs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    
    # Count total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    
    # Count status checks
    status_checks = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_checks} status check")
    
    # Get top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    
    top_ips = list(logs_collection.aggregate(pipeline))
    
    print("IPs:")
    for ip_info in top_ips:
        ip = ip_info.get("_id")
        count = ip_info.get("count")
        print(f"    {ip}: {count}")


if __name__ == "__main__":
    log_stats() 