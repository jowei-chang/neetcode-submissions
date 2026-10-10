class Solution:
    def checkValidString(self, s: str) -> bool:
        upper = 0
        lower = 0
        for ss in s:
            if ss=="(":
                upper += 1
                lower += 1
            elif ss==")":
                upper -= 1
                lower -= 1
            else:
                upper += 1
                lower -= 1

            if lower<0: lower=0
            if upper<0: return False

        return lower==0