class Solution:
    def check_if_koko_can_eat(self, piles, h, k):
        for pile in piles:
            time_to_eat = math.ceil(pile / k)
            h -= time_to_eat
            if h < 0:
                return 0

        return k if h >= 0 else 0

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        
        current_k = max(piles)
        l = 1
        r = current_k - 1
        while l <= r:
            mid = (r + l) // 2
            print(mid)
            new_k = self.check_if_koko_can_eat(piles, h, mid)
            if new_k and new_k < current_k:
                current_k = new_k
                r = mid - 1
            else:
                l = mid + 1
        return current_k