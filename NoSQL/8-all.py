#!/usr/bin/env python3
"""
Module for MongoDB operations with PyMongo
"""
from typing import List


def list_all(mongo_collection) -> List:
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection: The pymongo collection object
        
    Returns:
        List of all documents or empty list if no documents
    """
    documents = list(mongo_collection.find())
    return documents 