num = input('presione 1 si quieres convertir a horas y minutos: Presione 2 si quieres convertir de hora a segundos:')

def convert_seconds(sec):
    
    hours = int(seconds) / 3600
    minutes = (int(seconds) % 3600)/60
    print('la cantidad de horas es: ',int(hours),':',int(minutes))

def convert_hour(hour):
    seconds = int(hour)*3600
    print('la cantidad de segundos es: ',int(seconds))

if num == '1':
    seconds = input('ingrese cantidad de numeros para convertir en horas: ')
    convert_seconds(int(seconds))
elif num == '2':
    hour = input('ingrese cantidad de horas para convertir en segundos: ')
    convert_hour(int(hour))
else:
    print('opcion no valida')