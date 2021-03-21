The online multiplayer game involves a server and a client, however
while playing there is no actual difference between them.
There is some setup required to play the game between the
server and client.

In order to play within the same(wifi) network we need to send any one
file to the person we wish to play with and then modify the 
host variable in both the files to the local IP Address of the device 
running the 'server' file and then run the files in the respective
devices. In order to find the local IP Address of the device running
the 'server' file, open Command Prompt in windows and enter 'ipconfig'.
A line in the output will be similar to the line below:

IPv4 Address . . . . . . . . . . . : 192.168.x.x

Copy this number, modify the host variable and you are good to go!


In order to play from any part of the world, the process is quite 
complex, yet it is possible to play by port forwarding using ngrok or
by configuring your router.

Thank You!

Installation:
Python3.6 or newer
pip install pygame
pip install sockets
