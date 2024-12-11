from machine import Pin, I2C, PWM
import utime
from ssd1306 import SSD1306_I2C

# Pinos para o sensor Hall e o buzzer
hall_pin = Pin(7, Pin.IN)  # GPIO 7 para o sensor Hall
buzzer_pin = Pin(8)  # GPIO 8 para o buzzer
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.freq(2000)  # Frequência do buzzer

# Display OLED
i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

def centralizar_texto(texto, linha, largura_fonte=8):
    largura_texto = len(texto) * largura_fonte
    x = max(0, (oled.width - largura_texto) // 2)
    oled.text(texto, x, linha)

def desenhar_ima():
    oled.rect(54, 30, 20, 10, 1)  # Corpo do ímã
    oled.line(54, 35, 49, 30, 1)  # Lado esquerdo do ímã
    oled.line(54, 35, 49, 40, 1)  # Lado esquerdo do ímã
    oled.line(74, 35, 79, 30, 1)  # Lado direito do ímã
    oled.line(74, 35, 79, 40, 1)  # Lado direito do ímã

def ler_sensor_hall():
    return hall_pin.value()

def exibir_mensagem(magnetico):
    oled.fill(0)  # Limpa o display
    if magnetico:
        centralizar_texto("Campo Magnetico!", 0)
        centralizar_texto("Detectado", 10)
        desenhar_ima()  # Desenha o ímã
        buzzer_pwm.duty_u16(32768)  # Ativa o buzzer com 50% de duty cycle
    else:
        centralizar_texto("Sem Campo", 0)
        centralizar_texto("Magnetico", 10)
        buzzer_pwm.duty_u16(0)  # Desativa o buzzer

    oled.show()

while True:
    magnetico = ler_sensor_hall() == 0
    exibir_mensagem(magnetico)
    utime.sleep(0.5)  # Intervalo para leitura do sensor
