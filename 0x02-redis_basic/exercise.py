#!/usr/bin/env python3
"""0. Writing strings to Redis
"""
import random
import uuid
from redis import Redis
import typing
import uuid


class Cache:
    """Cach class
    """

    def __init__(self):
        """ redis obj
            create a connection and flush the db
        """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, float, bytes, int]) -> str:
        """
        args: data.
        returns: str.
        store method should; generate a random key (uuid),
        stores the input data inside Redis using the random key
        then returns the key.
        """
        my_key = str(uuid.uuid4())

        self._redis.set(my_key, data)
        return my_key

    def get_str(self, key: str, fn: typing.callable) -> str:
        """
        """
        data_format = str(fn)

        return str(data_format)

    def get_int(self, key: str, fn: typing.callable) -> int:
        """
        """
        data_format = int(fn)
        return int(data_format)
