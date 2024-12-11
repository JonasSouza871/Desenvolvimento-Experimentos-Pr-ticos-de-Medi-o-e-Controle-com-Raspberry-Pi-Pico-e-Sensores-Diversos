import machine
import onewire
import ds18x20
import utime
from ssd1306 import SSD1306_I2C

# Configure o pino GPIO ao qual o DS18B20 está conectado
pin_ds18b20 = machine.Pin(7)  # Use o pino GPIO 7

# Crie uma interface OneWire
ow = onewire.OneWire(pin_ds18b20)

# Crie um objeto DS18X20
ds_sensor = ds18x20.DS18X20(ow)

# Encontre todos os dispositivos DS18B20 na interface OneWire
roms = ds_sensor.scan()

# Configuração do display OLED
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

def read_temperature():
    # Inicie a conversão de temperatura em todos os dispositivos DS18B20
    ds_sensor.convert_temp()

    # Espere um tempo suficiente para a conversão terminar

    # Leia a temperatura do primeiro dispositivo DS18B20 encontrado
    temp = ds_sensor.read_temp(roms[0])
    return temp

def main():
    count = 1
    while True:
        # Leia a temperatura do DS18B20
        temperature = read_temperature()
        # Exiba a temperatura lida e o número de leituras
        print("Leitura", count, "- Temperatura: {:.4f} °C".format(temperature))
        
        # Limpe o display OLED
        oled.fill(0)
        oled.text("Leitura {}".format(count), 0, 0)
        oled.text("Temp: {:.4f} C".format(temperature), 0, 20)
        oled.show()
        
        # Armazene a temperatura em um arquivo de texto
        with open("dados_temperatura.txt", "a") as file:
            file.write("{}  {:.4f}\n".format(count, temperature))
        
        count +=1
        
        # Espere um pouco antes de ler novamente
        utime.sleep(1)

if __name__ == "__main__":
    main()
