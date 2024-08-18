#!/usr/bin/env python3
"""insert many"""


def insert_school(mongo_collection, **kwargs):
    """insert a coll of documents."""
    insertion = mongo_collection.insert_one(kwargs)
    return insertion.inserted_id
