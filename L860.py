# 860. 柠檬水找零
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0: return False
                five -= 1
                ten += 1
            else:
                if not (ten * 10 + five * 5 >= 15 and five != 0): return False
                ten -= 1
                five -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    ans = s.lemonadeChange([5, 5, 5, 10, 20])
    ans = s.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
    # ans = s.lemonadeChange([5, 5, 10, 10, 20])
    print(ans)
