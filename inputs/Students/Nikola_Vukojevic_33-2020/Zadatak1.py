def sabiranje(lista):
    nov = []
    visak = 0
    
    for i in range(-1, -(big+1), -1):
        pol = 10
        
        r = int(l_huge[i]) + int(l_smol[i]) + visak
        
            
        if (r >= pol):
            j = r % 10
            d = r // 10
            visak = d
            nov.insert(0, str(j))
        else:
            nov.insert(0, str(r))
            
            visak = 0

    


            

    return nov



    
            
            
        
        
    




#unos
p = input("1. string: ")
d = input("2. string: ")
o = input("Operacija: ")

pl = list(p)
pd = list(d)



#duzina
p_duzina = len(p)
d_duzina = len(d)
big = max(p_duzina, d_duzina) #za duzinu
smol = min(p, d) #najmanji string
l_smol = list(smol) #najmanji u listu
duzina_najmanjeg = len(l_smol)
huge = max(p, d) #najveci string
l_huge = list(huge)
duzina_najveceg = len(huge)


#dopunjavanje manjeg da ima isti broj cifara kao veci

while(duzina_najmanjeg < duzina_najveceg):
    l_smol.insert(0, "0")
    duzina_najmanjeg += 1

if (o == "+"):
    neko = sabiranje(l_huge)
    r = int(l_huge[0]) + int(l_smol[0]) 
    if (r >= 10):
        j = r % 10
        d = r // 10
        neko[0] = str(j)
        neko.insert(0, str(d))
    print(neko)


    

    










