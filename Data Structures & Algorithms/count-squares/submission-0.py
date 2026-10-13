class CountSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)
        self.xs = set()

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])]+=1
        self.xs.add(point[0])

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for xx in self.xs:
            if xx==px:
                continue
            ll = abs(px-xx)
            yy = py-ll
            res += self.points[(xx, yy)]*self.points[(xx, py)]*self.points[(px, yy)]

            yy = py+ll
            res += self.points[(xx, yy)]*self.points[(xx, py)]*self.points[(px, yy)]
        return res
