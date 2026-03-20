the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def converter(num):
    return "woko" if num == 0 else "wiki"

   
print(list(map(converter, the_bools)))

