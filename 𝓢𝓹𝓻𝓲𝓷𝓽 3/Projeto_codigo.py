from machine import Pin, PWM, ADC
import time
from hcsr04 import HCSR04
from time import sleep

in1 = Pin(18, Pin.OUT)
in2 = Pin(33, Pin.OUT)
in3 = Pin(4, Pin.OUT)
in4 = Pin(21, Pin.OUT)
ena = PWM(Pin(22), 800)
enb = PWM(Pin(15), 800)
TRIG = Pin(13)
ECHO = Pin(12)
ultrasonico = HCSR04(trigger_pin=TRIG, echo_pin=ECHO)
# Informações dos sensores do TCRT5000
sensor1 = ADC(Pin(25)) # Sensor do lado direito
sensor1.atten(ADC.ATTN_11DB)
sensor1.width(ADC.WIDTH_12BIT)
sensor2 = ADC(Pin(26)) # Sensor do lado esquerdo
sensor2.atten(ADC.ATTN_11DB)
sensor2.width(ADC.WIDTH_12BIT)

def frente_motor1(velocidade):
    in1.value(1)# Ligando para indicar o sentido do movimento do motor 1, a velocidade sera alterada conforme o adequado.
    in2.value(0)# Desligado, pois indica o outro sentido (para trás).
    ena.duty(velocidade)# O "u16" indica o máximo e mínimo de velocidade, nesse caso de 0 a 65535.
   
def frente_motor2(velocidade):
    in3.value(1)# Ligando para indicar o sentido do movimento do motor 1, a velocidade sera alterada conforme o adequado.
    in4.value(0)# Desligado pois indica o outro sentido (para trás).
    enb.duty(velocidade)# O "u16" indica o máximo e mínimo de velocidade, nesse caso de 0 a 65535.
   
def tras_motor1(velocidade):
    in1.value(0)
    in2.value(1)
    ena.duty(velocidade)
   
def tras_motor2(velocidade):
    in3.value(0)
    in4.value(1)
    enb.duty(velocidade)
   
def parar_motor1():
    in1.value(0)
    in2.value(0)
    ena.duty(0)
   
def parar_motor2():
    in3.value(0)
    in4.value(0)
    enb.duty(0)
   
def virar_esquerda(velocidade):
    tras_motor2(400)
    parar_motor1()
    ena.duty(velocidade)
    enb.duty(velocidade)
   
def virar_direita(velocidade):
    frente_motor1(400)
    parar_motor2()
    ena.duty(velocidade)
    enb.duty(velocidade)
   
def girar_no_eixo_para_direita():
    frente_motor1(300)
    tras_motor2(300)
    sleep(0.04)
    frente_motor1(300)
    tras_motor2(300)
    sleep(0.04)
    parar_motor1()
    parar_motor2()
    sleep(0.04)
    frente_motor1(400)
    frente_motor2(400)
    sleep(0.04)
    frente_motor1(200)
    frente_motor2(200)
    sleep(0.04)
   
   
def girar_no_eixo_para_esquerda():
    frente_motor1(300)
    tras_motor2(300)
    sleep(0.04)
    parar_motor1()
    parar_motor2()
    sleep(0.04)
    tras_motor1(400)
    tras_motor2(400)
    sleep(0.04)
    tras_motor1(200)
    tras_motor2(200)
    sleep(0.04)
   

primeiro = 0

try:
    while True:
        ler1 = sensor1.read()
        ler2 = sensor2.read()
        print(f"1 = {ler1}")
        print(f"2 = {ler2}")
        sleep(0.1)
        if ler1 < 2000 and ler2 < 2000:
            frente_motor1(400)
            tras_motor2(400)
            sleep(0.03)
            frente_motor1(10)
            tras_motor2(10)
        elif ler2 >= 2100:
            tras_motor1(200)
            frente_motor2(200)
            sleep(0.01)
            tras_motor1(50)
            frente_motor2(50)
            sleep(0.05)
            girar_no_eixo_para_esquerda()
        elif ler1 >= 2100:
            tras_motor1(200)
            frente_motor2(200)
            sleep(0.01)
            tras_motor1(50)
            frente_motor2(50)
            sleep(0.03)
            girar_no_eixo_para_direita()
           
       
       
    while 0 :
        var_cm = ultrasonico.distance_cm()
        print(var_cm)
        sleep(0.1)
        if var_cm <= 20:
            parar_motor1()
            parar_motor2()
        else:
            frente_motor1(25000)
            tras_motor2(25000)
            sleep(0.2)
            frente_motor1(10000)
            tras_motor2(10000)
    while 0:
        var_cm = ultrasonico.distance_cm()
        print(var_cm)
        sleep(0.1)
        if var_cm <= 23:
            frente_motor1(25000)
            tras_motor2(25000)
            sleep(0.15)
            parar_motor1()
            parar_motor2()
            sleep(0.5)
            virar_direita(10000)
            virar_esquerda(5000)
            sleep(0.5)
            frente_motor1(10000)
            tras_motor2(10000)
        else:
            frente_motor1(25000)
            tras_motor2(25000)
            sleep(0.2)
            frente_motor1(10000)
            tras_motor2(10000)

finally:
    parar_motor1()
    parar_motor2()