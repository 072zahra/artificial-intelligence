percept= ["ZAHRA","ANA","SHA","Saad"]
state = ["happy","Sad","angry","normal"]
rule = ["smile","cry","frown","watch ronaldo"]
def GetState(cPercept):
    index=-1
    for p in percept:
        index=index+1
        if p==cPercept:
            return state[index]
def GetRule(cState):
    index=-1
    for s in state:
        index=index+1
        if s==cState:
            return rule[index]
def SimpleReflexAgent(cPercept):
    return GetRule(GetState(cPercept))
print ("MENU: ")
print ("  0:ZAHRA 1:ANA 2:SHA 3:Saad")
print (SimpleReflexAgent(percept[int(input("Input Number :"))]))       



