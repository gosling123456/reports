# big = list(input('开始符(用","隔开):'))
# small = list(input('字母表(用","隔开):'))
# print('文法(格式为A -> a|aB|....),按"#"退出:')
# point1 = {}
# while 1:
#     ipt = input('')
#     if ipt == '#':
#         break
#     key,value = ipt.split(' -> ')[0],ipt.split(' -> ')[-1].split('|')
#     point1[key] = value

point = {'S': ['a', 'aA'], 'A': ['a', 'aA', 'cA', 'bB'], 'B': ['a', 'b', 'c', 'aB', 'bB', 'cB']}  # 文法
# print(point)
# print(point1)
big = list(set([i for i in str(point) if 'A' <= i <= 'Z']))+['Y']
# print(big)
small = list(set([i for i in str(point) if 'a' <= i <= 'z']))
"""文法转NFA"""
NFA_result = []
for key, value in point.items():
    dic = []  # 所有读取一个值到另外状态的字典的列表
    for i in value:  # 遍历point的一个value
        if len(i) == 1:
            dic.append({i[0]: 'Y'})  # 将转移函数加到列表里
        else:
            dic.append({i[0]: i[-1]})  # 将转移函数加到列表里
    di = {}
    for _ in dic:  # 值相同的字典合并
        for k, v in _.items():
            di.setdefault(k, []).append(v)
    NFA_result.append({key: di})  # 格式为{key1:{key2:value2}},其中key1是一个状态，key2是读入的字符,value2是转移状态的集合
# print(NFA_result)

print('五元组形式输出结果为：')
print('M = (%s,%s,$,S,Y)' % (str(big).replace('[', '(').replace(']', ')'),str(small).replace('[', '(').replace(']', ')')))
for i in NFA_result:
    for key, value in i.items():
        for j, k in value.items():
            print('$(' + key + ',' + j + ') = ', str(k).replace('[', '{').replace(']', '}'))
