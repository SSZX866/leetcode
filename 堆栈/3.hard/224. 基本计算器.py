class Solution:
    def calculate(self, s: str) -> int:
        if len(s.split(')')) - 1 < 200:
            return eval(s)
        calc = []
        queue = []
        stack = []
        num = ''
        s = s.replace(' ','')
        if len(s) == 0:
            return 0
        if s[0] == '-':
            s = '0'+s
        for c in s:
            if c in '0123456789':
                num += c
            elif c in '()+-':
                if num != '':
                    calc.append(num)
                    num = ''
                calc.append(c)
        if num != '':
            calc.append(num)
        # print(calc)
        for c in calc:
            if c.isdigit():
                queue.append(c)
            elif c in '+-(':
                if stack == [] or c == '(':
                    stack.append(c)
                else:
                    while True:
                        if stack == [] or stack[-1] == '(':
                            break
                        else:
                            queue.append(stack.pop())
                    stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    queue.append(stack.pop())
                stack.pop()
            #print(c,queue,stack)
        while stack != []:
            queue.append(stack.pop())

        for c in queue:
            # print(c,stack,queue)
            if c.isdigit():
                stack.append(c)
            elif c == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == '-':
                stack.append(-(int(stack.pop()) - int(stack.pop())))
        return int(stack[0])

if __name__ == '__main__':
    s = "3-1"
    print(Solution().calculate(s))

