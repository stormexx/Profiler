#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from colors import *
from banner import banner
from net_check import is_connected
from get_info import profiler


def interactive_shell():
    try:
        while True:
            os.system("clear")
            banner()
            cmd = input(
                light_green("[*] ENTER USERNAME: ")
                + reset()
            )
            os.system("clear")
            banner()

            if is_connected():
                print(profiler(cmd))
            else:
                print(red("CHECK YOUR INTERNET CONNECTION !"))
            if cmd.split()[0] == "exit":
                os.system("clear")
                banner()
                exit()
            print("\n")
            res = input(red(">>> Do you want to continue (Y/n) ? ")
                        + reset())
            while not (res == "Y" or res == "n"):
                os.system("clear")
                banner()
                print("\n")
                res = input(red(">>> Do you want to continue (Y/n) ? ")
                            + reset())
            if res == "Y":
                os.system('clear')
                continue
            elif res == "n":
                os.system("clear")
                banner()
                break


    except KeyboardInterrupt:
        print(red(" Use exit !"))


interactive_shell()
