class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = []

    def get(self, key: int) -> int:
        index = self._get_index(key)
        if index != None:
            val = self.cache.pop(index)[key]
            self.cache.append({key:val})
            return val
        return -1
        

    def _get_index(self,key):
        for i,j in enumerate(self.cache):
            if key in j:
                return i

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)
        if index != None:
            self.cache.pop(index)
        if len(self.cache) >= self.cap:
                self.cache.pop(0)
        self.cache.append({key:value})


        
        
