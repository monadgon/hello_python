nums = [11, 22, 33, 44, 55]
result = list(filter(lambda x: x%2 == 0, nums))
print(result)

# Like map, the result has to be explicitly converted to a list if you want to print it.