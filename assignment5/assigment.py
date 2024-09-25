s = {1, 2, 3}
s_list = list(s)
psl = [[]]  
for e in s_list:
    new = [sub + [e] for sub in psl]
    psl.extend(new)
print([set(sub) for sub in psl])