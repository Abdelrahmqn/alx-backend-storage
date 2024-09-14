#!/usr/bin/env python3
"""0. Writing strings to Redis
"""
import random
import uuid
import redis
import typing
import uuid
from typing import Callable, Union, Optional
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


def call_history(method: Callable) -> Callable:
    """  """
    key = method.__qualname__
    inp = key + ":inputs"
    out = key + ":outputs"

    @functools.wraps(method)
    def wrapping_mthod(self, *args, **kwargs):
        """  """
        self._redis.rpush(inp, str(args))
        self._redis.rpush(out, str(data))
        data = method(self, *args, **kwargs)
        return data
    return wrapping_mthod


class Cache:
    """Cach class
    """

    def __init__(self):
        """ redis obj
            create a connection and flush the db
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, float, bytes, int]:
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


def replay(method: Callable):
    """
    display the history of calls
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    redis = method.__self__._redis

    count = redis.get(key).decode("utf-8")

    print("{} was called {} times:".format(key, count))

    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)

    ziped = list(zip(inputList, outputList))

    for a, b in ziped:
        attr, data = a.decode("utf-8"), b.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))
