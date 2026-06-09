import dsplab2task1
import dsplab2task2
import dsplab2task3

# Variant 6
    

class dsplab2:
    def task1(self):
        self.task1_handler.init()
        self.task1_handler.run()
    
    def task2(self):
        self.task2_handler.init()
        self.task2_handler.run()
    
    def task3(self):
        self.task3_handler.init()
        self.task3_handler.run()
        
    def __init__(self):
        self.task1_handler = dsplab2task1.dsplab2task1()
        self.task2_handler = dsplab2task2.dsplab2task2()
        self.task3_handler = dsplab2task3.dsplab2task3()
        

lab = dsplab2()
lab.task1()
lab.task2()
lab.task3()

