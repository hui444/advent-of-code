# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     list.append(line)
list = []

f = open("input.txt", "r")
f = f.read().split("\n")
list = [int(i) for i in f]

count = 0
for i in range(len(list)):
    if i == 0: 
        continue
    if int(list[i-1]) < int(list[i]) :
        count += 1

print(count)