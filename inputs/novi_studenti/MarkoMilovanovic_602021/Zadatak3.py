def UnesiMatricu(n):
    M = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = int(input())
    return M
def Transformisi(M):
    #nova mat
    M2 = [[0 for i in range(len(M))] for i in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
             M2[i][j] = M[i][j]
            

    #glavna linija
    for i in range(len(M2)):
        M2[i][i] = 1

    #transformisi
    for i in range(len(M)):
        for j in range(len(M)):
            #print(str(i+1)+"  " + str(j+1)+"=="+str(M[i][j]))
            if M[i][j] == 1 and i!=j:
                for k in range(len(M)):
                    if M[j][k] == 1 and j!=k and i!=k:
                        #print(str(i+1)+" je u rel sa" + str(j+1) +", pa je " +str(i+1)+" je u rel sa" + str(k+1))
                        M2[i][k] = 1
    print(M2)
    #print(M)
            
    

n = int(input())
M = UnesiMatricu(n)
#print(M)
Transformisi(M)
