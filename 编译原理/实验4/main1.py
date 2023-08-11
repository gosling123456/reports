K = []  # NFA状态集
E = []  # NFA输入符号集
F = []  # NFA弧
S = []  # FNA初态集
Z = []  # NFA终态集
K_DFA = []  # DFA状态集
fx = []  # 状态转换函数


# 输入NFA
def input_NFA():
    a = input('请输入NFA状态集(以空格区分,以换行结束): ')
    K.extend(a.split(' '))
    a = input('请输入NFA输入符号集(以空格区分,以换行结束): ')
    E.extend(a.split(' '))
    a = input('请输入NFA初态集(以空格区分,以换行结束): ')
    S.extend(a.split(' '))
    a = input('输入NFA终态集(以空格区分,以换行结束): ')
    Z.extend(a.split(' '))
    print('请输入NFA弧的条数: ')
    n = int(input())
    print('请输入这些弧(分别输入状态1,输入符号,状态2,以空格区分换行结束,ε表示为$)')
    for i in range(n):
        a = input()
        t = a.split(' ')
        F.append(t)


# ε-closure函数
def closure(I):
    for i in I:
        for f in F:
            if f[0] == i and f[1] == "$":
                if f[2] not in I:
                    I.append(f[2])
    return sorted(I)  # 从小到大排序（按字典）


# move(I, a)函数
def move(I, a):
    new_I = []
    for i in I:
        for f in F:
            if f[0] == i and f[1] == a:
                if f[2] not in new_I:
                    new_I.append(f[2])
    return sorted(new_I)  # 从小到大排序（按字典）


# 判断新生成的子集是否存在,存在返回位置，不存在返回-1
def is_inDFA(new_k):
    new_set = set(new_k)
    index = 0
    for k in K_DFA:
        old_set = set(k)
        if old_set == new_set:
            return index
        index = index + 1
    return -1


# 添加到转换函数中
def myAppend(k, e, new_k):
    t = []
    t.append(k)
    t.append(e)
    t.append(new_k)
    fx.append(t)


# NFA转DFA
def NFA2DFA():
    J = closure(S)  # NFA的初态
    K_DFA.append(J)
    for k in K_DFA:
        for e in E:
            new_k = closure(move(k, e))
            if new_k is not None:  # 不存在于当前子集中，则加入
                if is_inDFA(new_k) == -1:
                    K_DFA.append(new_k)
                    myAppend(is_inDFA(k), e, is_inDFA(new_k))
                else:  # 存在于当前子集中，则不加入
                    myAppend(is_inDFA(k), e, is_inDFA(new_k))


# 打印DFA
def print_DFA():
    print("NFA子集构造法构造出的子集：")
    for k in K_DFA:
        print(K_DFA.index(k), end=": ")
        print(k)
    # 矩阵形式
    print("DFA矩阵表示：")
    print("\\", end="\t")
    for e in E:
        print(e, end="\t")
    print()
    for i in range(len(K_DFA)):
        print(i, end="\t")
        for e in E:
            for f in fx:
                if i == f[0] and e == f[1]:
                    print(f[2], end="\t"+'|')
                    break
                if fx.index(f) == len(fx) - 1:
                    print("", end="\t")
        for j in K_DFA[i]:
            if j in Z:
                print("(终态)", end=" ")
                break
        print()


if __name__ == '__main__':
    input_NFA()
    NFA2DFA()
    print_DFA()