import itertools

def parse_input(f):
    lines = f.read().split("\n")
    return [int(x) if x.isdigit() else 0 for x in lines ]

def calories_list(input_list):
    L = [list(g) for _, g in itertools.groupby(input_list, key=lambda x: x == 0)]
    res = [sum(x) for x in L if x]
    res.sort(reverse=True)
    return res

with open("input.txt","r") as f:
    L = parse_input(f) 
    print(f"Top: {calories_list(L)[0]}")
    print(f"Top 3: {sum(calories_list(L)[0:3])}")
