import random
import os
import sys
#import numpy
#from numpy import array

class worker(object):
    def __init__(self,ID):
        self.ID = ID
        self.s1 = random.uniform(1,5)
        self.s2 = random.uniform(1,5)        
        self.s3 = random.uniform(1,5)
        self.evaluation = 0
        self.age = random.randint(1,4)
        self.rank = 0
   
    def step(self):
        self.age = self.age + 1        
            
class firm(object):
    def __init__(self):
        self.w_agents = [worker(x) for x in range(10)]
        self.ranking = []
        self.workforce = []
        self.job = 0
        self.totalworkforce_RAN = []
        self.totalworkforce_UOO = []

    def step_model_ranking(self):
        self.evaluate_and_rank()
        self.fire_and_hire()
    
    def step_model_uporout(self):
        self.opportunity_and_perform()
        self.job_open_fill()        
        
    def evaluate_and_rank(self):
        self.ranking = []
        self.workforce = []
        for w_agent in self.w_agents:
            self.workforce.append(w_agent.s1 + w_agent.s2 + w_agent.s3)
            w_agent.evaluation = w_agent.s1 + w_agent.s2 + w_agent.s3 + random.randint(-5,5)
            self.ranking.append(w_agent.evaluation)
    
    def fire_and_hire(self):
        for w_agent in self.w_agents:
                if w_agent.evaluation == min(self.ranking):
                    z = w_agent.ID
                    self.ranking.remove(min(self.ranking))
                    w_agent.__init__(z)
                    w_agent.evaluation = w_agent.s1 + w_agent.s2 + w_agent.s3 + random.randint(-5,5)
                    self.ranking.append(w_agent.evaluation)
                    break
                    
    def opportunity_and_perform(self):
        self.ranking = []
        self.workforce = []
        for w_agent in self.w_agents:
            w_agent.step()
            s = [w_agent.s1,w_agent.s2,w_agent.s3]
            self.workforce.append(w_agent.s1 + w_agent.s2 + w_agent.s3)
            w_agent.evaluation = (w_agent.s1 + w_agent.s2 + w_agent.s3)
            self.ranking.append(w_agent.evaluation)
    
    def job_open_fill(self):   
        for w_agent in self.w_agents:
#         data = array(self.ranking)
            if w_agent.evaluation > int((sum(self.ranking))/10):
                w_agent.rank = 1
                w_agent.age  = 0
            if w_agent.rank == 0 and w_agent.age > 5:
                z = w_agent.ID
                w_agent.__init__(z)
                w_agent.age = 0
            if w_agent.rank == 1 and w_agent.age > 25:
                z = w_agent.ID
                w_agent.__init__(z)
                w_agent.age = 0
                break
                                             
    def run(self):
        for step in range (1000):
            self.step_model_ranking()
            self.totalworkforce_RAN.append(sum(self.workforce))
        self.__init__
        self.step_model_uporout()
        i = 0
        for w_agent in self.w_agents:
            if i < 3:
                w_agent.rank = 1
                i = i + 1
        for step in range (1000):
            self.step_model_uporout()
            self.totalworkforce_UOO.append(sum(self.workforce))
        name = self.FormReportFileName()
        self.save_file(name)

    def save_file(self,name): #f(TAKE NAME OF FILE AND SAVE IT IN FOLDER)        
        
        report=open(name,'w')
        lines = []
        lines.append('Step;TotalWorkForce_RAN;TotalWorkForce_UOO;\n')
        for i in range(1000):
            aline = '%s;%i;%i;\n' %(i,self.totalworkforce_RAN[i],self.totalworkforce_UOO[i])
            lines.append(aline)
        report.writelines(lines)
        report.close()
    
    def FormReportFileName(self): #F(CREATE FOLDER AND ENABLE NEW FILE + NAME)

        dirName = "Firms Model"
        numFiles = 0
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        else:
            for f in os.listdir(dirName):
                if os.path.isfile(os.path.join(dirName, f)):
                    numFiles += 1

        reportFileName = dirName + "\\" + "Report " +str(numFiles) + ".txt"
        return reportFileName                     


if __name__ == '__main__':   #LETS GET THE SIMULATION RUNNING...
    times = 10 #int(sys.argv[1:][0])
    for t in range(times):
        runsim = firm()
        runsim.run()
    print "Done!"
