#даны строки s,ss,sss. заменить в строке s последнее вхождение строки ss на строку sss
s = input('введите первую строку').strip()
ss = input('введите ввторую строку').strip()
sss = input('введите третью строку').strip()

pos = s.rfind(ss)
if pos != -1:
    res = s[:pos] + sss + s[pos + len(ss):]
else:
    res = s
print(res)
