import argparse
from moviepy.editor import VideoFileClip

def convertir_a_mp4(archivo_entrada, archivo_salida):
    try:
        video_clip = VideoFileClip(archivo_entrada)
        video_clip.write_videofile(archivo_salida, codec='libx264', preset='ultrafast', bitrate='10000k')
        print("Conversión completada con éxito.")
    except Exception as e:
        print(f"Error al convertir el video: {e}")


parser = argparse.ArgumentParser(description="Convierte un video a formato MP4 de manera rápida.")
parser.add_argument("input", help="Nombre del archivo de entrada")
parser.add_argument("output", help="Nombre del archivo de salida")

args = parser.parse_args()
    
archivo_entrada = args.input
archivo_salida = args.output

convertir_a_mp4(archivo_entrada, archivo_salida)
