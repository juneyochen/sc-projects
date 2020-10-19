"""
File: stanCode practice
Name: June-Yo Chen
----------------------
This file draws a picture about a meme.
I think it is very hard for people to draw a picture with python...
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow
window = GWindow(800, 600, title='stanCode practice')  # create a window for drawing

def main():
    """

    """
    #左上角，迷因文字第一段
    square1 = GRect(400, 300, x=0, y=0)
    window.add(square1)
    word1 = GLabel('上stanCode前的我', x=40, y=150)
    word1.font = 'Cowrier-30-italic'
    window.add(word1)
    word1_2 = GLabel('code是啥?可以吃嗎?', x=40, y=180)
    word1_2.font = 'Cowrier-20-italic'
    window.add(word1_2)

    #左下角，迷因文字第二段
    square2 = GRect(400, 300, x=0, y=300)
    window.add(square2)
    word2 = GLabel('上stanCode後的我', x=40, y=450)
    word2.font = 'Cowrier-30-italic'
    window.add(word2)
    word2_2 = GLabel('考試都考100分~', x=40, y=480)
    word2_2.font = 'Cowrier-20-italic'
    window.add(word2_2)

    #右上角，迷因圖片第一張
    #背景
    suqare_background1 = GRect(400, 220, x=400, y=0)
    suqare_background1.filled = True
    suqare_background1.fill_color = 'wheat'
    window.add(suqare_background1)
    suqare_background2 = GRect(400, 80, x=400, y=220)
    window.add(suqare_background2)
    suqare_background2.filled = True
    suqare_background2.fill_color = 'gray'

    # 小茶几
    desk6 = GRect(10, 50, x=405, y=210)
    desk6.filled = True
    desk6.fill_color = 'brown'
    window.add(desk6)
    desk7 = GRect(10, 50, x=465, y=210)
    desk7.filled = True
    desk7.fill_color = 'brown'
    window.add(desk7)
    desk1 = GPolygon()
    desk1.add_vertex((500, 230))
    desk1.add_vertex((480, 200))
    desk1.add_vertex((400, 200))
    desk1.add_vertex((420, 230))
    desk1.filled = True
    desk1.fill_color = 'brown'
    window.add(desk1)
    desk2 = GRect(80, 10, x=420, y=230)
    desk2.filled = True
    desk2.fill_color = 'brown'
    window.add(desk2)
    desk3 = GPolygon()
    desk3.add_vertex((420, 230))
    desk3.add_vertex((420, 240))
    desk3.add_vertex((400, 210))
    desk3.add_vertex((400, 200))
    desk3.filled = True
    desk3.fill_color = 'brown'
    window.add(desk3)
    desk4 = GRect(10, 50, x=485, y=240)
    desk4.filled = True
    desk4.fill_color = 'brown'
    window.add(desk4)
    desk5 = GRect(10, 50, x=425, y=240)
    desk5.filled = True
    desk5.fill_color = 'brown'
    window.add(desk5)

    # 檯燈
    lamp = GPolygon()
    lamp.add_vertex((440, 100))
    lamp.add_vertex((460, 100))
    lamp.add_vertex((480, 160))
    lamp.add_vertex((420, 160))
    lamp.filled = True
    lamp.fill_color = 'lightyellow'
    window.add(lamp)
    lamp2 = GRect(10,20, x=445, y=160)
    lamp2.filled= True
    lamp2.fill_color = 'grey'
    window.add(lamp2)
    lamp3 = GOval(30, 10, x=435, y=180)
    lamp3.filled = True
    lamp3.fill_color = 'lightyellow'
    window.add(lamp3)
    lamp4 = GRect(30, 30, x=435, y=185)
    lamp4.filled = True
    lamp4.fill_color = 'lightyellow'
    window.add(lamp4)

    # 沙發
    sofa1 = GRect(250, 100, x=550, y=100)
    sofa1.filled= True
    sofa1.fill_color = 'darkgray'
    window.add(sofa1)
    sofa2 = GPolygon()
    sofa2.add_vertex((550, 200))
    sofa2.add_vertex((800, 200))
    sofa2.add_vertex((800, 240))
    sofa2.add_vertex((600, 240))
    sofa2.filled = True
    sofa2.fill_color = 'darkgray'
    window.add(sofa2)
    sofa3 = GPolygon()
    sofa3.add_vertex((550, 100))
    sofa3.add_vertex((550, 200))
    sofa3.add_vertex((600, 240))
    sofa3.add_vertex((600, 300))
    sofa3.add_vertex((520, 240))
    sofa3.add_vertex((520, 60))
    sofa3.filled = True
    sofa3.fill_color = 'darkgray'
    window.add(sofa3)
    sofa4 = GPolygon()
    sofa4.add_vertex((550, 100))
    sofa4.add_vertex((520, 60))
    sofa4.add_vertex((800, 60))
    sofa4.add_vertex((800, 100))
    sofa4.filled = True
    sofa4.fill_color = 'darkgray'
    window.add(sofa4)
    sofa5 = GPolygon()
    sofa5.add_vertex((800, 240))
    sofa5.add_vertex((800, 300))
    sofa5.add_vertex((600, 300))
    sofa5.add_vertex((600, 240))
    sofa5.filled = True
    sofa5.fill_color = 'darkgray'
    window.add(sofa5)

    # 右上圖的人
    neck = GRect(20, 10, x=660, y=100)
    neck.filled = True
    neck.fill_color = 'peachpuff'
    window.add(neck)
    face = GOval(40, 60, x=650, y=45)
    face.filled = True
    face.fill_color = 'peachpuff'
    window.add(face)
    left_eye = GLine(660, 65, 670, 60)
    window.add(left_eye)
    right_eye = GLine(685, 65, 675, 60)
    window.add(right_eye)
    mouth = GLine(665, 90, 680, 90)
    window.add(mouth)
    body_1 = GRect(80, 80, x=630, y=110)
    body_1.filled = True
    body_1.fill_color = 'navy'
    window.add(body_1)
    body_2 = GPolygon()
    body_2.add_vertex((630, 110))
    body_2.add_vertex((570, 150))
    body_2.add_vertex((580, 162))
    body_2.add_vertex((630, 130))
    body_2.filled = True
    body_2.fill_color = 'navy'
    window.add(body_2)
    hand_1 = GOval(20,20, x=560, y=150)
    hand_1.filled = True
    hand_1.fill_color = 'peachpuff'
    window.add(hand_1)
    body_3 = GPolygon()
    body_3.add_vertex((710, 110))
    body_3.add_vertex((780, 133))
    body_3.add_vertex((765, 148))
    body_3.add_vertex((710, 130))
    body_3.filled = True
    body_3.fill_color = 'navy'
    window.add(body_3)
    hand_2 = GOval(20, 20, x=765, y=133)
    hand_2.filled = True
    hand_2.fill_color = 'peachpuff'
    window.add(hand_2)
    leg_2 = GPolygon()
    leg_2.add_vertex((730, 215))
    leg_2.add_vertex((740, 205))
    leg_2.add_vertex((790, 215))
    leg_2.add_vertex((780, 225))
    leg_2.filled = True
    leg_2.fill_color = 'peachpuff'
    window.add(leg_2)
    shoes_2 = GPolygon()
    shoes_2.add_vertex((780, 225))
    shoes_2.add_vertex((790, 200))
    shoes_2.add_vertex((800, 202))
    shoes_2.add_vertex((790, 228))
    shoes_2.filled = True
    shoes_2.fill_color = 'gold'
    window.add(shoes_2)
    body_4 = GPolygon()
    body_4.add_vertex((630, 190))
    body_4.add_vertex((630, 230))
    body_4.add_vertex((670, 230))
    body_4.add_vertex((690, 215))
    body_4.add_vertex((735, 220))
    body_4.add_vertex((760, 200))
    body_4.add_vertex((710, 190))
    body_4.filled = True
    body_4.fill_color = 'cadetblue'
    window.add(body_4)
    leg_1 = GRect(20, 50, x=640, y=230)
    leg_1.filled = True
    leg_1.fill_color ='peachpuff'
    window.add(leg_1)
    shoes_1 = GOval(33, 10, x= 635, y=278)
    shoes_1.filled = True
    shoes_1.fill_color = 'gold'
    window.add(shoes_1)

    # 右下圖的人
    neck2 = GRect(35, 30, x=582, y=495)
    neck2.filled = True
    neck2.fill_color = 'peachpuff'
    window.add(neck2)
    face2 = GOval(100, 150, x=550, y=350)
    face2.filled = True
    face2.fill_color = 'peachpuff'
    window.add(face2)
    hair = GPolygon()
    hair.add_vertex((555, 390))
    hair.add_vertex((555, 330))
    hair.add_vertex((565, 350))
    hair.add_vertex((575, 330))
    hair.add_vertex((585, 350))
    hair.add_vertex((595, 330))
    hair.add_vertex((605, 350))
    hair.add_vertex((615, 330))
    hair.add_vertex((625, 350))
    hair.add_vertex((635, 330))
    hair.add_vertex((645, 390))
    hair.filled = True
    hair.fill_color = 'yellow'
    window.add(hair)
    eye1 = GLine(570, 410, 590, 420)
    window.add(eye1)
    eye1_2 = GLine(590, 420, 570, 430)
    window.add(eye1_2)
    eye2 = GLine(610, 430, 620, 410)
    window.add(eye2)
    eye2_2 = GLine(620, 410, 630, 430)
    window.add(eye2_2)
    mouth2 = GOval(10, 10, x=595, y=470)
    mouth2.filled = True
    window.add(mouth2)
    body1 = GPolygon()
    body1.add_vertex((450, 600))
    body1.add_vertex((500, 550))
    body1.add_vertex((582, 525))
    body1.add_vertex((617, 525))
    body1.add_vertex((700, 550))
    body1.add_vertex((750, 600))
    body1.filled = True
    body1.fill_color = 'lightblue'
    window.add(body1)
    arm = GPolygon()
    arm.add_vertex((750, 600))
    arm.add_vertex((680, 600))
    arm.add_vertex((660, 580))
    arm.add_vertex((660, 550))
    window.add(arm)
    finger5 = GOval(20, 50, x=640, y=480)
    finger5.filled = True
    finger5.fill_color = 'peachpuff'
    window.add(finger5)
    hand1 = GOval(50, 80, x=630, y=520)
    hand1.filled = True
    hand1.fill_color = 'peachpuff'
    window.add(hand1)
    finger1 = GOval(50, 20, x=610, y=520)
    finger1.filled = True
    finger1.fill_color = 'peachpuff'
    window.add(finger1)
    finger2 = GOval(50, 20, x=610, y=540)
    finger2.filled = True
    finger2.fill_color = 'peachpuff'
    window.add(finger2)
    finger3 = GOval(50, 20, x=610, y=560)
    finger3.filled = True
    finger3.fill_color = 'peachpuff'
    window.add(finger3)
    finger4 = GOval(50, 20, x=610, y=580)
    finger4.filled = True
    finger4.fill_color = 'peachpuff'
    window.add(finger4)









if __name__ == '__main__':
    main()
