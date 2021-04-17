from vivitek import vivitek
import os

#endpoint = "192.168.1.36"
endpoint = os.environ["PROJ_ENDPOINT"]
projector = vivitek(endpoint)

while True:
    usrtxt = input("Enter: On, Off, Source, Mute, Unmute, Exit: ")
    
    if usrtxt == "On":
        projector.setpower(True)
    elif usrtxt == "Off":
        projector.setpower(False)
    elif usrtxt == "Source":
        for item in projector.options("sources"):
            print(item)
        src = input("Choose source: ")
        projector.setsource(src)
    elif usrtxt == "Mute":
        for item in projector.options("mute"):
            print(item)
        prop = input("Choose property to mute: ")
        projector.setmute(prop, True)
    elif usrtxt == "Unmute":
        for item in projector.options("mute"):
            print(item)
        prop = input("Choose property to mute: ")
        projector.setmute(prop, False)
    elif usrtxt == "Exit":
        break
    else:
        print("Invalid option.")
