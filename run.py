# import multiprocessing
# import subprocess

# # To run Jarvis
# def startJarvis():
#         # Code for process 1
#         print("Process 1 is running.")
#         from main import start
#         start()

# # To run hotword
# def listenHotword():
#         # Code for process 2
#         print("Process 2 is running.")
#         from engine.features import hotword
#         hotword()
        
# import multiprocessing
# import subprocess

# # To run Jarvis
# def startJarvis():
#     print("Process 1 is running.")
#     from main import start
#     start()

# # To run hotword
# def listenHotword():
#     print("Process 2 is running.")
#     from engine.features import hotword
#     hotword()

# if __name__ == "__main__":
#     # Create two processes
#     p1 = multiprocessing.Process(target=startJarvis)
#     p2 = multiprocessing.Process(target=listenHotword)

#     # Start both processes
#     p1.start()
#     p2.start()

#     # Optional: Wait for both processes to finish
#     p1.join()
#     p2.join()

 

import multiprocessing
import subprocess

# To run Jarvis
def startJarvis():
        # Code for process 1
        print("Process 1 is running.")
        from main import start
        start()

# # To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from engine.features import hotword
        hotword()


    # Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")


