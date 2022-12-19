class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if any(event2.count(x) > 0 for x in event1):
            return True
        h1, h2 = event1[0][:2], event1[1][:2]
        m1, m2 = event1[0][3:], event1[1][3:]
        h3, h4 =  event2[0][:2], event2[1][:2]
        m3, m4 = event2[0][3:], event2[1][3:]
        if h1 <= h3 <= h2 or h1 <= h4 <= h2:
            if h2 == h3:
                if m2 >= m3:
                    return True
                else:
                    return False
            return True
        if h3 < h2 <= h4 or h3 <= h1 <= h4:
            return True
