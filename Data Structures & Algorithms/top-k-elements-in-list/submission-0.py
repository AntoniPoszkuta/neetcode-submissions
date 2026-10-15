from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        sort = [[] for _ in range(len(nums) + 1)]

        for key, value in dic.items():
            sort[value].append(key)

        counter = len(sort) - 1

        output = []

        while k > 0 and counter >= 0:
            for val in sort[counter]:
                output.append(val)
                k -= 1
                if k == 0:
                    break
            counter -= 1


        return output