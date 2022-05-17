####Dependensy import####
import os
import sys
import urllib.request
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import tkinter as tk
from tkinter import messagebox
import atexit


####Open Server URL####
file_server_url = open("server.txt")
server_url=(file_server_url.read())
server_url=str(server_url)
####Open Version on File####
file_version = open("version.txt")
data_file=(file_version.read())
####Get Version on Server####
webUrl  = urllib.request.urlopen("http://"+(server_url)+"/version.html")
data = webUrl.read()
version_control = data
version_control = version_control.decode()


##############Funtions############
####funtion Download Update And Extract ZIP####
def yesupdate():
     result = messagebox.askquestion("", "افزار کنسول نیاز به بروز رسانی دارد . به روز رسانی میکنید؟")
     if result == "yes":
        zipurl = ("http://"+(server_url)+"/update.zip")
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall('.')
     else :
        hooks = ExitHooks()
        hooks.hook()

####funtion EXIT####
class ExitHooks(object):
    def __init__(self):
        self.exit_code = None
        self.exception = None

    def hook(self):
        self._orig_exit = sys.exit
        sys.exit = self.exit
        sys.excepthook = self.exc_handler

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def exc_handler(self, exc_type, exc, *args):
        self.exception = exc


####Call Funtions####
if version_control == data_file:
    messagebox.showwarning("", "!نرم افزار کنسول شما بروز میباشد")
    hooks = ExitHooks()
    hooks.hook()
elif version_control != data_file:
    atexit.register(yesupdate)
    hooks = ExitHooks()
    hooks.hook()
else:
    hooks = ExitHooks()
    hooks.hook()