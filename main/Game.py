from processing import *

class Game(object):
    def __init__(self):
        self.isReady = False
        self.isWin = False
                
    def check(self,inputDic):
        for key in inputDic:
            if inputDic[key] != '':
                self.isReady = True
            elif inputDic[key] == '' or type(key) is not int or (key > 5 or key < 0):
                inputDic[key] = 11
                self.isWin = False
            
        if inputDic['Blue'] == 1 and inputDic['Navy'] == 2 and inputDic['Green'] == 3 and inputDic['Red'] == 4 and inputDic['Grey'] == 5:
            self.isWin = True
    
                            
    def showResult(self, imgList, inputDic, numList):
        if not self.isReady:
            for imgs in imgList:
                for img in imgs:
                    img.display()
        
        else:
            for imgs in imgList:
                for img in imgs:
                    img.run(inputDic, numList)
            if self.isWin:
                print('yes')
            else:
                print('no')
        
    
    def run(self, imgList, inputDic, numList):
        self.check(inputDic)
        self.showResult(imgList, inputDic, numList)
