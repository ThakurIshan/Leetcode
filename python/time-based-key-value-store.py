class TimeMap:

    def __init__(self):
        self.x = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.x[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.x[key]
        if not data:
            return ""
        for i, j in reversed(data):
            if j <= timestamp:
                return i
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
