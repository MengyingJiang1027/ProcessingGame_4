# hint提示内容图片等待替换(白色底色比较好）


from Card import Card
from Game import Game
from Button import Button

def setup():
    global bg, game, frameCounter
    global inputDic, numList, imgList, resultList
    global scr_w, scr_h
    global blue, navy, red, green, grey
    global hint_btn
    
    bg = loadImage('./resources/bg.png')
    
    # 初始化字典
    blue = ''
    navy = ''
    red = ''
    green = ''
    grey = ''
    inputDic = {'Blue':blue, 'Navy':navy, 'Red':red, 'Green':green, 'Grey':grey}
    
    # 存入图案图片
    numList = []
    for i in range(5):
        numList.append(loadImage('./resources/img/' + str(i) + '.png'))
    
    # 存入单词图片
    letterList = []
    for i in range(5):
        letterList.append(loadImage('./resources/word/' + str(i) + '.png'))
     
    letterDic = {'Red':letterList[0], 'Grey':letterList[1], 'Blue':letterList[2], 'Green':letterList[3], 'Navy':letterList[4]}
    
    
    # 存入结果图片
    resultList = []
    for i in range(2):
        resultList.append(loadImage('./resources/result/' + str(i) + '.png'))
        
        
    # 卡片实例对象存入列表并且display
    imgList = []
    attributeDic = {1: 'Blue', 2: 'Navy', 3:'Green', 4:'Red', 5: 'Grey'}
    attributeList = [[1, 1, 2, 1, 1], [2, 2, 3, 2, 2], [3, 3, 5, 3, 3], [4, 4, 5, 4, 4]]
    for i in range(4):
        imgListRow = []
        for j in range(5):
            imgListRow.append(Card(50 + 150 * j, 240 + 100 * i, 100, 150, attributeDic[attributeList[i][j]], letterDic))
        imgList.append(imgListRow)
            

    scr_w = 960
    scr_h = 720
    frameCounter = 0
    game = Game()
    
    Chinese = createFont("LiSu", 35)
    textFont(Chinese)
    
    
    # 加入提示信息
    attr_hint_btn = {"btn_x":720,"btn_y":655,"btn_w":60,"btn_h":60,
                 "msg_x":375,"msg_y":230,"msg_w":500,"msg_h":400}
    
    hint_btn = Button(attr=attr_hint_btn,
                      imgs=["/resources/q_mark.png", "/resources/hint_msg.png"])

    size(960,720)
    
    
def draw():
    global bg, game, frameCounter
    global inputDic, numList, imgList, resultList
    global scr_w, scr_h
    global blue, navy, red, green, grey
    global hint_btn
    
        
    ######## 学生输入代码区域 ###########

    blue = 1
    navy = 2
    green = 3
    red = 4
    grey = 5



    
    ###### 学生输入代码区域###########
    

    inputDic['Blue'] = blue
    inputDic['Navy'] = navy
    inputDic['Red'] = red
    inputDic['Green'] = green
    inputDic['Grey'] = grey
    

    updateFrame(game,resultList, hint_btn)


def updateFrame(game,resultList, hint_btn):
    global frameCounter
    
    if game.isReady:
        frameCounter += 1
        if game.isWin:
            if frameCounter < 100:
                game.run(imgList, inputDic, numList)

            
            elif frameCounter < 200:
                tint(255, frameCounter  - 100)
                game.run(imgList, inputDic, numList)
                image(bg, 0, 0, scr_w, scr_h)
        
                
            else:
                tint(255, 120)
                game.run(imgList, inputDic, numList)
                image(bg, 0, 0, scr_w, scr_h)
                noTint()
                image(resultList[0],scr_w//2-50,scr_h//2-150,200,200)
                fill(255)
                textSize(40)
                text(u"恭喜你闯关成功！",scr_w//2-200,scr_h//2+125)
    

        else:
            if frameCounter < 100:
                game.run(imgList, inputDic, numList)
            
            elif frameCounter < 200:
                tint(255, frameCounter  - 100)
                game.run(imgList, inputDic, numList)
                image(bg, 0, 0, scr_w, scr_h)
                
            else:
                tint(255, 120)
                game.run(imgList, inputDic, numList)
                image(bg, 0, 0, scr_w, scr_h)
                noTint()
                image(resultList[1],scr_w//2-50,scr_h//2-150,200,200)
                fill(255)
                textSize(40)
                text(u"哎呀好像结果不正确呢，再想想",scr_w//2-200,scr_h//2+125)
               
        
    else:
        image(bg, 0, 0, scr_w, scr_h)
        game.run(imgList, inputDic, numList)
        hint_btn.show(mouseX,mouseY)
        

        
'''    
# 显示坐标系
def showMouseXY(scr_w,scr_h,coord_type=0):# display the current cord of X and Y
    fill(255)
    rectMode(CENTER)
    rect(mouseX,mouseY,5,5)
    point(mouseX,mouseY)
    if coord_type == 0: #origin at the center of the screen
        fill(255)
        textSize(15)
        text("x:"+str(mouseX-scr_w/2),mouseX+15,mouseY)
        text("y:"+str(scr_h/2-mouseY),mouseX+60,mouseY)
    else: # processing's default coord-sys
        fill(255)
        textSize(15)
        text("x:" + str(mouseX), mouseX+15, mouseY)
        text("y:" + str(mouseY), mouseX+60, mouseY)
'''
        
    
        
    
    

    
