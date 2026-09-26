class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if not position:
            return 0

        dic = {}
        for index, pos in enumerate(position):
            dic[pos] = (target - pos) / speed[index] 

        stack = []
        
        for number in sorted(dic.keys()):
            stack.append(dic[number])

        fleets = 1

        maxi = stack[-1]

        for _ in range(len(stack)):
            car = stack.pop()
            if car > maxi:
                maxi = car
                fleets += 1

        return fleets