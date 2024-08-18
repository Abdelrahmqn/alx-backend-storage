#!/usr/bin/env python3
"""list the documents"""


def list_all(mongo_collection):
    """list all"""
    return list(mongo_collection.find())
