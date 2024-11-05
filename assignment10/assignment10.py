#1
# txt = open("/workspaces/pythonLab112315180/assignment10/hello.txt", "r")
# dict = {}
# for i in txt.read().split():
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# txt.close()
# out = open("out", "w")
# for i, count in dict.items():
#     out.write(f"{i}: {count}\n")
# out.close()
#2
# out = open("out", "w")
# l=["hello.txt","hello1.txt"]
# for i in l:
#     f=open(i,"r")
#     out.write(f.read()+ "\n")
#3
# txt = open("hello.txt", "r")
# a = "abc"
# out = open("out", "w")
# lines = txt.readlines()
# for line in lines:
#     if a in line:
#         out.write(line)
# txt.close()
# out.close()
#4
import os
a = os.path.expanduser("~")
b = os.path.join(a, "sub")
c = os.path.join(a, "sub1")
os.makedirs(b, exist_ok=True)
os.makedirs(c, exist_ok=True)
files = os.listdir(b)
for i in files:
    so = os.path.join(b, i)
    dest = os.path.join(c, i)
    try:
        src = open(so, 'rb')
        print(src)
        dest = open(dest, 'wb')
        dest.write(src.read())
        src.close()
        dest.close()
    except Exception as e:
        print("Error copying", i, ":", e)