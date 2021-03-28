from itertools import permutations, product

n = 8
nplets = {}
lst = list(aapl_minute_closes)

for e in product("10", repeat=n):
    nplets[''.join(e)] = {"0":0, "1":0}

#print(nplets)

def get_type(lst, i):
    ans = ''
    for i2 in range(n):
        ans += numeric_compare(lst[i-n+i2-1], lst[i-n+i2])
    return ans

def numeric_compare(n1, n2):
    return "1" if n1 < n2 else "0"

for i,e in enumerate(lst):
    if (i < n):
        continue
    t = get_type(lst, i)
    current = numeric_compare(lst[i-1], lst[i])
    nplets[t][current] += 1

nplets_percentage = {key:abs(1-nplets[key]['0']/nplets[key]['1']) for key in nplets.keys()}
for key in sorted(nplets_percentage.keys()):
    if (nplets_percentage[key] > 0.20):
        print(key, nplets_percentage[key])
print()

for key in sorted(nplets.keys()):
    print(key, nplets[key])
