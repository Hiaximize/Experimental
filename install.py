#!/usr/bin/env python3

import subprocess
import os
import tkinter
from tkinter import scrolledtext

print("This script will get your Kali linux installation up to speed")



###############################Experimental Code#######################################


firstWindow = tkinter.Tk()
firstWindow.title("Experimental Framework Installer")
ScrolledText = scrolledtext.ScrolledText(firstWindow, width=70, height=27)
ScrolledText.grid(column=5, row=4)
f = open("text.txt", "r")
fo = f.readlines()
ScrolledText.insert(tkinter.INSERT, fo)
firstLabel = tkinter.Label(firstWindow, text="Experimental GUI", font=("Calibri", 10))

firstWindow.geometry('1500x1000')
firstLabel.grid(column=0, row=0)


firstWindow.mainloop()

###################################################################################################

print("")
print("[+] Performing update, upgrade, full upgrade and distribution upgrade")
print("")

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newpath):
        self.newpath = os.path.expanduser(newpath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newpath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def install_beelogger():
    with cd("~/"):
        print("[-] Installing BeeLogger in your root directory")
        subprocess.call("git clone https://github.com/4w4k3/BeeLogger.git >> test.txt", shell=True)
        with cd("BeeLogger/"):
            subprocess.call("./install.sh >> test.txt", shell=True)
            print("[+] BeeLogger is now installed in root directory")


def install_thefatrat():
    with cd("~/"):
        print("")
        print("[-] Installing TheFatRat to root directory")
        print("")
        subprocess.call("git clone https://github.com/Screetsec/TheFatRat.git", shell=True)
        with cd("TheFatRat/"):
            subprocess.call("chmod +x setup.sh", shell=True)
            subprocess.call("./setup.sh", shell=True)
            print("")
            print("[+] TheFatRat is now installed in the root directory")

def install_empire():
    with cd("~/"):
        print("")
        print("[-] Installing Empire to root directory")
        print("")
        subprocess.call("git clone https://github.com/EmpireProject/Empire.git", shell=True)
        with cd("Empire/setup"):
            subprocess.call("chmod +x install.sh", shell=True)
            subprocess.call("./install.sh", shell=True)
            print("")
            print("[+] Empire is now installed in the root directory")


def install_lazagne():
    with cd("~/"):
        print("")
        print("[-] Installing LaZagne to root directory")
        print("")
        subprocess.call("git clone https://github.com/AlessandroZ/LaZagne.git", shell=True)
        with cd("LaZagne/setup"):
            print("")
            print("[+] LaZagne is now installed in the root directory")


def install_veil_framework():
    with cd("~/"):
        print("")
        print("[-] Installing Veil-Framework to root directory")
        print("")
        subprocess.call("git clone https://github.com/gold1029/Veil-Framework-Veil3.0-.git", shell=True)
        with cd("Veil-Framework-Veil3.0-/setup"):
            subprocess.call("chmod +x setup.sh", shell=True)
            subprocess.call("./setup.sh", shell=True)
            print("")
            print("[+] Veil-Framework is now installed in the root directory")


def install_zlogger():
    with cd("~/"):
        print("")
        print("[-] Installing Zlogger to root directory")
        print("")
        subprocess.call("git clone https://github.com/jlemon/zlogger.git", shell=True)
        with cd("ZLogger/"):
            subprocess.call("chmod +x install.sh", shell=True)
            subprocess.call("./install.sh", shell=True)
            print("")
            print("[+] ZLogger is now installed in the root directory")


def installing_and_setup_tor():
    f = open("/etc/proxychains.conf", "a")
    f.write("socks5  127.0.0.1 9050\n")
    f.write("socks5  127.0.0.1 9050")
    f.close()
    subprocess.call("leafpad /etc/proxychains.conf", shell=True)
    with cd("~/"):
        subprocess.call("clear")
        print('')
        print("[-] Installing tor...")
        subprocess.call("apt-get install tor -y", shell=True)
        subprocess.call("clear", shell=True)

def install_repository_tools():
    subprocess.call("apt-get install snort -y", shell=True)
    subprocess.call("apt-get install pdas -y", shell=True)
    subprocess.call("apt-get install mitmf -y", shell=True)


def setup_networkmanager():
    print("You will need to change the value from false to true, click the exit button when done")
    subprocess.call("leafpad /etc/NetworkManager/NetworkManager.conf", shell=True)
    subprocess.call("service network-manager restart", shell=True)
    subprocess.call("clear", shell=True)
    print("There is one more thing to do which is quite complicated but hopefully this gets everything up and running "
          "for your network")
    subprocess.call("clear", shell=True)

def testing_function():
    print("[+] Printing to the text output for the gui")
    subprocess.call("ping google.com >> text.txt", shell=True)
#

# def setup_NetworkManager():
#     with cd("~/"):
#         tempfile = open("/etc/NetworkManager/NetworkManager.conf", )
#     for line in .input("NetworkManager.conf"):
#         if "true" in line:
#             print("Current value set to true")
#             continue
#         else:
#             print("Changing value to true")
#             tempfile.write(line.replace("false", "true"))
#             tempfile.close()


def main_function():
#    setup_networkmanager()
#    setup_NetworkManager()
#    installing_and_setup_tor()
#    install_beelogger()
#    install_thefatrat()
#    install_empire()
#    install_lazagne()
#    install_veil_framework()
#    install_zlogger()
#    install_repository_tools()
#    subprocess.call("apt-get update && apt-get upgrade -y && apt-get full-upgrade -y && apt-get dist-upgrade -y", shell=True)
     testing_function()


main_function()