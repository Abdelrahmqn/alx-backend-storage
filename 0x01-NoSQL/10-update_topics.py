#!/usr/bin/env python3
"""topics"""


def update_topics(mongo_collection, name, topics):
    """Updating the documents and topics."""
    update_doc = mongo_collection.update_many({"name": name},
                                              {"$set": {"topics": topics}})
    return update_doc
