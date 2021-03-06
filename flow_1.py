import numpy as np
import random


beta = 0.5
gamma = 0.5



AA = [[1,0,-1,1,-1,0,0,0,0,0],[0,-1,-1,1,0,1,0,0,0,0],[0,0,0,0,-1,0,-1,1,0,1],[0,0,0,0,0,-1,1,0,1,0]]



BB = [[-2,-5,10,0]]
CC = [[1,1,0,0,0,0,0,0,0,0]]


x_0 = np.ones((10,1))    # 1*10
s_0 = np.ones((10,1))
y_0 = np.zeros((4,1))

e = np.ones((10,1))

# initializing x_k, s_k , y_k
x_k = x_0                   # 10*1
y_k = y_0                   # 10*1
s_k = s_0                   # 4*1

#begin the iterations
k = 1
ep = 0.001
count = 0

A = np.array(AA)
b = np.transpose(np.array(BB))
c = np.transpose(np.array(CC))

for k in range(1000):
    #     print (x_k[0])
    count  = count + 1
    Axk = np.dot(A,x_k)
    r_P = b - Axk
    Ayk = np.dot(A.T, y_k)
    r_D = c - np.reshape(Ayk, [10,1]) - s_k
    #     print (r_D)# 10*1
    n = 10.0
    st = np.dot(np.transpose(x_k), s_k)
    u = (st) / n
    
    
    # check for termination
    
    temp1 = np.transpose(s_k)[0]
    S_k = np.diag(temp1)       # 10*10
    S_k_inv = np.linalg.inv(S_k)    # 10*10
    temp2 = np.transpose(x_k)[0]
    X_k = np.diag(temp2)       # 10*10
    
    flag0 = np.dot(A,S_k_inv)
    flag1= np.dot(flag0,X_k)
    M = np.dot(flag1,np.transpose(A))
    flag2= np.dot(A,S_k_inv)# 4*4
    mul = gamma*u*e
    r = b + np.dot(flag2 , (np.dot(X_k, r_D) - mul))      #4*1
    
    
    d_y = np.linalg.solve(M, r)
    
    
    d_s = r_D - np.dot(A.T, d_y)
    
    
    prod = gamma * u * e
    dot = np.dot(X_k, d_s)
    d_x = -x_k + np.dot(S_k_inv, ( prod- dot) )
    
    
    min_P = []
    min_P.append(1000)
    #     min_P.append(100)
    for i in range (len(d_x)):
        cond1 = d_x[i][0]<0
        if(cond1):
            f1 = x_k[i][0] / d_x[i][0]
            min_P.append(-f1)



#     print (min_P)

    min_D = []
    min_D.append(1000)
    for i in range (len(d_s)):
        cond2= d_s[i][0]<0
        if(cond2):
            f2 = s_k[i][0] / d_s[i][0]
            min_D.append(-f2)


    arr =  np.array([np.min(np.array(min_D)), np.min(np.array(min_P))])
#     alpha_k =

    x_k = x_k + np.min(np.array([0.95*np.min(arr), 1]))*d_x
    y_k = y_k + np.min(np.array([0.95*np.min(arr), 1]))*d_y
    s_k = s_k + np.min(np.array([0.95*np.min(arr), 1]))*d_s


    print(np.min(np.array([0.95*np.min(arr), 1])))

    
    if(np.linalg.norm(r_D)<0.001 and np.dot(x_k.T,s_k)< 0.001 and np.linalg.norm(r_P) < 0.001):
        break
#     if (u < ep):
#         break
#     break

#     print(x_k)
#     print(y_k)
#     print(s_k)
#     break
    break
if (count == 1000):
    print("no optimal solution")
else :
    print(29 - np.dot(c.T,x_k))
# print(count)
