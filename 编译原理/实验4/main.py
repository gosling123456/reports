# ##################################
# ##           实验1              ##
# ##################################
# """数据快测：
# 非终极符(大写字母,用英文逗号隔开,并用大括号括起来）：{A,B,C,S}
# 终极符(小写字母,用英文逗号隔开并用大括号括起来）：{a,b,c}
# 文法(一行输入，不同文法之间以"#"开始,"\n"结尾，用空格隔开，内部用 "|" 和 "->" 隔开）：
# 产生式1:
# #S->A
# 产生式2:
# #A->a|aB|aA|aC
# 产生式3:
# #B->b|bB
# 产生式4:
# #C->c|cC
#
# 开始符：a
# 存储文件名称：文法1
# 输入句子允许的最大长度：4
#
#
# 错误！初始符不能为终结符！！！
# 写入文件至 D:\Class\Core_course-main\编译原理\实验4\文法1.txt，此次共产生了0个句子
#
# 开始符：S
# 存储文件名称：文法2
# 输入句子允许的最大长度：4
# a
# ab
# abb
# abbb
# aa
# aab
# aabb
# aaa
# aaab
# aaaa
# aaac
# aac
# aacc
# ac
# acc
# accc
# 写入文件至D:\Class\Core_course-main\编译原理\实验4\文法2.txt，此次共产生了16个句子
#
# """
# import os
#
#
# def loop(string):
#     for i in range(len(string)):  # 遍历当前句子，判断其中是否含有非终极符
#         if string[i] in convert.keys():
#             for j in convert[string[i]]:  # 如果当前句子存在非终极符，就进行文法的推导
#                 # print(string)
#                 new_string = string[0:i] + j + string[i + 1:]  # 推到后产生的新句子
#                 # print(new_string)
#                 if len(new_string) > max_length:  # 判断句子长度是否合法，如果不合法就不再进行推导（因为继续推导不会更短）
#                     break  # 如果句子长度合法、且不含非终极符，那么久成功的产生了一个句子
#                 elif new_string.islower():
#                     f.write(new_string + '\n')  # 写入结果
#                     print(new_string)
#                     # print('')
#                     result.append(new_string)
#                 else:  # 如果句子长度合法、但是包含非终极符，那么就递归进行推导
#                     # print(new_string)
#                     loop(new_string)
#
#
# if __name__ == '__main__':
#     content = []
#     convert = {}
#     """存储文法"""
#     V = "V=" + input('非终极符(大写字母,用英文逗号隔开,并用大括号括起来）：') + '\n'
#     T = "T=" + input('终极符(小写字母,用英文逗号隔开并用大括号括起来）：') + '\n'
#     print('文法(一行输入，不同文法之间以"#"开始,"\\n"结尾，用空格隔开，内部用 "|" 和 "->" 隔开）：')
#     P = []
#     num = V.count(',') + 1
#     for i in range(num):  # 循环输入语法
#         print('产生式%d:' % (i + 1))
#         P.append(input() + '\n')
#     S = 'S=' + input('开始符：')
#     name = input('存储文件名称：')
#     f = open(name + '.txt', 'w', encoding='utf-8')
#     f.write(V)  # 写入非终极符
#     f.write(T)  # 写入终极符
#     f.write('P\n')  # 声明以下内容是产生式
#     for i in P:  # 写入产生式
#         f.write(i)
#     f.write(S)  # 写入开始符
#     f.write('\n\n利用上述文法，得到的结果是:\n\n')  # 写入结果声明
#
#     content = [V] + [T] + ['P\n'] + P + [S]
#     for i in content[3:-1]:  # 获取产生式中的语法信息，将其存储在convert字典中
#         key = i[1:-1][0]
#         value = i[1:-1][3:].split('|')
#         convert[key] = value
#     result = []
#     max_length = int(input('输入句子允许的最大长度：'))  # 设置最大长度（因为有些文法能产生无穷长度的句子）
#
#     string = content[-1][-1]  # 获取开始符S
#     #  print(string)
#     if string.islower():  # 如果开始符本身就是终极符，就需要进行异常处理
#         print('错误！初始符不能为终结符！！！')
#     else:
#         loop(string)  # 递归调用loop函数完成句子的产生
#     print("写入文件至%s，此次共产生了%d个句子" % (os.getcwd() + '\\' + name + '.txt', len(set(result))))  # 产生句子的总数




##################################
##           实验2              ##
##################################
"""数据快测：
输入状态转移函数，按“#”键结束
(q0,0)=q1
(q0,1)=q0
(q1,0)=q2
(q1,1)=q0
(q2,0)=q3
(q2,1)=q0
(q3,0)=q3
(q3,1)=q0
#
输入存储文件的名称：DFA识别以000结尾
输入起始符：q0
输入终态符：q3
输入句子:101000
Finished!
"""
# def DFA(beg, end):
#     next = beg
#     present = next
#     for i in string:
#         next = rule['(%s,%s)' % (present, i)]
#         # result.append('(%s,%s)=%s' % (present, i, next))
#         f.write('(%s,%s)=%s' % (present, i, next) + '\n')
#         present = next
#         if present == end:
#             return 0
#         return 1
#
#
# if __name__ == '__main__':
#     # F = 'q0'  # input('输入起始符：')
#     # E = 'q3'  # input('输入终态符：')
#     result = []
#     # rule = {'(q0,0)': 'q1', '(q0,1)': 'q0', '(q1,0)': 'q2', '(q1,1)': 'q0', '(q2,0)': 'q3', '(q2,1)': 'q0',
#     #         '(q3,0)': 'q3',
#     #         '(q3,1)': 'q0'}
#     # print(rule)
#     print('输入状态转移函数，按“#”键结束')
#     rule1 = []
#     while 1:
#         a = input()
#         if a == "#":
#             break
#         rule1.append(a)
#     if '' in rule1:
#         del rule1[rule1.index('')]
#         # print(rule1)
#     rule = {i.split('=')[0]: i.split('=')[-1] for i in rule1}
#     name = input('输入存储文件的名称：')
#     F = input('输入起始符：')
#     E = input('输入终态符：')
#     string = input('输入句子:')
#     f = open(name + '.txt', 'w', encoding='utf-8')
#     f.write(
#         'Q=%s' % str(sorted(list(set((rule.values()))))).replace('[', '{').replace(']', '}') + '\n')  # 写第一行，状态集合
#     f.write(
#         'A=%s' % str(sorted(list(set([int(i[1:-1].split(',')[-1]) for i in rule.keys()])))).replace('[',
#                                                                                                     '{').replace(
#             ']', '}') + '\n')  # 写第二行，字母表
#     f.write('T:' + '\n')  # 写第三行
#     for i in rule1:
#         f.write("%s\n" % i)
#     f.write('输入的句子是%s，识别过程为：\n' % (string))
#     judge = ['', '不']
#     # DFA(F, E)
#     f.write('%s状态%s可以被该DFA接受' % (string, judge[DFA(F, E)]))
#     print('Finished!')
#
#
#
# ##################################
# ##           实验3              ##
# ##################################
# # big = list(input('开始符(用","隔开):'))
# # small = list(input('字母表(用","隔开):'))
# # print('文法(格式为A -> a|aB|....),按"#"退出:')
# # point1 = {}
# # while 1:
# #     ipt = input('')
# #     if ipt == '#':
# #         break
# #     key,value = ipt.split(' -> ')[0],ipt.split(' -> ')[-1].split('|')
# #     point1[key] = value
#
# point = {'S': ['a', 'aA'], 'A': ['a', 'aA', 'cA', 'bB'], 'B': ['a', 'b', 'c', 'aB', 'bB', 'cB']}  # 文法
# # print(point)
# # print(point1)
# big = list(set([i for i in str(point) if 'A' <= i <= 'Z'])) + ['Y']
# # print(big)
# small = list(set([i for i in str(point) if 'a' <= i <= 'z']))
# """文法转NFA"""
# NFA_result = []
# for key, value in point.items():
#     dic = []  # 所有读取一个值到另外状态的字典的列表
#     for i in value:  # 遍历point的一个value
#         if len(i) == 1:
#             dic.append({i[0]: 'Y'})  # 将转移函数加到列表里
#         else:
#             dic.append({i[0]: i[-1]})  # 将转移函数加到列表里，只限于长度为2的候选式
#     print('dic:', dic)
#     di = {}
#     for _ in dic:  # 键相同的字典合并
#         for k, v in _.items():
#             di.setdefault(k, []).append(v)
#     NFA_result.append({key: di})  # 格式为{key1:{key2:value2}},其中key1是一个状态，key2是读入的字符,value2是转移状态的集合
#     print('NFA_result:', NFA_result)
# # print(NFA_result)
#
# print('五元组形式输出结果为：')
# print('M = (%s,%s,$,S,Y)' % (
#     str(big).replace('[', '(').replace(']', ')'), str(small).replace('[', '(').replace(']', ')')))
# for i in NFA_result:
#     for key, value in i.items():
#         for j, k in value.items():
#             print('$(' + key + ',' + j + ') = ', str(k).replace('[', '{').replace(']', '}'))
#
#
#
# ##################################
# ##            实验4             ##
# ##################################
#
# # S = input('输入开始符：')
# # E = input('输入结束符：')
# # status = input('输入所有状态(用空格分开）：').split(' ')
# # data = input('输入读入的符号：')
# # print('请输入NFA对应的转移函数,按#退出,如：(q0,a)=q0：')
# # NFA = []
# # while 1:
# #     a = input()
# #     if a=='#':
# #         break
# #     NFA.append([str(a.split('=')[0][1:3]),a.split('=')[0][-2],a.split('=')[-1]])
# # print(NFA)
#
#
# NFA = [
#     ['q0', 'a', 'q0'],
#     ['q0', 'a', 'q1'],
#     ['q0', 'b', 'q0'],
#     ['q1', 'a', 'q2'],
#     ['q1', 'b', 'q2'],
#     ['q2', 'a', 'q3'],
#     ['q2', 'b', '$'],
#     ['q3', 'a', 'q3'],
#     ['q3', 'b', 'q3'],
# ]
#
#
# def get_item(stlis, word):  # 给当前状态集和读取的字符，返回可达状态
#     lis = []
#     for i in stlis:
#         for j in NFA:
#             if [i, word] == j[:2]:
#                 lis.append(j[2])
#     if '$' in lis:
#         del lis[lis.index('$')]
#     return sorted(list(set(lis)))
#
#
# lower = ['a', 'b']
# # print(get_item(['q0', 'q1', 'q2', 'q3'], 'b'))
# # print('\ \t a \t b')
# point = [['q0']]
# result = []
# for i in point:
#     for j in lower:
#         # print(get_item(i, j), end='\t')
#         result.append(get_item(i, j))
#         if get_item(i, j) not in point:
#             point.append(get_item(i, j))
#             # print('')
# print(result)
# print(point)
# DFA = {}
# print('  ' * 44 + 'DFA状态转移表 ' + '  ' * 44)
# print('- ' * 100)
# print('%-40s | %-40s | %-40s ' % ('状态', 'a', 'b'))
# print('- ' * 100)
# for i in range(0, len(result), 2):
#     cur_point = point[i // 2]
#     nex_point = [result[i], result[i + 1]]
#     print('%-40s | %-40s | %-40s ' % (point[i // 2], result[i], result[i + 1]))  # 2==len(lower)
#     print('- ' * 100)
# print('结束')
#
# print('\n\n\n')
# print('  ' * 44 + 'DFA状态转移函数 ' + '  ' * 44)
# for i in range(0, len(result), 2):
#     cur_point = point[i // 2]
#     # print("$(%s,a) = %s"%(cur_point,result[i]))
#     # print(str(cur_point))
#     print("%50s = %s" % (str('$(' + str(cur_point) + ', a)'), str(result[i]).replace('[', '{').replace(']', '}')))
#     print("%50s = %s" % (str('$( ' + str(cur_point) + ', b)'), str(result[i + 1]).replace('[', '{').replace(']', '}')))
# print('结束')
