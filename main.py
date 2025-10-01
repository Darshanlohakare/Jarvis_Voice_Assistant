# import os
# import eel 

# from engine.features import playAssistantSound
# from engine.command import *  # Only keep thpython main.pyis if you're using functions from here

# # Initialize the eel app with the 'www' folder
# def start():
#     eel.init("www")

#     # Play a sound before launching
#     playAssistantSound()

#     # Launch Microsoft Edge in app mode manually (optional if eel.start can do it)
#     os.system('start msedge.exe --app="http://localhost:8000/index.html"')

#     # Start the eel web app
#     eel.start('index.html', mode=None, host='localhost', port=8000, block=True) 

import os
import eel
from engine.features import playAssistantSound
from engine.command import *

def start():
    eel.init("www")
    print("Eel initialized")

    playAssistantSound()
    print("Sound played")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    print("Browser opened")

    # os.system('start chrome.exe --app="http://localhost:8000/index.html"')
    # print("Browser opened")


    eel.start('index.html', mode=None, host='localhost', port=8000, block=True)

if __name__ == "__main__":
    start()

