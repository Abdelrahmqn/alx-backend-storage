#!/usr/bin/env python3
"""schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """iterates over the school based on the topic"""
    return list(mongo_collection.find({"topics": topic}))
