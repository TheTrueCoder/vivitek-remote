import requests

# Constants
# API url base
control_url = "http://{}/tgi/console.tgi?{}"

# Function query strings
qstrs = {
    "power": {
        False: "powerOff",
        True: "powerOn"
    },
    "sources": {
        "pc1": "computer1",
        "pc2": "computer2",
        "pc3": "computer3",
        "comp": "component",
        "vid": "vedio",
        "svid": "sVedio"
    },
    "mute": {
        "prefix": "mute",
        "states": ["Off", "On"],
        "prop": {
            "video": "Pic",
            "sound": "Snd",
            "osd": "OSD"
        }
    }
}


class vivitek:
    def __init__(self, endpoint, debug=False):
        self.endpoint = endpoint
        self.debug = debug


    # Prints debug messages if the option is enabled.
    def dprint(self, message):
        if self.debug is True:
            print(message)


    # Send a request to the control api.
    def api_set(self, qstring):
        try:
            response = requests.get(control_url.format(self.endpoint, qstring))
            self.dprint(response)
            return True
        except:
            self.dprint("Something failed in api_set.")
            return False

    # Control projector power state
    def setpower(self, state):
        if state < 0 or state > 1:
            self.dprint("The state input should be a boolean")
            return False
        state = bool(state)

        qstr = qstrs["power"][state]
        self.dprint(qstr)
        return self.api_set(qstr)

    def setsource(self, source):
        if source not in qstrs["sources"].keys():
            self.dprint("Input one of the keys in the sources dictionary")
            return False

        qstr = qstrs["sources"][source]
        self.dprint(qstr)
        return self.api_set(qstr)

    def setmute(self, prop, state):
        mqstrs = qstrs["mute"]
        if prop not in mqstrs["prop"].keys():
            self.dprint("Input one of the keys in the mute dictionary")
            return False
        if state < 0 or state > 1:
            self.dprint("The state input should be a boolean")
            return False

        qstr = (mqstrs["prefix"] + mqstrs["prop"][prop] +
                mqstrs["states"][bool(state)])
        self.dprint("QStr: " + qstr)
        return self.api_set(qstr)

    def options(self, function):
        if function == "mute":
            return qstrs[function]["prop"].keys()
        elif function in qstrs.keys():
            return qstrs[function].keys()
        else:
            print(f"Please choose a function from {qstrs.keys()}.")
