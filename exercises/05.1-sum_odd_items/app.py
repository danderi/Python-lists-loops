my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    odd_nums = 0
    for i in list:
        if i%2 != 0:
            odd_nums += i
    return odd_nums

print(sum_odds(my_list))
