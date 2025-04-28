#!/usr/bin/env python3
"""
Module for MongoDB operations with PyMongo - Schools by topic
"""
from typing import List


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    
    Args:
        mongo_collection: The pymongo collection object
        topic (str): The topic searched
        
    Returns:
        List of schools having the specified topic
    """
    schools = list(mongo_collection.find({"topics": topic}))
    return schools 