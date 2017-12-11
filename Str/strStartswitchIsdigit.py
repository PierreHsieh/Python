# conding=utf-8


s1 = '100'
result = s1.startswith('1')
print(result)
# True

s2 = '200'
result = s2[0].isdigit()
print(result)
# True

result = s2[0:2].isdigit()
print(result)
# True

s3 = '1 name 90'
result = s3.split()
print(result)
# ['1', 'name', '90']
