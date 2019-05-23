#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preferencia homens:
abe: abi, eve, cath, ivy, jan, dee, fay, bea, hope, gay
bob: cath, hope, abi, dee, eve, fay, bea, jan, ivy, gay
col: hope, eve, abi, dee, bea, fay, ivy, gay, cath, jan
dan: ivy, fay, dee, gay, hope, eve, jan, bea, cath, abi
ed: jan, dee, bea, cath, fay, eve, abi, ivy, hope, gay
fred: bea, abi, dee, gay, eve, ivy, cath, jan, hope, fay
gav: gay, eve, ivy, bea, cath, abi, dee, hope, jan, fay
hal: abi, eve, hope, fay, ivy, cath, jan, bea, gay, dee
ian: hope, cath, dee, gay, bea, abi, fay, ivy, jan, eve
jon: abi, fay, jan, gay, eve, bea, dee, cath, ivy, hope


Preferencia mulheres:
abi: "bob", "fred", "jon", "gav", "ian", "abe", "dan", "ed", "col", "hal"
bea: "bob", "abe", "col", "fred", "gav", "dan", "ian", "ed", "jon", "hal"
cath: "fred", "bob", "ed", "gav", "hal", "col", "ian", "abe", "dan", "jon"
dee: "fred", "jon", "col", "abe", "ian", "hal", "gav", "dan", "bob", "ed"
eve: "jon", "hal", "fred", "dan", "abe", "gav", "col", "ed", "ian", "bob"
fay: "bob", "abe", "ed", "ian", "jon", "dan", "fred", "gav", "col", "hal"
gay: "jon", "gav", "hal", "fred", "bob", "abe", "col", "ed", "dan", "ian"
hope: "gav", "jon", "bob", "abe", "ian", "dan", "hal", "ed", "col", "fred"
ivy: "ian", "col", "hal", "gav", "fred", "bob", "abe", "ed", "jon", "dan"
jan: "ed", "hal", "gav", "abe", "bob", "jon", "col", "ian", "fred", "dan"

"""

def Set_PList(): 
    PMen = dict()
    for boy in ("abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"):
        PMen[boy]=[boy]
        PMen[boy].remove(boy)
        
    for girl in ("abi", "eve", "cath", "ivy", "jan", "dee", "fay", "bea", "hope", "gay"):
        PMen["abe"].append(girl)
    for girl in ("cath", "hope", "abi", "dee", "eve", "fay", "bea", "jan", "ivy", "gay"):
        PMen["bob"].append(girl)
    for girl in ( "hope", "eve", "abi", "dee", "bea", "fay", "ivy", "gay", "cath", "jan"):
        PMen["col"].append(girl)
    for girl in ("ivy", "fay", "dee", "gay", "hope", "eve", "jan", "bea", "cath", "abi"):
        PMen["dan"].append(girl)
    for girl in ("jan", "dee", "bea", "cath", "fay", "eve", "abi", "ivy", "hope", "gay"):
        PMen["ed"].append(girl)
    for girl in ("bea", "abi", "dee", "gay", "eve", "ivy", "cath", "jan", "hope", "fay"):
        PMen["fred"].append(girl)
    for girl in ("gay", "eve", "ivy", "bea", "cath", "abi", "dee", "hope", "jan", "fay"):
        PMen["gav"].append(girl)
    for girl in ("abi", "eve", "hope", "fay", "ivy", "cath", "jan", "bea", "gay", "dee"):
        PMen["hal"].append(girl)
    for girl in ("abi", "eve", "hope", "fay", "ivy", "cath", "jan", "bea", "gay", "dee"):
        PMen["hal"].append(girl)
    for girl in ("hope", "cath", "dee", "gay", "bea", "abi", "fay", "ivy", "jan", "eve"):
        PMen["ian"].append(girl)     
    for girl in ("abi", "fay", "jan", "gay", "eve", "bea", "dee", "cath", "ivy", "hope"):
        PMen["jon"].append(girl)  


    PWom = dict()
    for girl in ("abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"):
        PWom[girl]=[girl]
        PWom[girl].remove(girl)

    for boy in ("bob", "fred", "jon", "gav", "ian", "abe", "dan", "ed", "col", "hal"):
        PWom["abi"].append(boy)
    for boy in ("bob", "abe", "col", "fred", "gav", "dan", "ian", "ed", "jon", "hal"):
        PWom["bea"].append(boy)
    for boy in ("fred", "bob", "ed", "gav", "hal", "col", "ian", "abe", "dan", "jon"):
        PWom["cath"].append(boy)
    for boy in ("fred", "jon", "col", "abe", "ian", "hal", "gav", "dan", "bob", "ed"):
        PWom["dee"].append(boy)
    for boy in ("jon", "hal", "fred", "dan", "abe", "gav", "col", "ed", "ian", "bob"):
        PWom["eve"].append(boy)
    for boy in ("bob", "abe", "ed", "ian", "jon", "dan", "fred", "gav", "col", "hal"):
        PWom["fay"].append(boy)
    for boy in ("jon", "gav", "hal", "fred", "bob", "abe", "col", "ed", "dan", "ian"):
        PWom["gay"].append(boy)
    for boy in ("gav", "jon", "bob", "abe", "ian", "dan", "hal", "ed", "col", "fred"):
        PWom["hope"].append(boy)
    for boy in ("ian", "col", "hal", "gav", "fred", "bob", "abe", "ed", "jon", "dan"):
        PWom["ivy"].append(boy)
    for boy in ("ed", "hal", "gav", "abe", "bob", "jon", "col", "ian", "fred", "dan"):
        PWom["jan"].append(boy)
    return PMen, PWom


def value(PersonName, PersonList):
    count = 0
    while PersonName != PersonList[count]:
        count = count + 1
    return count


def Gale_Shappley(Pman, Pwom):
    
    #lista de "casados"
    Engaged = []
    
    #listas que armazemam os homens e mulheres livres
    MenNotEngaged = []
    WomenNotEngaged = []
    
    #incializa as listas acima com todos os nomes
    for Person in Pman:
        MenNotEngaged.append(Person)
    for Person in Pwom:
        WomenNotEngaged.append(Person)
  
    while len(MenNotEngaged) != 0:
        
        Man = MenNotEngaged[0]
        Woman = Pman[Man][0]
       
        if Woman in WomenNotEngaged:
            Engaged.append((Man, Woman))
            WomenNotEngaged.remove(Woman)
            MenNotEngaged.remove(Man)
            
        else:
            for (u,v) in Engaged:
                if v == Woman:
                    Current_Husband = u 

            if value(Man, Pwom[Woman]) > value(Current_Husband, Pwom[Woman]):
                Pman[Man].remove(Woman)
                
            else:
                Engaged.remove((Current_Husband, Woman))
                MenNotEngaged.append(Current_Husband)
                Pman[Current_Husband].remove(Woman)

                MenNotEngaged.remove(Man)
                Engaged.append((Man, Woman))
            
    return Engaged
                


Pman, Pwom = Set_PList()
CasadosMenChoice = Gale_Shappley(Pman,Pwom)

CasadosWomenChoice = Gale_Shappley(Pwom,Pman)
print("Men First: ",CasadosMenChoice, "\nWomen First: ",CasadosWomenChoice)













    
