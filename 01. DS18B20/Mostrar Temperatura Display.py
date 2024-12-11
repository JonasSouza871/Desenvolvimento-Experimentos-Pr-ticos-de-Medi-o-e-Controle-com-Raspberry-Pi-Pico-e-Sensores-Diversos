import machine
import onewire
import ds18x20
import utime
from ssd1306 import SSD1306_I2C

# Configuração do barramento 1-Wire
pin_ds18b20 = machine.Pin(7)
ds18b20_bus = onewire.OneWire(pin_ds18b20)
ds_sensor = ds18x20.DS18X20(ds18b20_bus)

# Configuração do display OLED
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

# Função para desenhar a borda da tela
def draw_border():
    oled.rect(0, 0, oled.width, oled.height, 1)

# Função para exibir o título no topo da tela
def draw_title():
    oled.text("Monitor de", 8, 2)
    oled.text("Temperatura", 8, 12)

# Função para exibir o ícone do termômetro
def draw_thermometer_icon():
    oled.fill_rect(105, 2, 20, 20, 1)
    oled.fill_rect(115, 5, 4, 10, 0)
    oled.fill_rect(110, 22, 14, 4, 1)

try:
    while True:
        # Descobre os sensores DS18B20 conectados
        device_list = ds_sensor.scan()

        if not device_list:
            print("Nenhum sensor DS18B20 encontrado!")
        else:
            print("Sensores DS18B20 encontrados:", device_list)

        # Inicia a conversão de temperatura em todos os dispositivos
        ds_sensor.convert_temp()

        # Aguarda a conversão ser concluída
        utime.sleep_ms(750)

        # Limpa o display OLED
        oled.fill(0)

        # Desenha a borda da tela
        draw_border()

        # Exibe o título
        draw_title()

        # Exibe o ícone do termômetro
        draw_thermometer_icon()

        # Centraliza a leitura da temperatura no centro da tela
        temperature = ds_sensor.read_temp(device_list[0])
        text = "{:.2f}C".format(temperature)
        text_width = len(text) * 6  # Reduzindo o tamanho da fonte
        x = (oled.width - text_width) // 2
        y = (oled.height - 8) // 2
        oled.text(text, x, y)

        # Atualiza o display OLED
        oled.show()

        # Aguarda 1 segundo entre as leituras
        utime.sleep(1)

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
