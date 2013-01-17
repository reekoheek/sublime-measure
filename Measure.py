import sublime, sublime_plugin
from datetime import datetime
from os.path import expanduser
import os

#
class MeasureListener(sublime_plugin.EventListener):
    """ This is event to log every activity while you are coding """
    # home = ""
    log_dir = ""

    def __init__(self):
        setting = sublime.load_settings("Measure.sublime-settings")
        # self.home = expanduser("~")
        self.log_dir = expanduser(setting.get("log_dir", "~/logs"))
        try:
            os.makedirs(self.log_dir)
        except:
            pass

    def log(self, view, activity):
        now = datetime.now();

        file_name = self.log_dir + "/measure-" + now.strftime("%Y-%m-%d") + ".log"

        file_accessed = view.file_name()
        if not file_accessed:
            file_accessed = ""

        with open(file_name, "a") as myfile:
            myfile.write(str(now) + " " + activity + " " + file_accessed + "\n")


    def on_new(self, view):
        self.log(view, "n")

    def on_clone(self, view):
        self.log(view, "c")

    def on_load(self, view):
        self.log(view, "l")

    def on_post_save(self, view):
        self.log(view, "v")

    def on_selection_modified(self, view):
        self.log(view, "s")

    def on_activated(self, view):
        self.log(view, "a")

    def on_deactivated(self, view):
        self.log(view, "d")

    def on_modified(self, view):
        self.log(view, "m")

