from sublime_plugin import WindowCommand
from sublime import packages_path, ENCODED_POSITION
from time import strftime
from os.path import isfile

headerText = """
--------------------------------------------------------------------------------------------

     ______   ______   ______   ______   ______  ______   __  __   ______  ______   _____
    /\  ___\ /\  ___\ /\  == \ /\  __ \ /\__  _\/\  ___\ /\ \_\ \ /\  == \/\  __ \ /\  __-.
    \ \___  \\ \ \____\ \  __< \ \  __ \\/_/\ \/\ \ \____\ \  __ \\ \  _-/\ \  __ \\ \ \/\ \
     \/\_____\\ \_____\\ \_\ \_\\ \_\ \_\  \ \_\ \ \_____\\ \_\ \_\\ \_\   \ \_\ \_\\ \____-
      \/_____/ \/_____/ \/_/ /_/ \/_/\/_/   \/_/  \/_____/ \/_/\/_/ \/_/    \/_/\/_/ \/____/


--------------------------------------------------------------------------------------------

"""


class OpenScratchpadCommand(WindowCommand):
    def run(self):
        scratchpadFile = packages_path()[:-8] + "scratchpad.md"
        checkAndFillEmpty(scratchpadFile)
        self.window.open_file(scratchpadFile)


class ScratchpadCommand(WindowCommand):
    def run(self):
        scratchpadFile = packages_path()[:-8] + "scratchpad.md"
        global headerText
        checkAndFillEmpty(scratchpadFile)
        count = putTimeStamp(scratchpadFile)
        self.window.open_file(scratchpadFile + ":" + str(count + 1), ENCODED_POSITION)


def checkAndFillEmpty(scratchpadFile):
    global headerText
    if not isfile(scratchpadFile):
        with open(scratchpadFile, "a") as scratchFile:
            scratchFile.write(headerText)


def putTimeStamp(scratchpadFile):
    timeStamp = "\n\n# " + strftime("%c") + "\n\n"

    with open(scratchpadFile, "a") as scratchFile:
        scratchFile.write(timeStamp)

    with open(scratchpadFile) as scratchFile:
        count = sum(1 for line in scratchFile)

    return count
