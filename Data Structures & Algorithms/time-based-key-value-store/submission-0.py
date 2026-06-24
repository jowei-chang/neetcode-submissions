class TimeMap:

    def __init__(self):
        self.table={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = [[value,timestamp]]
        else:
            self.table[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.table:
            for val, timstep in reversed(self.table[key]):
                if timstep <= timestamp:
                    return val
        return ""
