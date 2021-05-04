import sys
import time
import random

class Expression:
    
    def __init__(self):
        self.noOfVariables=0
        self.expression=[]
        self.maxTries=0
 

    def setMaxTries(self,value):
        self.maxTries=value
        
    
    def getMaxTries(self):
        return self.maxTries
          
    def getExpression(self):
        return self.expression
        
    def setNoOfVariables(self,value):
        self.noOfVariables=value
        
    def getNoOfVariables(self)-> int:
        return self.noOfVariables
    
    def stringToExpressionInputConveter(self,expression: list):
        closure=[]
        for item in expression:
            item=item.strip('\n')
            if item:
                val=int(item)
                if val==0:
                  break
                closure.append(val)
        self.expression.append(closure)
        

def generateRandomTruthAssignment(noOfVariables: int):
    l = random.choices([True, False], k=noOfVariables)
    return l

def checkMAxSatisfiability(expression:Expression,solution: list):
    noOfExpectedClosureSatisfiability=int(7/8*len(expression.getExpression()))
    noOfSatisfiedClosures=0
    for closure in expression.getExpression():
        for literal in closure:
            if (literal>0 and solution[abs(literal)-1]) or (literal<0 and not(solution[abs(literal)-1])):
                noOfSatisfiedClosures=noOfSatisfiedClosures+1
                break
            
        if noOfSatisfiedClosures>=noOfExpectedClosureSatisfiability:
            return True
    return False  


def randomisedAlgorithm(expression:Expression):
    for i in range(expression.getMaxTries()):
        randomlyGeneratedValues=generateRandomTruthAssignment(expression.getNoOfVariables())
        if checkMAxSatisfiability(expression,randomlyGeneratedValues):
            return randomlyGeneratedValues
    return []
      
    


if __name__ =="__main__":
    try:
        
        expression=Expression()
        expression.setMaxTries(int(sys.argv[2]))
        
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            noOfVariables=line.split(" ")[2]
            expression.setNoOfVariables(int(noOfVariables))
            line=file.readline()
            
            while line:
                list=line.split(" ")
                expression.stringToExpressionInputConveter(list)
                line=file.readline()
                
                
            print('Algorithm Started::')
            seconds = time.time()
            l=randomisedAlgorithm(expression)
            seconds = seconds-time.time()
            if len(l)==0:
                print('No Satified Answers found to SAT problem ')
            else:
                print('Answer to SAT problem :'+str(l))
            print('Finished::')
            print('Running Time in second'+str(seconds))
            
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python Dpll.py <filename>  <Max no of tries>')