import RPi.GPIO as GPIO
import time
IN1 = 37#1 right
IN2 = 35#
IN3 = 33#2 left
IN4 = 31#
TRIG = 3#i                     
ECHO = 5
BEE = 23
R_LIGHT = 40
G_LIGHT = 38
B_LIGHT = 36
class Car():
    '''
        a class about Car action
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
        self.LIGHT.R_LIGHT()
        
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
        self.LIGHT.W_LIGHT()#倒车灯
    def turn_left(self):
        print('turn_left')
        self.LIGHT.C_LIGHT()
        GPIO.output(IN1,True)
        GPIO.output(IN2,False)
        GPIO.output(IN3,False)
        GPIO.output(IN4,False)
        self.LIGHT.B_LIGHT()#转向灯
    def turn_right(self):
        print('turn_right')
        self.LIGHT.C_LIGHT()
        GPIO.output(IN3,True)
        GPIO.output(IN1,False)
        GPIO.output(IN2,False)
        GPIO.output(IN4,False)
        self.LIGHT.B_LIGHT()
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
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.action = Car()
        self.BEE = BEE
    def get(self):
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
        if self.get()<5:
            self.action.stop()
            self.ring()
            return 0
    def ring(self):
        GPIO.output(BEE,GPIO.LOW)
        time.sleep(1)
        GPIO.output(BEE,GPIO.HIGH)
class car_light():
    def R_LIGHT(self):
        GPIO.output(R_LIGHT,GPIO.HIGH)
    def G_LIGHT(self):
        GPIO.output(G_LIGHT,GPIO.HIGH)
    def B_LIGHT(self):
        GPIO.output(B_LIGHT,GPIO.HIGH)
    def C_LIGHT(self):
        GPIO.output(R_LIGHT,GPIO.LOW)
        GPIO.output(G_LIGHT,GPIO.LOW)
        GPIO.output(B_LIGHT,GPIO.LOW)
    def W_LIGHT(self):
        GPIO.output(R_LIGHT,GPIO.HIGH)
        GPIO.output(G_LIGHT,GPIO.HIGH)
        GPIO.output(B_LIGHT,GPIO.HIGH)
