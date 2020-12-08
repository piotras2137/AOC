file="data.dat"
inputs = open(file, "r").read().splitlines()
index_dict = {i:(input[0:3],input[4],input[5:]) for i,input in enumerate(inputs)}
def count_acc(data):
  exc = 0
  acc = 0
  exc_lines = []
  while True:
    if exc in exc_lines:
      return acc
    exc_lines.append(exc)
    if exc not in data:
      return acc
    c,o,n = data[exc]
    if "jmp" == c:
      exc = eval(f"{exc} {o} {n}")
    elif "acc" == c:
      exc += 1
      acc = eval(f"{acc} {o} {n}")
    elif "nop" == c:
      exc += 1
print(count_acc(index_dict))