import RPi.GPIO as GPIO
import time
from config import *
'''此模块为小车的各种定义'''
'''封装小车的相关方法，方便其他模块直接调用'''


class Car():
    '''
        此类是小车的类，定义了小车的属性和相关方法
    '''
    def __init__(self):
        '''
            初始化，将函数的的对应方法附上电机的GPIO口号
            将方法对应上LED灯对应的GPIO口号
            初始化，将对象的LIGHT方法实例为car_light类的对象
        '''
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4
        self.R_LIGHT = R_LIGHT
        self.B_LIGHT = B_LIGHT
        self.G_LIGHT = G_LIGHT
        self.LIGHT = car_light()
    def forward(self):
        '''
         提供小车前进的方法
        '''
        self.LIGHT.C_LIGHT()#清除掉灯光信息
        print('forward')
        GPIO.output(IN3,True)
        GPIO.output(IN4,False)
        GPIO.output(IN1,True)
        GPIO.output(IN2,False)
        #GPIO.output(G_LIGHT,True)
        self.LIGHT.G_LIGHT()
    def stop(self):
        '''
        提供小车停止的方法
        '''
        print('stop')
        self.LIGHT.C_LIGHT()
        GPIO.output(IN3,False)
        GPIO.output(IN1,False)
        GPIO.output(IN2,False)
        GPIO.output(IN4,False)
        #GPIO.output(R_LIGHT,True)
        self.LIGHT.R_LIGHT()#停车灯红色
        
    def back(self):
        '''
        提供小车后退的方法
        '''
        print('back')
        self.LIGHT.C_LIGHT()
        GPIO.output(IN4,True)
        GPIO.output(IN2,True)
        GPIO.output(IN1,False)
        GPIO.output(IN3,False)
        self.LIGHT.W_LIGHT()#倒车灯白色
    def turn_left(self):
        print('turn_left')
        self.LIGHT.C_LIGHT()
        GPIO.output(IN1,True)
        GPIO.output(IN2,False)
        GPIO.output(IN3,False)
        GPIO.output(IN4,False)
        self.LIGHT.B_LIGHT()#转向灯蓝色
    def turn_right(self):
        print('turn_right')
        self.LIGHT.C_LIGHT()
        GPIO.output(IN3,True)
        GPIO.output(IN1,False)
        GPIO.output(IN2,False)
        GPIO.output(IN4,False)
        self.LIGHT.B_LIGHT()#转向灯蓝色
class dangerous():
    '''
        提供一个，在危险的时候小车的动作
    '''
    def __init__(self):
        '''
        初始化，将实例的TRIG方法，和ECHO方法对越该模块的GPIO接口
        将实例的action 方法作为Car类的实例
        将实例的BEE方法对应蜂鸣器的GPIO接口
        '''
        self.TRIG = TRIG    #添加实例的属性
        self.ECHO = ECHO
        self.action = Car()
        self.BEE = BEE
    def get(self):
        '''
        通过位于接口上的的超声波传感器，获取到小车距离障碍物的距离
        :return:小车距离前方障碍物的距离
        '''
        GPIO.output(TRIG,True)
        time.sleep(0.00015)
        GPIO.output(TRIG,False)
        while not GPIO.input(ECHO):
            pass
        t1 = time.time()
        while GPIO.input(ECHO):
            pass
        t2 = time.time()
        return (t2-t1)*340 * 100/2
    def check(self):
        '''
        传入实例的get()方法的返回值判断小车是否遇到危险
        并操作实例的ring，和action中的stop()方法
        :return: 0
        '''
        while True:
            if self.get()<5:
                self.action.stop()
                self.ring()
                return 0
    def ring(self):
        '''
        调用会响
        :return:
        '''
        GPIO.output(BEE,GPIO.LOW)
        time.sleep(1)
        GPIO.output(BEE,GPIO.HIGH)
class car_light():
    '''
    小车灯光的的类，以小车中LED灯光矩阵为对象
    '''
    def R_LIGHT(self):
        '''
        红灯
        :return:
        '''
        GPIO.output(R_LIGHT,GPIO.HIGH)
    def G_LIGHT(self):
        '''
        绿灯
        '''
        GPIO.output(G_LIGHT,GPIO.HIGH)
    def B_LIGHT(self):
        '''
        蓝灯
        :return:
        '''
        GPIO.output(B_LIGHT,GPIO.HIGH)
    def C_LIGHT(self):
        '''
        关灯
        :return:
        '''
        GPIO.output(R_LIGHT,GPIO.LOW)
        GPIO.output(G_LIGHT,GPIO.LOW)
        GPIO.output(B_LIGHT,GPIO.LOW)
    def W_LIGHT(self):
        '''
        白灯
        :return:
        '''
        GPIO.output(R_LIGHT,GPIO.HIGH)
        GPIO.output(G_LIGHT,GPIO.HIGH)
        GPIO.output(B_LIGHT,GPIO.HIGH)
