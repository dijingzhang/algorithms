# ( ) + -
def calculate(s: str) -> int:
      res, num, sign = 0, 0, 1
      stack = []
      if not s:
          return 0

      for char in s:
          if char == " ":
              continue
          elif char.isdigit():
              num = 10 * num + int(char)
          else:
              if char in "+-":
                  res += sign * num
                  num = 0
                  sign = 1 if char == "+" else -1
              elif char == "(":
                  stack.append(res)
                  stack.append(sign)
                  res = 0
                  sign = 1
              else:
                  res += sign * num
                  num = 0
                  res *= stack.pop()
                  res += stack.pop()
      res += sign * num
      return res
# * / + -
  def calculate2(s: str) -> int:
      n = len(s)
      stack = []
      pre_sign = "+"
      num = 0

      for i in range(n):
          if s[i] != ' ' and s[i].isdigit():
              num = num * 10 + ord(s[i]) - ord('0')
          if i == n - 1 or s[i] in "+-*/":
              if pre_sign == "+":
                  stack.append(num)
              elif pre_sign == "-":
                  stack.append(-num)
              elif pre_sign == "*":
                  stack.append(stack.pop() * num)
              else:
                  top = stack.pop()
                  if top < 0:
                      stack.append(-(-top//num))
                  else:
                      stack.append(top // num)
              pre_sign = s[i]
              num = 0
      return sum(stack)
