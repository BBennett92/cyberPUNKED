# cyberPUNKED
Python 'ping' script.
[readme.txt](https://github.com/BBennett92/cyberPUNKED/files/10778157/readme.txt)
*WORK IN PROGRESS*


"cyberPUNKED" is a python script that pings all possible IP addresses on a network and reports back both

inside the terminal as well as outputting a text file in the directory it is ran in detailing all of the

devices online it has found on the it is ran on network. Based off of the "Ping" hack found in the

game "Cyberpunk 2077". *DISCLAIMER* Something something ethics something something don't break the law

something something no alphabet bois something something you will be resposnsible for your own actions

something something."


ENJOY!

-mh

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣠⠤⡶⠚⠉⢹⣿⣿⠀⣄⠙⣿⠁⠀⠈⠉⣿⣿⣷⠒⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡖⠻⣿⣿⠀⣷⠀⠸⠻⣿⣿⠀⠟⢠⣿⡄⢸⣿⣷⣿⣿⡏⢠⠀⣾⡿⠛⢳⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⡄⠉⠙⠀⣿⡀⠰⡶⢿⣿⠇⠀⠘⣿⡇⢀⣀⣿⣿⡿⠀⢿⢠⣿⠁⠀⣼⣿⣿⠛⠷⣦⡀⠀
⠀⠀⠀⠀⠸⣿⡄⣴⣄⣿⣇⣀⣀⣤⣿⣤⣼⣄⣸⡇⠘⠉⣽⡿⠁⢠⡄⢸⡏⠀⣼⣿⣿⠇⠀⣴⣿⣿⠂
⠀⠀⠀⠀⠀⠛⢛⣛⣫⣭⣭⣤⡄⢹⣿⣿⠉⠉⢻⣿⣿⠟⠻⢷⣦⣿⣇⣸⡇⠀⠛⣻⡏⢀⣾⣿⣿⠇⠀
⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⠀⠀⠈⣿⡏⠀⠀⣾⠇⠀⠀⢹⡿⠲⢶⣯⡀⠉⢩⣿⠏⠀⠀
⠠⣾⣿⣿⣿⡿⣿⣿⣿⡏⣿⣿⣿⡀⣿⣿⠀⠀⠀⠹⠀⠀⢠⡿⠀⣼⠀⢸⡇⢀⠀⠹⣿⣿⣿⠏⠀⠀⠀
⠀⢻⣿⠈⣿⢰⣎⢿⣿⡇⣿⣿⣿⡇⢸⣿⠀⢀⣆⠀⡀⠀⢸⠇⠀⠛⠀⣿⠁⣸⡇⠀⣿⣿⠏⠀⠀⠀⠀
⠀⠈⢿⣷⠸⡎⣿⣆⢿⡇⣿⡿⣻⣿⠈⣟⡀⢸⣿⣾⠁⠀⣾⠀⣸⠇⢀⡟⠀⣿⠃⠀⣿⡟⠀⠀⠀⠀⠀
⠀⠀⠘⣿⣧⢳⡹⣿⢸⡇⣿⠃⣿⣿⡄⣉⢉⣉⣉⣉⡉⠐⠛⠢⠿⣀⣸⠇⠈⠁⣀⣾⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣿⡈⣱⣬⣼⡇⣿⡆⣩⡙⣇⢸⡀⢻⠀⣿⠁⣉⢱⠒⠢⣄⡈⠑⠲⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣧⣿⣿⣮⣴⣿⠘⡇⢠⡀⣿⠀⠛⣿⢀⡆⢸⠈⠑⢤⡀⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⡿⠿⢛⣛⣋⣉⣉⣉⠀⠷⣼⣇⣿⠀⢿⡿⠈⢁⡿⠀⣸⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣬⡛⢦⡀⡇⣴⢸⡇⠀⢹⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠣⣿⢸⠃⣸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡏⠉⠉⠉⠉⠙⠛⠿⣿⣿⣿⣷⣝⢾⠀⠈⣿⡇⣴⣶⣶⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠲⠒⠒⠂⠉⠀⠀⠀⠉⠻⢿⣿⣷⣕⢼⣿⢠⣶⣾⣷⣮⣻⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⡸⠿⠿⢟⣵⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀
*FUTURE FEATURES TO INCLUDE:

-Port scans on online IPs found, print what ports are open and what services run on said ports, if any-
-List MAC address of online IP-
-Geolocation of online IP-
-WHOIS lookup of IP to obtain info on IP owner-
-Trace route, trace the packet sent from source to destination-
-Reverse DNS lookup, obtain hostname associated with IP-
-Vulnerability scanner-
-OS detection, print operating system used by the device linked to IP-
-E-mail tracing-
-Botnet detection-
-IP fingerprinting, print device version/type/config/installed software-
-VPN detection-
-Output all known data found online during recon for each IP to a text file-
-Add ability to scan a range of IPs if desired-
-DoS, packet flood ability to kick a rouge device off network-
-GUI?-
-8-bit tunes-
-Real-time updates via E-mail, text message-
-Error reporting-
-Multi-threading-
-Integration with third-party APIs-
-????
-PROFIT!-
*
