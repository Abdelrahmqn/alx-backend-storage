#!/usr/bin/env python3
"""0. Writing strings to Redis
"""
import random
import uuid
import redis
import typing
import uuid
from typing import Callable
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times the method is called"""
    key = method.__qualname__

    @functools.wraps(method)
    def inc(self, *args, **kwargs):
        """Function to increment the count of method calls"""
        self._redis.incr(key)   # Increment Redis key corresponding to method
        return method(self, *args, **kwargs)

    return inc


class Cache:
    """Cach class
    """

    def __init__(self):
        """ redis obj
            create a connection and flush the db
        """
        self._redis = redis.Redis()
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

    def get(self, key: str, fn: typing.Optional[Callable]) -> typing.Any:
        """
        """
        val = self._redis.get(key)
        if val is None:
            return None
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """
        calls the get method to str
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """to int
        """
        return self.get(key, fn=lambda d: int(d))
