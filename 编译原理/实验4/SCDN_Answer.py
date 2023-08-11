# __author__ = 'PythonStriker'
# global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld, \
#     StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld, DFA_StatusWrold
# EnterWorld = []  # 输入状态
# NFA_StatusWorld = []  # NFA有穷状态集
# DFA_StatusWrold = []  # DFA有穷状态集
#
#
# def main():
#     EndList = []
#     global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld, \
#         StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld, DFA_StatusWrold
#     StartWorld = input("输入开始状态:")
#     EndWorld = input("输入结束状态:")
#     StatusNumber = int(input("输入状态个数:"))
#     EnterNumber = int(input("状态机输入个数:"))
#     print("输入不确定有穷状态机转换表:")
#     NFA_StautsMatrix = [[] for _ in range(0, StatusNumber + 1)]  # NFA状态转换表
#     for row in range(0, StatusNumber + 1):  # 存入状态转换表
#         line = input().split(' ')
#         for column in range(len(line)):
#             NFA_StautsMatrix[row].append(line[column])
#
#     for enter in NFA_StautsMatrix[0]:  # 存入输入状态
#         if enter != '\\' and enter != '&':
#             EnterWorld.append(enter)
#     for row in range(1, StatusNumber + 1):  # NFA有穷状态集
#         NFA_StatusWorld.append(NFA_StautsMatrix[row][0])
#     DFA_Start = Empty_Closure(StartWorld)  # DFA开始状态
#     for status in DFA_StatusWrold:
#         for enter in EnterWorld:
#             Empty_Closure(Enter_Closure(status, enter))
#
#     DFA_StautsMatrix = [[] for _ in range(0, len(DFA_StatusWrold) + 1)]
#
#     for row in range(0, len(DFA_StatusWrold) + 1):
#         if row == 0:
#             line = "\ a b c"
#             line = line.split(' ')
#             for column in range(len(line)):
#                 DFA_StautsMatrix[row].append(line[column])
#         else:
#             if row <= len(DFA_StatusWrold):
#                 number = DFA_StatusWrold[row - 1]
#                 lineList = []
#                 line = number
#                 for enter in EnterWorld:
#                     if Empty_Closure(Enter_Closure(number, enter)) == False:
#                         line = line + ' ' + '&'
#                     else:
#                         line = line + ' ' + Empty_Closure(Enter_Closure(number, enter))
#                 lineList = line.split(' ')
#                 for column in range(len(lineList)):
#                     DFA_StautsMatrix[row].append(lineList[column])
#     print("------------------------------DFA-------------------------------------")
#     print("确定有穷自动机DFA_S：", end='')
#     for number in DFA_StatusWrold:
#         print(number, end='  ')
#     print("\n确定有穷自动机DFA_∑:", end='')
#     for number in EnterWorld:
#         print(number, end='  ')
#     print("\n确定有穷自动机DFA_S0:" + DFA_Start)
#     for number in DFA_StatusWrold:
#         if EndWorld in number:
#             EndList.append(number)
#     print("确定有穷自动机DFA_Z:", end='')
#     for number in EndList:
#         print(number, end='  ')
#     print("\n确定有穷自动机DFA_δ:")
#     for row in DFA_StautsMatrix:
#         print()
#         for column in row:
#             print('%8s' % column, end='')
#
#
# def Empty_Closure(string):
#     global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld, \
#         StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld, DFA_StatusWrold
#     List = []
#     flag = 0
#     NewList = []
#     NewStatus = string
#     if string == False:
#         return False
#     if ',' not in string:
#         while flag == 0:
#             if ',' not in string:
#                 row = NFA_StatusWorld.index(string) + 1
#                 if NFA_StautsMatrix[row][1] != '&' and NFA_StautsMatrix[row][1] != '*':
#                     if NFA_StautsMatrix[row][1] not in NewStatus:
#                         NewStatus = NewStatus + ',' + NFA_StautsMatrix[row][1]
#                         string = NFA_StautsMatrix[row][1]
#                     else:
#                         flag = 1
#                 else:
#                     flag = 1
#             else:
#                 List = string.split(',')
#                 for number in range(len(List)):
#                     if List[number] not in NewStatus:
#                         NewStatus = NewStatus + ',' + List[number]
#                         string = List[number]
#                     elif List[number] in NewStatus and List[number] in NewStatus:
#                         flag = 1
#                         break
#         if ',' in NewStatus:
#             NewList = NewStatus.split(',')
#             NewList = set(NewList)
#             NewList = (sorted(set(NewList)))
#             NewStatus = ','.join(NewList)
#         if NewStatus not in DFA_StatusWrold:
#             DFA_StatusWrold.append(NewStatus)
#         return NewStatus
#     else:
#         List = string.split(',')
#         for number in List:
#             row = NFA_StatusWorld.index(number) + 1
#             if ',' not in NFA_StautsMatrix[row][1]:
#                 if NFA_StautsMatrix[row][1] != '&' and NFA_StautsMatrix[row][1] != '*':
#                     if NFA_StautsMatrix[row][1] not in NewStatus:
#                         NewStatus = NewStatus + ',' + NFA_StautsMatrix[row][1]
#                     else:
#                         pass
#                 else:
#                     break
#         if ',' in NewStatus:
#             NewList = NewStatus.split(',')
#             NewList = set(NewList)
#             NewList = (sorted(set(NewList)))
#             NewStatus = ','.join(NewList)
#         if NewStatus not in DFA_StatusWrold:
#             DFA_StatusWrold.append(NewStatus)
#         return NewStatus
#
#
# def Enter_Closure(string, enter):
#     global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld, \
#         StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld, DFA_StatusWrold
#     status = '99999'
#     List = []
#     NewList = []
#     if ',' not in string:
#         row = NFA_StatusWorld.index(string) + 1
#         if NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '&' \
#                 and NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '*' \
#                 and string != NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]:
#
#             if status == '99999':
#                 status = NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#             else:
#                 status = status + ',' + NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#         elif NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '&' \
#                 and NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '*' \
#                 and string == NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]:
#             if string in status:
#                 pass
#             else:
#                 if status == '99999':
#                     status = NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#                 else:
#                     status = status + ',' + NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#         else:
#             return False
#         if status != '99999':
#             if string not in status:
#                 if Enter_Closure(status, enter):
#                     status = status + ',' + Enter_Closure(status, enter)
#             return status
#         else:
#             return False
#     else:
#         List = string.split(',')
#         for number in List:
#             row = NFA_StatusWorld.index(number) + 1
#             if NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '&' \
#                     and NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '*' \
#                     and number != NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]:
#                 if status == '99999':
#                     status = NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#                 else:
#                     status = status + ',' + NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#             elif NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '&' \
#                     and NFA_StautsMatrix[row][EnterWorld.index(enter) + 2] != '*' \
#                     and number == NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]:
#                 if number in status:
#                     break
#                 else:
#                     if status == '99999':
#                         status = NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#                     else:
#                         status = status + ',' + NFA_StautsMatrix[row][EnterWorld.index(enter) + 2]
#             else:
#                 pass
#         if status != '99999':
#             NewList = status.split(',')
#             for number in NewList:
#                 if number not in List:
#                     if Enter_Closure(number, enter):
#                         status = status + ',' + Enter_Closure(number, enter)
#             return status
#         else:
#             return False
#
#
# if __name__ == "__main__":
#     main()
a = [12]
b = {}
b[a] = 1
print(b)