class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tokens = deque(tokens)


        while tokens:
            cur = tokens.popleft()
            if cur not in "+-*/":
                stack.append(cur)
            else:
                a2 = stack.pop()
                a1 = stack.pop()
           
                if cur == "+":
                    stack.append(int(a1)+int(a2))
                elif cur == "-":
                    stack.append(int(a1)-int(a2))
                elif cur == "*":
                    stack.append(int(a1)*int(a2))
                else:
                    stack.append(int(a1)/int(a2))
        
        return int(stack[0])

            

