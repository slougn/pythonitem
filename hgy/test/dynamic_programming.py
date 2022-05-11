#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-05-09 09:05:43
LastEditTime: 2022-05-11 22:04:34
LastEditors: 560130
Description: 直接导入H列数据,从H列开始,重新计算之后的列，并且完成动态规划
             本文档所有计算都使用numpy包
FilePath: /pythonitem/hgy/test/dynamic_programming.py
'''
import numpy as np
from scipy.optimize import minimize
import copy

#导入H列数据 原始冷负荷
January = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/1月.npy")
February = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/2月.npy")
March = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/3月.npy")
April = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/4月.npy")
May = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/5月.npy")
June = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/6月.npy")
July = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/7月.npy")
August = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/8月.npy")
September = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/9月.npy")
October = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/10月.npy")
November = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/11月.npy")
December = np.load(
    "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/12月.npy")

H = [
    January, February, March, April, May, June, July, August, September,
    October, November, December
]  # 数组列表


# 数组转为数组列表
def to_arraylist(standard, arr):
    a_l = []
    b = 0
    e = 0
    for s in standard:
        e = len(s) + b
        a_l.append(arr[b:e])
        b = e
    return a_l


# 数组列表转为数组
def to_array(arr_list):
    arr = arr_list[0]
    for i in range(1, len(arr_list)):
        arr = np.r_[arr, arr_list[i]]
    return arr



# 第CC列参数
CC = [
    1, 1, 1, 0.745724112, 0.398184911, 0.410399204, 0.449879249, 0.544061884,
    0.481509413, 0.549749516, 1.113799611, 1
]



# 第I列  冷负荷 I = H * CC
def I_column(H, CC):
    I_c = []
    for i in range(len(H)):
        I_c.append(H[i] * CC[i])
    return I_c




# 第D列 需要计算的系数
# param = np.ones(12) * 1



# 第J列  修正冷负荷 J = I * param
def J_column(I, param):
    J = []
    for i in range(len(I)):
        J.append(I[i] * param[i])
    return J




# 获取第K列 湿球温度



# 获取L列 冷却水进水温度 L = K + 5
def L_column(K):
    return K + 5




# 获取M列 冷却水进水温度
def M_column(L):
    M = copy.deepcopy(L)
    M[M < 18] = 18
    return M





# 获取N列 运行台数
def N_column(J):
    N = copy.deepcopy(J)
    for n in N:
        n[n != 0] = np.ceil(n[n != 0] / 350 / 3.517)
    return N




# 获取O列 冷水机组1号运行台数
def O_column(N):
    O = copy.deepcopy(N)
    for i in range(len(O)):
        O[i][O[i]>=1] = 1
        O[i][O[i]<1] = 0
    return O
        

# 获取P列
def P_column(N):
    P = copy.deepcopy(N)
    for p in P:
        p[p<2] = 0
        p[p>=2] = 1
    return P



# Q列 冷水机组1#符合率
def Q_column(O,J,P):
    Q = copy.deepcopy(O)
    for i in range(len(O)):
        Q[i][Q[i]==0] = 0
        Q[i][Q[i]!=0] = J[i][Q[i]!=0]/(350*3.517*O[i][Q[i]!=0]+350*3.517*P[i][Q[i]!=0])
    return Q



# R列 冷水机组2#符合率
def R_column(O,J,P):
    R = copy.deepcopy(P)
    for i in range(len(O)):
        R[i][R[i]==0] = 0
        R[i][R[i]!=0] = J[i][R[i]!=0]/(350*3.517*O[i][R[i]!=0]+350*3.517*P[i][R[i]!=0])
    return R



# S列 冷冻水出水温度
def S_column(standard):
    S = []
    for s in standard:
        S.append(np.ones(s.shape)*7.5)
    return S



# T列 冷水机组1#修正符合率
def T_column(Q):
    T = copy.deepcopy(Q)
    for t in T:
        t[t<0.1] = 0
        t[(t>=0.1) & (t<0.3)] = 0.3
        t[t>1] = 1
    return T



# U列 冷水机组2#修正符合率
def U_column(R):
    U = T_column(R)
    return U



# AB列公式  COP公式 X1,X2,X3 为数值
def COP(X1,X2,X3): 
    a = 0.000407461117728266
    b = 0.0319727844024694
    c = -0.0321549861357119
    d = 2.49432757221509
    return np.exp(a * X1 + b * X2 + c * X3 + d)

# V列 1#COP
def V_column(T,S,M):
    M = to_arraylist(H,M)
    V = copy.deepcopy(T)
    for i in range(len(V)):
        V[i][V[i]==0] = 0
        V[i][V[i]!=0] = COP(T[i][V[i]!=0]*100,S[i][V[i]!=0],M[i][V[i]!=0])*(1-0.02*10)*0.9
    return V



# W列 2#COP
def W_column(U,S,M):
    W = V_column(U,S,M)
    return W



# X列 1#制冷量
def X_column(T):
    X = []
    for t in T:
        X.append(t*350*3.517)
    return X




# Y列 2#制冷量
def Y_column(U):
    Y = X_column(U)
    return Y


# Z列 1#功率
def Z_column(V,X):
    Z = copy.deepcopy(V)
    for i in range(len(Z)):
        Z[i][Z[i]==0] = 0
        Z[i][Z[i]!=0] = X[i][Z[i]!=0] / V[i][Z[i]!=0] 
    return Z



# AA列 2#功率
def AA_column(W,Y):
    AA = Z_column(W,Y)
    return AA



# AD列 冷水机组功率
def AD_column(Z,AA):
    AD = []
    for i in range(len(Z)):
        AD.append(Z[i] + AA[i])
    return AD


# AG列 1#冷冻水流量
def AG_column(X):
    AG = []
    for x in X:
        AG.append(x*0.172*5/3)
    return AG



# AH列 2#冷冻水流量
def AH_column(Y):
    AH = AG_column(Y)
    return AH



# AI列 1#冷冻水频率
def AI_column(AG):
    AI = copy.deepcopy(AG)
    for ai in AI:
        ai[:] = ai/250*50
        ai[ai == 0] = 0
        ai[(ai>0) & (ai < 30)] = 30
        ai[ai >50] = 50
    return AI


# AJ列 2#冷冻水频率
def AJ_column(AH):
    AJ = AI_column(AH)
    return AJ



# AK列 1#冷冻水功率
def AK_column(AI):
    AK = copy.deepcopy(AI)
    for ak in AK:
        ak[:] = 55 * (ak/50)**3 /0.85/0.9
        ak[ak>55] = 55
    return AK



# AL列 2#冷冻水泵功率
def AL_column(AJ):
    AL = AK_column(AJ)
    return AL



# AM列 冷冻水泵功率
def AM_column(AK,AL):
    AM = []
    for i in range(len(AK)):
        AM.append(AK[i] + AL[i])
    return AM



# AN列 1#冷却水泵流量
def AN_column(X):
    AN = []
    for x in X:
        AN.append(x * 0.125 * 5 / 3)
    return AN



# AO列 2#冷却水流量
def AO_column(Y):
    AO = AN_column(Y)
    return AO



# AP列 1#冷却泵频率
def AP_column(AN):
    AP = copy.deepcopy(AN)
    for ap in AP:
        ap[:] = ap/300*50
        ap[ap == 0] = 0
        ap[(ap>0) & (ap < 30)] = 30
        ap[ap >50] = 50
    return AP



# AQ列 2#冷却水频率
def AQ_column(AO):
    AQ = AP_column(AO)
    return AQ




# AR列 1#冷却水泵功率
def AR_column(AP):
    AR = AK_column(AP)
    return AR



# AS列 2#冷却水泵功率
def AS_column(AQ):
    AS = AK_column(AQ)
    return AS



# AT列 冷却水泵功率
def AT_column(AR,AS):
    AT = []
    for i in range(len(AR)):
        AT.append(AR[i] + AS[i])
    return AT



# AU列 1#冷却塔流量修正
def AU_column(AN):
    AU = copy.deepcopy(AN)
    for au in AU:
        au[au==0] = 0
        au[(au>0)&(au<300*25/50)] = 300*25/50
    return AU



# AV列 2#冷却水泵流量修正
def AV_column(AO):
    AV = AU_column(AO)
    return AV



# AW列 1#冷却塔功率
def AW_column(AU):
    AW = copy.deepcopy(AU)
    for aw in AW:
        aw[:] = 22 * (aw/300)**3 /0.85
        aw[aw>22] = 22
    return AW



# AX列 2#冷却塔功率
def AX_column(AV):
    AX = AW_column(AV)
    return AX



# AY列 冷却塔功率
def AY_column(AW,AX):
    AY = []
    for i in range(len(AW)):
        AY.append(AW[i] + AX[i])
    return AY




# AZ列 二级功率
def AZ_column(AG):
    AZ = copy.deepcopy(AG)
    for az in AZ:
        az[az==0] = 0
        az[az!=0] = 75
    return AZ



# BA列 末端功率
def BA_column(AZ,X,Y):
    BA = copy.deepcopy(AZ)
    for i in range(len(BA)):
        BA[i][BA[i]==0] = 0
        BA[i][BA[i]!=0] =  (X[i][BA[i]!=0] + Y[i][BA[i]!=0]) * 0.15
    return BA



# BB列 空调系统功率
def BB_column(AD,AM,AT,AY,AZ,BA):
    BB = []
    for i in range(len(AD)):
        BB.append(AD[i] + AM[i] + AT[i] + AY[i] + AZ[i] +BA[i])
    
    return BB





# #动态规划

def BB_caculate(param,H,CC,K):
    I = I_column(H, CC)  # 数组列表
    # 第D列 需要计算的系数
    J = J_column(I, param)  # 数组列表
    L = L_column(K)  # 数组
    M = M_column(L)  # 数组
    N = N_column(J)  # 数组列表
    O = O_column(N) # 数组列表
    P = P_column(N) # 数组列表
    Q = Q_column(O,J,P) # 数组列表
    R = R_column(O,J,P) # 数组列表
    S = S_column(H) # 数组列表
    T = T_column(Q) # 数组列表
    U = U_column(R) # 数组列表
    V = V_column(T,S,M) # 数组列表
    W = W_column(U,S,M) # 数组列表
    X = X_column(T) # 数组列表
    Y = Y_column(U) # 数组列表
    Z = Z_column(V,X) # 数组列表
    AA = AA_column(W,Y) # 数组列表
    AD = AD_column(Z,AA) # 数组列表
    AG = AG_column(X) # 数组列表
    AH = AH_column(Y) # 数组列表
    AI = AI_column(AG) # 数组列表
    AJ = AJ_column(AH) # 数组列表
    AK = AK_column(AI)
    AL = AL_column(AJ) # 数组列表
    AM = AM_column(AK,AL) # 数组列表
    AN = AN_column(X) # 数组列表
    AO = AO_column(Y) # 数组列表
    AP = AP_column(AN) # 数组列表
    AQ = AQ_column(AO) # 数组列
    AR = AR_column(AP) # 数组列表
    AS = AS_column(AQ) # 数组列表
    AT = AT_column(AR,AS) # 数组列表
    AU = AU_column(AN) # 数组列表
    AV = AV_column(AO) # 数组列表
    AW = AW_column(AU) # 数组列表
    AX = AX_column(AV) # 数组列表
    AY = AY_column(AW,AX) # 数组列表
    AZ = AZ_column(AG) # 数组列表
    BA = BA_column(AZ,X,Y) # 数组列表
    BB = BB_column(AD,AM,AT,AY,AZ,BA)
    return BB



def Fobj(param, H,CC,K, ENERGY):
    BB = BB_caculate(param,H,CC,K)
    bb = []
    for i in range(len(BB)):
        bb.append(sum(BB[i]))
    bb = np.array(bb)
    error_out = np.sum(abs(bb-ENERGY))

    return error_out


def make_consf(H,CC,K,ENERGY):
    cons_list = []
    for i in range(len(H)):
        def make_cons_fun(i):
            def cons_fun(X):
                BB = BB_caculate(X,H,CC,K)
                bb = []
                for j in range(len(BB)):
                    bb.append(sum(BB[j]))
                sum_bb = sum(bb)
                return 0.01- abs((sum(BB[i]) - ENERGY[i])/sum(ENERGY))
                # return 1.01 - sum(BB[i])/sum(ENERGY)
            return cons_fun
        cons_list.append(make_cons_fun(i))
    cons_tuple_list = []
    for i in range(len(cons_list)):
        cons_tuple_list.append(("type","ineq"))
        cons_tuple_list.append(("fun",cons_list[i]))
    cons_dict_list = []
    for i in range(0,len(cons_tuple_list),2):
        tmp = dict(cons_tuple_list[i:i+2])
        cons_dict_list.append(tmp)
    cons_dict_tuple = tuple(cons_dict_list)
    return cons_dict_tuple

def make_consf2(H,CC,K,ENERGY):
    def consf(X):
        BB = BB_caculate(X, H,CC,K)
        bb = []
        for i in range(len(BB)):
            bb.append(sum(BB[i]))
        bb = np.array(bb)
        return 0.01 - abs((sum(bb)-sum(ENERGY))/sum(ENERGY))
    cons = (
        {
            'type':'ineq',
            'fun':consf
        }
    )
    return cons

def do_optimization(Fobj, param,H,CC,K, ENERGY):
    def f(X):
        # param = to_arraylist(H,X)
        return Fobj(X, H,CC,K, ENERGY)

        # return 0.01 - abs(sum(bb)-sum(ENERGY))/sum(ENERGY)
    
    cons = make_consf2(H,CC,K,ENERGY)
    # from scipy import optimize
    # fprime = lambda x: optimize.approx_fprime(x, f, 0.01)
    # res = minimize(f, param, method='Newton-CG', constraints=cons,jac = fprime)
    # res = minimize(f, param, method='L-BFGS-B', constraints=cons)
    # res = minimize(f, param, method='TNC', constraints=cons)
    res = minimize(f, param, method='SLSQP',constraints=cons)
    return res


if __name__ == "__main__":
    H = [
        January, February, March, April, May, June, July, August, September,
        October, November, December
    ]  # 数组列表

    # 第CC列参数
    # CC = [
    #     1, 1, 1, 0.745724112, 0.398184911, 0.410399204, 0.449879249, 0.544061884,
    #     0.481509413, 0.549749516, 1.113799611, 1
    #     ]
    CC = [
        1, 0.725835, 0.202332, 0.177195, 0.1071, 0.101639, 0.105531, 0.119935,
        0.11683, 0.152055, 0.278822, 0.680969
        ]
    CC = np.array(CC)  # 数组

    # 第D列 需要计算的系数
    param = np.ones(12) 
    # param = []
    # for i in range(len(H)):
    #     param.append(np.ones(len(H[i])))
    param = np.array([1.0,1.0,2.03,2.08,2.11,2.17,2.23,2.40,2.44,2.46,2.47,1.0])
    # 获取第K列 湿球温度
    K = np.load(
        "/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/test/湿球温度.npy"
        )    # 数组
    # 目标函数
    ENERGY = np.array([146000,122000,116000,110000,118000,140000,166000,196000,144000,108000,114000,160000])*2
    BB = BB_caculate(param,H,CC,K)

    print("==========================")
    print("开始时误差")
    err = Fobj(param, H,CC,K, ENERGY)
    print(err)

    print("开始时约束条件")
    cons = make_consf2(H,CC,K,ENERGY)
    print(cons['type'],cons['fun'](param))
    # for t in cons:
        # print(t['type'],t['fun'](param))

    print("=============开始动态规划===============")
    res = do_optimization(Fobj,param,H,CC,K, ENERGY)
    print(res)
    print("============动态规划结束==============")

    BB = BB_caculate(res.x,H,CC,K)
    bb = []
    for i in range(len(BB)):
        bb.append(sum(BB[i]))
    print("理论结果",bb)
    print("实际结果",ENERGY)

    print("==========================")
    print("结束时误差")
    err = Fobj(res.x, H,CC,K, ENERGY)
    print(err)

    print("结束时约束条件")
    cons = make_consf2(H,CC,K,ENERGY)
    print(cons['type'],cons['fun'](res.x))
    # for t in cons:
        # print(t['type'],t['fun'](res.x))




## 以下代码无用
    # L = L_column(K)  # 数组

    # M = M_column(L)  # 数组

    # N = N_column(J)  # 数组列表

    # O = O_column(N) # 数组列表

    # P = P_column(N) # 数组列表

    # Q = Q_column(O,J,P) # 数组列表

    # R = R_column(O,J,P) # 数组列表

    # S = S_column(H) # 数组列表

    # T = T_column(Q) # 数组列表

    # U = U_column(R) # 数组列表

    # V = V_column(T,S,M) # 数组列表

    # W = W_column(U,S,M) # 数组列表

    # X = X_column(T) # 数组列表

    # Y = Y_column(U) # 数组列表

    # Z = Z_column(V,X) # 数组列表

    # AA = AA_column(W,Y) # 数组列表

    # AD = AD_column(Z,AA) # 数组列表

    # AG = AG_column(X) # 数组列表

    # AH = AH_column(Y) # 数组列表

    # AI = AI_column(AG) # 数组列表

    # AJ = AJ_column(AH) # 数组列表

    # AK = AK_column(AI)

    # AL = AL_column(AJ) # 数组列表

    # AM = AM_column(AK,AL) # 数组列表

    # AN = AN_column(X) # 数组列表

    # AO = AO_column(Y) # 数组列表

    # AP = AP_column(AN) # 数组列表

    # AQ = AQ_column(AO) # 数组列表

    # AR = AR_column(AP) # 数组列表

    # AS = AS_column(AQ) # 数组列表

    # AT = AT_column(AR,AS) # 数组列表

    # AU = AU_column(AN) # 数组列表

    # AV = AV_column(AO) # 数组列表

    # AW = AW_column(AU) # 数组列表

    # AX = AX_column(AV) # 数组列表

    # AY = AY_column(AW,AX) # 数组列表

    # AZ = AZ_column(AG) # 数组列表

    # BA = BA_column(AZ,X,Y) # 数组列表

    # BB = BB_column(AD,AM,AT,AY,AZ,BA)