class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            print(stk)
            match c:
                case '+':
                    val2 = stk.pop()
                    val1 = stk.pop()
                    stk.append(val1 + val2)
                case '-':
                    val2 = stk.pop()
                    val1 = stk.pop()
                    stk.append(val1 - val2)
                case '*':
                    val2 = stk.pop()
                    val1 = stk.pop()
                    stk.append(val1 * val2)
                case '/':
                    val2 = stk.pop()
                    val1 = stk.pop()
                    stk.append(int(val1 / val2))
                case _:
                    stk.append(int(c))
        return stk.pop()

        
