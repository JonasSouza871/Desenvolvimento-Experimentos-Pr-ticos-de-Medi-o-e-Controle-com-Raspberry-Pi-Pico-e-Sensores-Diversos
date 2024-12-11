import machine
import utime

# Configuração dos pinos
hall_pin = machine.Pin(7, machine.Pin.IN)  # Sensor Hall
buzzer_pin = machine.Pin(8)  # Buzzer

# Configuração do PWM para o buzzer
buzzer_pwm = machine.PWM(buzzer_pin)
buzzer_pwm.freq(2000)  # Define a frequência do buzzer

def read_hall_sensor(pin):
    """ Verifica o estado do sensor Hall e retorna seu valor. """
    return pin.value()

def main():
    start_time = utime.ticks_ms()
    
    while True:
        # Verifica o estado do sensor Hall
        magnetic = 1 if read_hall_sensor(hall_pin) == 0 else 0
        
        # Ativa ou desativa o buzzer com base na detecção
        if magnetic:
            buzzer_pwm.duty_u16(32768)  # Ativa o buzzer com 50% de duty cycle
            buzzer_state = 1
            print("Tempo: {:.1f}s - Campo Magnético Detectado!".format(utime.ticks_diff(utime.ticks_ms(), start_time) / 1000))
        else:
            buzzer_pwm.duty_u16(0)  # Desativa o buzzer
            buzzer_state = 0
            print("Tempo: {:.1f}s - Sem Campo Magnético".format(utime.ticks_diff(utime.ticks_ms(), start_time) / 1000))
        
        # Captura o tempo atual
        current_time = utime.ticks_diff(utime.ticks_ms(), start_time) / 1000
        
        # Salva os dados no arquivo
        with open("dados_sensor2.txt", "a") as file:
            file.write("{:.1f}\t{}\t{}\n".format(current_time, magnetic, buzzer_state))
        
        utime.sleep_ms(100)  # Pausa de 100 milissegundos entre leituras

if __name__ == "__main__":
    main()
