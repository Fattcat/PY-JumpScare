# Potrebne Moduly
###############
import ctypes #
import time   #
import os     #
import pygame #
###############ň

# definovanie kde sa nachadza subor (a aj vsetky ostatne) vlastne ako lokalizacia
script_directory = os.path.dirname(os.path.abspath(__file__))

# nazov premennej Song v ktorej je zvukovy subor
Song = "DevourJumpScareSound.mp3"

# initializovanie pygame a mixeru
pygame.init()
pygame.mixer.init()


# LIST Fotiek, kt. sa zobrazia na tapece
wallpapers = [
    os.path.join(script_directory, "001.jpg"),
    os.path.join(script_directory, "002.jpg"),
    os.path.join(script_directory, "003.jpg"),
    os.path.join(script_directory, "004.jpg"),
    os.path.join(script_directory, "005.jpg"),
    os.path.join(script_directory, "006.jpg"),
    os.path.join(script_directory, "007.jpg"),
    os.path.join(script_directory, "008.jpg"),
    os.path.join(script_directory, "009.jpg"),
    os.path.join(script_directory, "010.jpg"),
    os.path.join(script_directory, "011.jpg"),
    os.path.join(script_directory, "012.jpg"),
    os.path.join(script_directory, "013.jpg"),
    os.path.join(script_directory, "014.jpg"),
    os.path.join(script_directory, "015.jpg"),
    os.path.join(script_directory, "016.jpg"),
    os.path.join(script_directory, "017.jpg"),
    os.path.join(script_directory, "018.jpg"),
    os.path.join(script_directory, "019.jpg"),
    os.path.join(script_directory, "020.jpg"),
    os.path.join(script_directory, "021.jpg"),
    os.path.join(script_directory, "022.jpg")
]

# Premenna DefaultWallPap v kt. je definovane odkial sa ma zobraziť Astronaut.jpg po skonceni obrazok ako posledny WallPaper na nastavenie
DefaultWallPap = os.path.join(script_directory, "Astronaut.jpg")

# for loop pre spustenie songi
for WallPap in wallpapers:
    pygame.mixer.music.load(Song)
    pygame.mixer.music.play()
    
    # while loop pre : podmienku pokial sa prehráva song tak sa bude aj WallPaper
    while pygame.mixer.music.get_busy():
        for icko in wallpapers:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, icko, 0)
            time.sleep(0.099)
    else:
        time.sleep(1)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, DefaultWallPap ,0)
        time.sleep(1)
        break

#    ctypes.windll.user32.SystemParametersInfoW(20,0, icko, 0)
#    time.sleep(0.2)
