#!/bin/bash
### BEGIN INIT INFO
# Provides:          ver
# Required-Start:
# Required-Stop:
# Should-Start:
# Default-Start:
# Default-Stop:
# Short-Description: Donne des infos sur le systeme
# Description:       Indique les infos reseau
#                    et pingue l exterieur
### END INIT INFO

#########################
##      à modifier     ##
#########################
install_date="nc"
ip_publique="1.1.1.1"
fqdn_public="www.bing.com"
check_ip="ifconfig.co"

clear

echo -e "Nom d'hôte :          \033[33m" `hostname` "\033[0m"
echo -e "Date d'installation : \033[33m" "$install_date" "\033[0m"
echo -e "Version Debian :      \033[33m" `cat /etc/debian_version` "\033[0m"
echo -e "Version noyau  :      \033[33m" `uname -rm`  "\033[0m"


echo -e "Adresse(s) IP : \033[33m"
# ifconfig eth0 | grep "inet"
ip -4 addr | grep "inet"
# ifconfig wlan | grep "inet"
echo -e -n "\033[0m"


echo -e "Route par défaut : \033[33m"
echo -n "          "
# route | grep "default"
ip route | grep "default"
echo -e -n "\033[0m"


echo -e "Résolveurs : \033[33m"
echo -n "    "
cat /etc/resolv.conf
echo -e -n "\033[0m"


ping -c 2 $ip_publique > /dev/null 2>&1
if [ $? -eq 0 ]; then
        echo -e "Ping vers une IP publique : \033[32mOK\033[0m"
else
        echo -e "Ping vers une IP publique : \033[31mKO\033[0m"
fi


ping -c 2 $fqdn_public > /dev/null 2>&1
if [ $? -eq 0 ]; then
        echo -e "Ping vers un FQDN public :  \033[32mOK\033[0m"
else
        echo -e "Ping vers un FQDN public :  \033[31mKO\033[0m"
fi


echo -e "Adresse IPv4 publique :      \033[33m" "`curl -4 --connect-timeout 5 $check_ip 2>/dev/null`" "\033[0m"
echo -e "Adresse IPv6 publique :      \033[33m" "`curl -6 --connect-timeout 5 $check_ip 2>/dev/null`" "\033[0m"


exit 0
