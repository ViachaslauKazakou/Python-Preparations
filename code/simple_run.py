s = '["123","456"]'
result_list = s.strip('[]').split(',')
result_list = [item.strip('"') for item in result_list]
# print(result_list)



s = '["123","456"]'
result_list = [item.strip().strip('"') for item in s.strip('[]').split(',')]
cleared_list = '[' + ', '.join(f'"{item}"' for item in result_list) + ']'
print(cleared_list)
res =  list(map(str, cleared_list.strip('[]').split(',')))
print(res)

import re
s = '["123","456"]'
result_list = re.findall(r'"(.*?)"', s)
print(result_list)