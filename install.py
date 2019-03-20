#!/usr/bin/env python3


# import statements used to write the program
import subprocess
import os

# The below code was a class discovered through research to easily traverse local directories
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newpath):
        self.newpath = os.path.expanduser(newpath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newpath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


# Below function will install a tool for generating key loggers with emailing capabilities
def install_beelogger():
    with cd("~/"):
        print("[-] Installing BeeLogger in your root directory")
        subprocess.call("git clone https://github.com/4w4k3/BeeLogger.git >> test.txt", shell=True)
        with cd("BeeLogger/"):
            subprocess.call("./install.sh", shell=True)
            print("[+] BeeLogger is now installed in root directory")


# Below function will install a tool for creating malicious payloads, most notably android apks
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


# Below function will install a tool for creating malicious payloads for various platforms evading common AV's
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


# Below function will install a tool for creating trojans to have a windows machine send you all the saved passwords for websites
def install_lazagne():
    with cd("~/"):
        print("")
        print("[-] Installing LaZagne to root directory")
        print("")
        subprocess.call("git clone https://github.com/AlessandroZ/LaZagne.git", shell=True)
        print("")
        print("[+] LaZagne is now installed in the root directory")


# Below function will install a tool for creating customizable malicious payloads that evade AV's.
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
            


# Below function will install a tool for downloading and setting up tor to tunnel your connection through the tor network for anonymization
def installing_and_setup_tor():
    f = open("/etc/proxychains.conf", "a")
    f.write("\nsocks5  127.0.0.1 9050\n")
    f.write("socks5  127.0.0.1 9050")
    f.close()
    subprocess.call("leafpad /etc/proxychains.conf", shell=True)
    with cd("~/"):
        subprocess.call("clear", shell=True)
        print('')
        print("[-] Installing tor...")
        subprocess.call("apt-get install tor -y", shell=True)
        subprocess.call("clear", shell=True)


# Below function will install tools that are available through the linux repository
def install_repository_tools():
    subprocess.call("apt-get install snort -y", shell=True)
    subprocess.call("apt-get install pdas -y", shell=True)
    subprocess.call("apt-get install mitmf -y", shell=True)
    subprocess.call("apt-get install virtualbox -y", shell=True)


# Below function is for program testing
def testing_function():
    print("[+] Printing to the text output for the gui")
    subprocess.call("ping -c 1 google.com", shell=True)


# Below function is the main function for the program
def main_function():
#    testing_function()
    installing_and_setup_tor()
    install_beelogger
    install_thefatrat()
    install_empire()
    install_lazagne()
    install_veil_framework()
    install_repository_tools()
    subprocess.call("apt-get update && apt-get upgrade -y && apt-get full-upgrade -y && apt-get dist-upgrade -y", shell=True)


main_function()
  
