# brightness
Brightness control tool.

This simple Python script is designed to control brightness in GhostBSD. It can work with any window manager, including: KDE, Mate, i3, Xfce, OpenBox, etc... 

Requirements (List of packages required for this script to work):
1) Python (≥3)
2) PyGObject
3) GTK3
4) GhostBSD-utilities (contains cli tool "backlight", used in this python script). Any other cli brightness control tool can be used as well, but, in this case, the python script will have to be modified, replacing "backlight" with other command line tool
5) Optional: Create startup script ( sh script).

   For example:
   
   #!/bin/sh
   
   /usr/local/bin/python3 /path/to/directory/containing/file.py

If a startup script (simple sh script) has not been created, then running a specific Python script/file is simple: open a terminal in the directory of the downloaded Python script, then type "python3" followed by the name of the downloaded Python script/file. A small window will appear with a horizontal slider (the default brightness value is 43, you can change it in the script). Click on the slider and move it left or right to decrease or increase the brightness. The slider is set to decrease/increase the brightness by 5% (you can change it to any other desired %).

NOTE: The Ghost-BSD development team is free to add to or modify it to make it part of the MATE (desktop environment), as an applet or part of the power manager.
