#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'

echo -e "${GREEN} "
echo ""
echo "  ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗██████╗ "
echo "  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝██╔══██╗"
echo "  ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗  ██████╔╝"
echo "  ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝  ██╔══██╗"
echo "  ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗██║  ██║"
echo "  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝"
echo ""
echo -e "${BLUE}                   https://github.com/stormexx ${NC}"
echo ""
echo -e ${CYAN}              "└──OPTIONS "
echo ""
echo -e "${WHITE}       [1] Install "
echo -e "${WHITE}       [0] Exit "
echo ""
echo -n -e "${RED}profiler@stormex ${GREEN}»${NC}"
read choice
if [ $choice == 1 ]; then
  echo ""
	if [[ $? -eq 0 ]]; then
      echo -e "${YELLOW}[~] Loading... "
      echo -e "${CYAN}[>] Installing Requirements..."
	pip3 install requests
	pip3 install termcolor
      echo -e "${GREEN}[✔] Successfully Installed "
	else
	  echo ""
		echo -e  "${RED}[✘] Installation Failed"
		echo "";
		exit
	fi
elif [ $choice -eq 0 ];
then
    exit
else
    echo -e $RED "[!] Invalid Option"
fi
