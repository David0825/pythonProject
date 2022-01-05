import json

# 存储数据 json json.dump json.load
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# 使用json.dump()存储数据
with open(filename, 'w') as f:
    json.dump(numbers, f)

# 使用json.load()读取数据到内存
with open(filename) as f:
    numbers = f.read()
print(numbers)
