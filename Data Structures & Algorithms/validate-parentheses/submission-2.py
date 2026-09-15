class Solution:
    def isValid(self, s: str) -> bool:
        checkValidParentheses = []
        lookup = { '(' : ')', '{': '}', '[': ']'}
        for i in s:
            if i in lookup:
                checkValidParentheses.append(i)
            elif len(checkValidParentheses) > 0 and lookup[checkValidParentheses[-1]] == i:
                checkValidParentheses.pop()
            else:
                return False

        return len(checkValidParentheses) == 0