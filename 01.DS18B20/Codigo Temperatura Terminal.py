import machine
import onewire
import ds18x20
import utime

# Configuração do barramento 1-Wire
pin_ds18b20 = machine.Pin(7)
ds18b20_bus = onewire.OneWire(pin_ds18b20)
ds_sensor = ds18x20.DS18X20(ds18b20_bus)

# Descobre os sensores DS18B20 conectados
device_list = ds_sensor.scan()

if not device_list:
    print("Nenhum sensor DS18B20 encontrado!")
else:
    print("Sensores DS18B20 encontrados:", device_list)

try:
    while True:
        # Inicia a conversão de temperatura em todos os dispositivos
        ds_sensor.convert_temp()

        # Aguarda a conversão ser concluída
        utime.sleep_ms(750)

        # Lê a temperatura de todos os dispositivos
        for device in device_list:
            temperature = ds_sensor.read_temp(device)
            print("Temperatura: {:.2f}°C".format(temperature))

        # Aguarda 1 segundo entre as leituras
        utime.sleep(1)

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
