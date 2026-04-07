from collections import OrderedDict

class TimeMap:
    """
    Inutiion:
    - Keep a dict in the for Dict[string]OrderedDict[int]string
    - To set an element; simply set the key to the value in the form dict = { "key": { 1: "value" }}
    - From the example above; each key will have a dict that has timestamps as the key and the value as the value of the parent key passed. 
    -


    kv = {
        "love": {
            10: "high",
            20: "low"

            }
    } 
    """


    def __init__(self):
      self.kv = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []

        self.kv[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        key_length = len(self.kv[key])
        equal = None
        lesser = None

        for i in range(key_length - 1, -1, -1):
            prev_t, prev_v = self.kv[key][i]
            if prev_t == timestamp:
                equal = prev_v 
                break

            if prev_t <= timestamp:
                lesser = prev_v
                break
            
        return equal or lesser or ""