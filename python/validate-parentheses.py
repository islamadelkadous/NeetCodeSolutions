class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['(', '{', '[']:
                stk.append(c)
            elif len(stk) == 0:
                return 
            elif (c == ')' and stk.pop() != '('):
                return False
            elif (c == '}' and stk.pop() != '{'):
                return False
            elif (c == ']' and stk.pop() != '['):
                return False
            
        return len(stk) == 0

                
        
