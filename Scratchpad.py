from os.path import expanduser, isfile
from time import strftime

from sublime import ENCODED_POSITION, load_settings, packages_path
from sublime_plugin import WindowCommand

SETTINGS_FILENAME = 'Scratchpad.sublime-settings'

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
        scratchpad_file = expandFilePath()
        if scratchpad_file:
            pass
        checkAndFillEmpty(scratchpad_file)
        self.window.open_file(scratchpad_file)


class ScratchpadCommand(WindowCommand):
    def run(self):
        scratchpad_file = expandFilePath()
        global headerText
        checkAndFillEmpty(scratchpad_file)
        count = putTimeStamp(scratchpad_file)
        self.window.open_file(scratchpad_file + ":" + str(count + 1), ENCODED_POSITION)


def expandFilePath():
    settings = load_settings(SETTINGS_FILENAME)
    scratchpad_file = settings.get('file_path')
    if not scratchpad_file:
        scratchpad_file = packages_path()[:-8] + "scratchpad.md"

    home_dir = expanduser("~") + "/"

    scratchpad_file = scratchpad_file.replace("~/", home_dir)
    scratchpad_file = scratchpad_file.replace("$HOME/", home_dir)

    return scratchpad_file


def checkAndFillEmpty(scratchpad_file):
    global headerText
    if not isfile(scratchpad_file):
        with open(scratchpad_file, "a") as scratch_file:
            scratch_file.write(headerText)


def putTimeStamp(scratchpad_file):
    timeStamp = "\n\n# " + strftime("%c") + "\n\n"

    with open(scratchpad_file, "a") as scratch_file:
        scratch_file.write(timeStamp)

    with open(scratchpad_file) as scratch_file:
        count = sum(1 for line in scratch_file)

    return count
