#!/usr/bin/env python3
"""
This module provides a Cache class for storing data in Redis.
It allows storing strings, bytes, integers, and floats using
randomly generated keys.
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.

    Args:
        method: The method to be decorated.

    Returns:
        Callable: The wrapped method that increments the call count.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments call count and calls original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function.

    Args:
        method: The method to be decorated.

    Returns:
        Callable: The wrapped method that stores input/output history.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores inputs and outputs in Redis lists.
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Args:
        method: The method to replay the history for.
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__
    call_count = redis_instance.get(method_name)
    if call_count:
        call_count = int(call_count)
    else:
        call_count = 0
    print("{} was called {} times:".format(method_name, call_count))
    inputs = redis_instance.lrange(method_name + ":inputs", 0, -1)
    outputs = redis_instance.lrange(method_name + ":outputs", 0, -1)
    for inp, out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            method_name,
            inp.decode("utf-8"),
            out.decode("utf-8")
        ))


class Cache:
    """
    Cache class for storing data in Redis.
    Provides methods to store various data types with auto-generated keys.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance.
        Creates a Redis client connection and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data: The data to store. Can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis and optionally convert it.

        Args:
            key: The key to retrieve from Redis.
            fn: Optional callable to convert the data.

        Returns:
            The retrieved data, optionally converted by fn.
            Returns None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve a string from Redis.

        Args:
            key: The key to retrieve from Redis.

        Returns:
            The retrieved data as a UTF-8 string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer from Redis.

        Args:
            key: The key to retrieve from Redis.

        Returns:
            The retrieved data as an integer.
        """
        return self.get(key, fn=int)
