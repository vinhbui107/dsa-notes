class Solution:
    """
    https://leetcode.com/problems/evaluate-reverse-polish-notation/

    >>> solution = Solution()
    >>> solution.evalRPN(["2","1","+","3","*"])
    9
    """

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for item in tokens:
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(item))

        return stack.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
