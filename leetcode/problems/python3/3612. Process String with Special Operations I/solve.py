class Solution:
    def processStr(self, s: str) -> str:
        isRev = False
        result = ""
        for c in s:
            if c == "*":
                if isRev:
                    result = result[1:]
                else:
                    result = result[:-1]
            elif c == "#":
                result *= 2
            elif c == "%":
                isRev = not isRev
            else:
                if isRev:
                    result = c + result
                else:
                    result += c

        if isRev:
            result = result[::-1]

        return result
