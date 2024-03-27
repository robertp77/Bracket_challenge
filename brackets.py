from random import random
#This code aims to generate 25 brackets for the ESPN bracket challenge. Change the following lists to edit how your brackets are Generated!

#ROUND 1
#This is who I think would win in a 7 game series for each matchup and predicted matchup

picks1={'UConn': 4, 'San Diego St': 0, 'Illinois': 4, 'Iowa St': 3, 'Carolina': 4, 'Alabama': 1, 'Clemson': 1, 'Arizona': 4, 'Houston': 4, 'Duke': 3, 'North Carolina St': 2, 'Marquette': 4, 'Purdue': 4, "Gonzaga": 0, 'Creighton': 4, 'Tennessee': 2}

#SUBSEQUENT ROUNDS
#change the team names if you had a different predicted team for these rounds

picks2={'UConn': 4, 'Illinois': 2, 'Carolina': 3, 'Arizona': 4, 'Houston': 4, 'Marquette': 2, 'Purdue': 4, 'Creighton': 2}
picks3={'UConn': 4, 'Arizona': 2, 'Houston': 1, 'Purdue': 4}
picks4={'UConn': 2, 'Purdue': 4}

#SEEDING
#Here is the custom seeding. It is mainly based on the actual seeds but I made some low seeded teams a bit higher to give them a better chance.

teams={'UConn': 1, 'San Diego St': 5, 'Illinois': 3, 'Iowa St': 2, 'Carolina': 1, 'Alabama': 4, 'Clemson': 5, 'Arizona': 2, 'Houston': 1, 'Duke': 4, 'North Carolina St': 5, 'Marquette': 2, 'Purdue': 1, "Gonzaga": 5, 'Creighton': 3, 'Tennessee': 2}

picks=[]
Brackets=[]
def pick(a,b,c,d):
    if random()<(b/(b+d)):
        return a
    else:
        return c
def pick2(a,b,f,h):
    if a==f and b==h:
        if random()<(picks2[f]/(picks2[f]+picks2[h])):
            return a
        else:
            return b
    elif a!=f:
        if random()<(picks2[f]+(teams[a]-teams[f]))/(picks2[f]+picks2[h]):
            return a
        else:
            return b 
    else:
        if random()<(picks2[h]+(teams[b]-teams[h]))/(picks2[f]+picks2[h]):
            return b
        else:
            return a 
def pick3(a,b,f,h):
    if a==f and b==h:
        if random()<(picks3[f]/7):
            return a
        else:
            return b
    elif a!=f:
        if random()<(picks3[f]+(teams[a]-teams[f]))/7:
            return a
        else:
            return b 
    else:
        if random()<(picks3[h]+(teams[b]-teams[h]))/7:
            return b
        else:
            return a 
def pick4(a,b,f,h):
    if a==f and b==h:
        if random()<(picks4[f]/7):
            return a
        else:
            return b
    elif a!=f:
        if random()<(picks4[f]+(teams[a]-teams[f]))/7:
            return a
        else:
            return b 
    else:
        if random()<(picks4[h]+(teams[b]-teams[h]))/7:
            return b
        else:
            return a 
for x in range(25):
    picks=[]
    for y in range(0,8):
        picks.append(pick(list(teams)[2*y],picks1[list(picks1)[2*y]],list(teams)[2*y+1],picks1[list(picks1)[2*y+1]]))
    for y in range(0,4):
        picks.append(pick2(picks[2*y],picks[2*y+1],list(picks2)[2*y],list(picks2)[2*y+1]))
    for y in range(0,2):
        picks.append(pick3(picks[8+2*y],picks[8+2*y+1],list(picks3)[2*y],list(picks3)[2*y+1]))
    picks.append(pick4(picks[12],picks[13],list(picks4)[0],list(picks4)[1]))
    print(picks)

