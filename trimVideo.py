import subprocess

def cortar_video_ffmpeg(input_path, output_path, inicio, fin):
    # Construye el comando ffmpeg
    comando = [
        'ffmpeg',
        '-ss', inicio,
        '-to', fin,
        '-i', input_path,
        '-c', 'copy',
        output_path
    ]

    # Ejecuta el comando
    try:
        subprocess.run(comando)
    except Exception as e:
        print("Error:", e)
        input()

def logConSeparador(log):
    print("")
    print(log)
    print("")

def getInputAndTrimVideo():
    # Input file
    inputPath = input("Nombre del archivo a cortar (si no se indica extensión, pasa a ser .mp4):")
    posDotInputPath = len(inputPath) - 4
    if inputPath[posDotInputPath] != ".":
        inputPath = f'{inputPath}.mp4'

    logConSeparador(f'Archivo a cortar: {inputPath}')

    # Output file
    outputPath = input("Nombre del archivo de salida (si no se indica extensión, pasa a ser .mp4):")
    posDotOutputPath = len(outputPath) - 4
    if outputPath[posDotOutputPath] != ".":
        outputPath = f'{outputPath}.mp4'
    
    logConSeparador(f'Archivo de salida: {outputPath}')
        
    # Hora inicio
    horaDeInicio = input("Hora en la que inicia el corte (formato X ó XX):")
    if horaDeInicio == "":
        horaDeInicio = "00"
    elif len(horaDeInicio) == 1:
        horaDeInicio = f'0{horaDeInicio}'

    # Minuto inicio
    minutoDeInicio = input("Minuto en el que inicia el corte:")
    if minutoDeInicio == "":
        minutoDeInicio = "00"
    elif len(minutoDeInicio) == 1:
        minutoDeInicio = f'0{minutoDeInicio}'

    inicio_tiempo = f'{horaDeInicio}:{minutoDeInicio}:00'
    logConSeparador(f'Tiempo inicio: {inicio_tiempo}')

    input("¿OK?")

    # Hora fin
    horaDeFin = input("Hora en la que termina el corte (formato X ó XX):")
    if horaDeFin == "":
        horaDeFin = "00"
    elif len(horaDeFin) == 1:
        horaDeFin = f'0{horaDeFin}'

    # Minuto fin
    minutoDeFin = input("Minuto en el que termina el corte:")
    if minutoDeFin == "":
        minutoDeFin = "00"
    elif len(minutoDeFin) == 1:
        minutoDeFin = f'0{minutoDeFin}'

    fin_tiempo = f'{horaDeFin}:{minutoDeFin}:00'
    logConSeparador(f'Segmento a cortar: {inicio_tiempo} - {fin_tiempo}')

    input("¿OK?")

    # Llama a la función para cortar el video
    try:
        cortar_video_ffmpeg(inputPath, outputPath, inicio_tiempo, fin_tiempo)
    except Exception as e:
        print("Error:", e)
        input()
    
    finally:
        print("Terminó la ejecución del script")
        input()

print("Se requiere tener instalada la librería ffmpeg (https://ffmpeg.org/)")
print("--------------------------------------------------------------------")
input("Press enter")
getInputAndTrimVideo()