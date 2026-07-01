class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        x,y = point
        result =0

        for(col, row) , cnt in self.points.items():
            if row!=y or col==x:
                continue
            d = col-x
            count1 = self.points.get((x, y+d), 0) * self.points.get((col, y+d), 0)
            count2 = self.points.get((x, y-d), 0) * self.points.get((col,y-d), 0)
            result += (count1+count2)*cnt

        return result
        
