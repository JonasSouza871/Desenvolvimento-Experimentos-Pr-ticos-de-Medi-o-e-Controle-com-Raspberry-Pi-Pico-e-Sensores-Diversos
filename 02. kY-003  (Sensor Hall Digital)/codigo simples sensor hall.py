import machine
import utime

# Configuração dos pinos
pino_hall = machine.Pin(7, machine.Pin.IN)  # Sensor Hall
pino_buzzer = machine.Pin(8)  # Buzzer

# Configuração do PWM para o buzzer
pwm_buzzer = machine.PWM(pino_buzzer)
pwm_buzzer.freq(2000)  # Define a frequência do buzzer

def ler_sensor_hall(pino):
    """ Verifica o estado do sensor Hall e retorna seu valor. """
    return pino.value()

def principal():
    while True:
        # Verifica o estado do sensor Hall
        magnetico = ler_sensor_hall(pino_hall) == 0
        
        # Ativa ou desativa o buzzer com base na detecção
        if magnetico:
            pwm_buzzer.duty_u16(32768)  # Ativa o buzzer com 50% de duty cycle
            print("Campo Magnético Detectado!")
        else:
            pwm_buzzer.duty_u16(0)  # Desativa o buzzer
            print("Sem Campo Magnético")
        
        utime.sleep(1)  # Pausa entre leituras

if __name__ == "__main__":
    principal()
