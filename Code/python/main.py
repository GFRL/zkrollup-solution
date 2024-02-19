import matplotlib.pyplot as plt
import numpy as np
import math
MAXX=100
numm=1000
#solve_second
#input( A, B, C)
#output(postive  x that makes Ax^2+Bx+C=0)
M=0;C=0;b=0;N=0;C_suppose=0;total_limit=0;C_average=0
S=0
LN=np.arange(0,MAXX,MAXX/numm)
LX1=[];LX2=[];LX11=[];LX22=[];LE1=[];LE2=[];Lpercent1=[];Lpercent2=[];Lpercent=[]
def clear():
    global LX1,LX2,LX11,LX22,LE1,LE2,Lpercent1,Lpercent2,Lpercent
    LX1=[];LX2=[];LX11=[];LX22=[];LE1=[];LE2=[];Lpercent1=[];Lpercent2=[];Lpercent=[]
def solve_second(A,B,C):
    if A<0:
        A=-A
        B=-B
        C=-C
    delta=B*B-4*A*C
    if delta<0 or A==0:
        return 0
    else:
        return (-B +math.sqrt(delta))/(2*A)

def compute(type=0):
    if type == 0 :#足够多钱
        X1 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - M * (N + 1), C * C - M * C + M * b)
        X2 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - M * N, C * C - M * C + M * b)
        E1 = (X1+b) * ((M / ((N + 2) * X1 + C)) - 1)#平衡点运算的时候进行了变形，X_i实际上是X_i-b;
        E2 = (X2+b) * ((M / ((N + 1) * X2 + C)) - 1)
        #if (E2 < 0):
         #   return
        #print("M=%.0lf,C=%.0lf(%.0lf),b=%.0lf\n", M, C, C / C_average, b)
        LX1.append(X1+b)
        LX2.append(X2+b)
        LE1.append(E1)
        LE2.append(E2)
        Lpercent1.append(E1*100/(X1+b))
        Lpercent2.append(E2*100/(X2+b))
        Lpercent.append(50*E2/E1)
    elif type == 1 :
        X1 = C_suppose - b
        X2 = 2 * C_suppose - b
        X11 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - M * (N + 1), C * C - M * C + M * b)
        X22 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - M * (N ), C * C - M * C + M * b)
        if (X1 > X11) :
            X1 = X11 
          #  return
        else:
            X11 = solve_second(N * N, 2 * (C + 2 * X1) * N - M * (N - 1), (C + 2 * X1) * (C + 2 * X1) - M * (C + 2 * X1) + M * b)
        if (X2 > X22) :
            X2 = X22 
           # return
        else:
            X22= solve_second(N * N, 2 * (C + X2) * N - M * (N - 1), (C + X2) * (C + X2) - M * (C + X2) + M * b)
        E1 = (X1+b) * ((M / (N * X11 + C + 2 * X1)) - 1)
        E2 = (X2 + b) * ((M / (N * X22 + C +  X2)) - 1)
        #if (E2 < 0):
            #return
        LX1.append(X1+b)
        LX2.append(X2+b)
        LX11.append(X11+b)
        LX22.append(X22+b)
        LE1.append(E1)
        LE2.append(E2)
        Lpercent1.append(E1*100/(X1+b))
        Lpercent2.append(E2*100/(X2+b))
        Lpercent.append(50*E2/E1)

def compute2(type=0):
    if type == 0 :#足够多钱
        X1 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - (N + 1) * S, C * C - S * C + M)
        X2 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - N * S, C * C - S * C + M)
        E1 = ((M / X1) + S) * X1 / ((N + 2) * X1 + C) - X1 - b#平衡点运算的时候进行了变形，X_i实际上是X_i-b;
        E2 = ((M / X2) + S) * X2 / ((N + 1) * X2 + C) - X2 - b
        #if (E2 < 0):
         #   return
        #print("M=%.0lf,C=%.0lf(%.0lf),b=%.0lf\n", M, C, C / C_average, b)
        LX1.append(X1+b)
        LX2.append(X2+b)
        LE1.append(E1)
        LE2.append(E2)
        Lpercent1.append(E1*100/(X1+b))
        Lpercent2.append(E2*100/(X2+b))
        Lpercent.append(50*E2/E1)
    elif type == 1 :
        X1 = C_suppose - b
        X2 = 2 * C_suppose - b
        X11 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - (N + 1) * S, C * C - S * C + M)
        X22 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - N * S, C * C - S * C + M)
        if (X1 > X11) :
            X1 = X11 
          #  return
        else:
            X11 = solve_second(N * N, 2 * (C + 2 * X1) * N - (N - 1) * S,
				(C + 2 * X1) * (C + 2 * X1) - S * (C + 2 * X1) + M)
        if (X2 > X22) :
            X2 = X22 
           # return
        else:
            X22= solve_second(N * N, 2 * (C + X2) * N - (N - 1) * S,
				(C + X2) * (C + X2) - S * (C + X2) + M)
        E1 = ((M / X1) + S) * X1 / (N * X11 + C + 2 * X1) - X1 - b
        E2 = ((M / X2) + S) * X2 / (N * X22 + C + X2) - X2 - b
        #if (E2 < 0):
            #return
        LX1.append(X1+b)
        LX2.append(X2+b)
        LX11.append(X11+b)
        LX22.append(X22+b)
        LE1.append(E1)
        LE2.append(E2)
        Lpercent1.append(E1*100/(X1+b))
        Lpercent2.append(E2*100/(X2+b))
        Lpercent.append(50*E2/E1)

def compute3(type=0):
    if type == 0 :#足够多钱
        X1 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - (N + 1) * S,  - S * C + M)
        X2 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - N * S, - S * C + M)
        E1 = ((M / X1) + S) * X1 / ((N + 2) * X1 + C) - X1#平衡点运算的时候进行了变形，X_i实际上是X_i-b;
        E2 = ((M / X2) + S) * X2 / ((N + 1) * X2 + C) - X2
        #if (E2 < 0):
         #   return
        #print("M=%.0lf,C=%.0lf(%.0lf),b=%.0lf\n", M, C, C / C_average, b)
        LX1.append(X1)
        LX2.append(X2)
        LE1.append(E1)
        LE2.append(E2)
        Lpercent1.append(E1*100/X1)
        Lpercent2.append(E2*100/X2)
        Lpercent.append(50*E2/E1)
    elif type == 1 :
        X1 = C_suppose
        X2 = 2 * C_suppose
        X11 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - (N + 1) * S, -S * C + M)
        X22 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - N * S, -S * C + M)
        if (X1 > X11) :
            X1 = X11 
          #  return
        else:
            X11 = solve_second(N * N, 2 * (C + 2 * X1) * N - (N - 1) * S,
				 - S * (C + 2 * X1) + M)
        if (X2 > X22) :
            X2 = X22 
           # return
        else:
            X22= solve_second(N * N, 2 * (C + X2) * N - (N - 1) * S,
				 - S * (C + X2) + M)
        E1 = ((M / X1) + S) * X1 / (N * X11 + C + 2 * X1) - X1 
        E2 = ((M / X2) + S) * X2 / (N * X22 + C + X2) - X2
        #if (E2 < 0):
            #return
        LX1.append(X1)
        LX2.append(X2)
        LX11.append(X11)
        LX22.append(X22)
        LE1.append(E1)
        LE2.append(E2)
        Lpercent1.append(E1*100/X1)
        Lpercent2.append(E2*100/X2)
        Lpercent.append(50*E2/E1)

#b = 1; C = 19 * 98; C_suppose = 20; total_limit = 3000; C_average = 19;M = 2040
#b = 1; C = 19 * 98; C_suppose = 20; total_limit = 3000;S = 2100; M = 900
b=1;C=20*98;C_suppose=20;total_limit=3000;S=2000;M=20*(40800/19-S)
mycolor=["b","c","g","k","m","r","y"]
print("MX/(X-b)  very rich\n")
plt.figure(1)
plt.figure(figsize=(50, 20))
#plt.subplot(1,1,1)
plt.xlabel("Number of Other clever people")
plt.ylabel("the tempetation to cooperate")

plt.figure(2)
plt.figure(figsize=(50, 20))
plt.subplot(1,2,1)
plt.xlabel("Number of Other clever people")
plt.ylabel("benifit of E1")
plt.subplot(1,2,2)
plt.xlabel("Number of Other clever people")
plt.ylabel("benifit of E2")
plt.figure(3)
plt.figure(figsize=(50, 20))
plt.subplot(1,2,1)
plt.xlabel("Number of Other clever people")
plt.ylabel("benifit percent of E1")
plt.subplot(1,2,2)
plt.xlabel("Number of Other clever people")
plt.ylabel("benifit percent of E2")
for j in range(8):
    C_suppose=5*(j+1)
    clear()
    for i in LN:
        N = i; C = (98 - i) * 19
        compute(1)
    plt.figure(1)
    plt.plot(LN,Lpercent,color=mycolor[j%7],label="C_suppose="+str(C_suppose))
    plt.figure(2)
    plt.subplot(1,2,1)
    plt.plot(LN,LE1,color=mycolor[j%7],label="C_suppose="+str(C_suppose))
    plt.subplot(1,2,2)
    plt.plot(LN,LE2,color=mycolor[j%7],label="C_suppose="+str(C_suppose))
    plt.figure(3)
    plt.subplot(1,2,1)
    plt.plot(LN,Lpercent1,color=mycolor[j%7],label="C_suppose="+str(C_suppose))
    plt.subplot(1,2,2)
    plt.plot(LN,Lpercent2,color=mycolor[j%7],label="C_suppose="+str(C_suppose))
clear()
for i in LN:
    N = i; 
    #C = (98 - i) * 19！！！
    C = (98 - i) * 20
    compute()
plt.figure(1)
plt.plot(LN,Lpercent,color='b',label="C_suppose=infite")
plt.legend()
plt.figure(2)
plt.subplot(1,2,1)
plt.plot(LN,LE1,color='b',label="C_suppose1="+str(C_suppose))
plt.legend()
plt.subplot(1,2,2)
plt.plot(LN,LE2,color='b',label="C_suppose1="+str(C_suppose))
plt.figure(3)
plt.subplot(1,2,1)
plt.plot(LN,Lpercent1,color='b',label="C_suppose1="+str(C_suppose))
plt.legend()
plt.subplot(1,2,2)
plt.plot(LN,Lpercent2,color='b',label="C_suppose1="+str(C_suppose))

plt.figure(1)
plt.savefig("./example3_detail tempetation.png")

plt.figure(2)
plt.savefig("./example3_detail benifit.png")

plt.figure(3)
plt.savefig("./example3_detail benifit percent.png")



# plt.figure(4)
# plt.figure(figsize=(50, 20))
# #plt.subplot(1,1,1)
# plt.xlabel("C_suppose")
# plt.ylabel("the tempetation to cooperate")

# LN=np.arange(10,100)
# clear()
# N=0;C=(98-i)*20
# for j in LN:
#     C_suppose=j
#     compute(1)
# plt.figure(4)
# plt.plot(LN,Lpercent,color=mycolor[j%7],label="C_suppose="+str(C_suppose))
# for i in LN:
#     N = i; 
#     #C = (98 - i) * 19！！！
#     C = (98 - i) * 20
#     compute()

# plt.figure(4)
# plt.savefig("./example3_detail amazing benifit percent.png")		