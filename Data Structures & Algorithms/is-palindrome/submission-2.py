class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^A-Za-z0-9]+', '', s)
        if cleaned == '':
            return True
        a = 0
        b = len(cleaned) - 1
        while(b != 0 or a != len(cleaned) - 1):
            if cleaned[a].lower() != cleaned[b].lower():
                return False
            else:
                b -= 1 
                a += 1

        return True