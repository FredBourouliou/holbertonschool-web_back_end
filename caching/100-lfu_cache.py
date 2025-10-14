#!/usr/bin/env python3
""" LFUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}
        self.access_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

                for k in self.access_order:
                    if k in lfu_keys:
                        lfu_key = k
                        break

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.access_order.remove(lfu_key)
                print("DISCARD: {}".format(lfu_key))

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.access_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
