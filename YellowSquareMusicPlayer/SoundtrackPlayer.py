import os
import pygame
import keyboard
from colorama import Fore, Style

def PlaySoundtrack(folder, soundtrack_name):

    file_path = os.path.join(folder, soundtrack_name)
    paused = False
    loop_enabled = False

    if not os.path.exists(file_path):
        print(Fore.LIGHTRED_EX + "ERR0R! File not found" + Style.RESET_ALL)
        return "exit"
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=-1 if loop_enabled else 0)
    name, _ = os.path.splitext(soundtrack_name)
    sonido = pygame.mixer.Sound(file_path)
    duracion_total = sonido.get_length()
    segundos = duracion_total % 60
    minutos = duracion_total // 60
    #status = "looping" if loop_enabled else "not looping"
    #status = "🔂" if loop_enabled else "🔀"
    print(f"Now playing: {Fore.LIGHTYELLOW_EX}{name}{Style.RESET_ALL}")
    print("  <- key  | spacebar | ⬆ key | escape | -> key")
    print(" previous |  pause   | loop  |  exit  |  next ")
    print(f" Soundtrack duration: {minutos:2.0f}:{segundos:02.0f}") # :2.0f makes the code not showing the decimals

    while True:
        evento = keyboard.read_event() #IMPORTANT: This should be change in case the device lenguage is other
        if evento.event_type == keyboard.KEY_UP:
            if evento.name == "space":
                if paused == False:
                    pygame.mixer.music.pause()
                    paused = True
                elif paused == True:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    print(Fore.LIGHTRED_EX + "ERR0R! How the fuck did you reach this error?" + Style.RESET_ALL)
            if evento.name == "flecha arriba":
                loop_enabled = not loop_enabled
                pygame.mixer.music.play(loops=-1 if loop_enabled else 0)
                status = "enabled" if loop_enabled else "disabled"
                print(f"Loop {status}")
            if evento.name == "flecha izquierda":
                pygame.mixer.music.stop()
                return "previous"
            if evento.name == "flecha derecha":
                pygame.mixer.music.stop()
                return "next"
            if evento.name == "esc":
                pygame.mixer.music.stop()
                return "exit"