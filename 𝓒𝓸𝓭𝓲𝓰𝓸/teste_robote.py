from machine import Pin, PWM
import time
from time import sleep

in1 = Pin(18, Pin.OUT)
in2 = Pin(33, Pin.OUT)
in3 = Pin(4, Pin.OUT)
in4 = Pin(21, Pin.OUT)
ena = PWM(Pin(23), 500)
enb = PWM(Pin(15), 500)


def frente_motor1(velocidade):
    in1.value(1)# Ligando para indicar o sentido do movimento do motor 1, a velocidade sera alterada conforme o adequado.
    in2.value(0)# Desligado, pois indica o outro sentido (para trás).
    ena.duty_u16(velocidade)# O "u16" indica o máximo e mínimo de velocidade, nesse caso de 0 a 65535.
    
def frente_motor2(velocidade):
    in3.value(1)# Ligando para indicar o sentido do movimento do motor 1, a velocidade sera alterada conforme o adequado.
    in4.value(0)# Desligado pois indica o outro sentido (para trás).
    enb.duty_u16(velocidade)# O "u16" indica o máximo e mínimo de velocidade, nesse caso de 0 a 65535.
    
def tras_motor1(velocidade):
    in1.value(0)
    in2.value(1)
    ena.duty_u16(velocidade)
    
def tras_motor2(velocidade):
    in3.value(0)
    in4.value(1)
    enb.duty_u16(velocidade)
    
def parar_motor1():
    in1.value(0)
    in2.value(0)
    ena.duty_u16(0)
    
def parar_motor2():
    in3.value(0)
    in4.value(0)
    enb.duty_u16(0)
    
def virar_esquerda(velocidade):
    tras_motor2(20000)
    parar_motor1()
    ena.duty_u16(velocidade)
    enb.duty_u16(velocidade)
    
def virar_direita(velocidade):
    frente_motor1(20000)
    parar_motor2()
    ena.duty_u16(velocidade)
    enb.duty_u16(velocidade)

def freio_motor1():
    in1.value(1)
    in2.value(1)
    ena.duty_u16(1)
    
def freio_motor2():
    in3.value(1)
    in4.value(1)
    enb.duty_u16(1)
    
try:
    while True:
        frente_motor1(20000)
        tras_motor2(20000)
        freio_motor1()
        freio_motor2()
finally:
    parar_motor1()
    parar_motor2()


    