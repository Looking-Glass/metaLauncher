import os
import subprocess

while os.path.exists("unityLauncherPath.txt"):
	if os.path.exists("targetApp.txt"):
		targetAppPath = open("targetApp.txt", "r").readlines();
		
		os.remove("targetApp.txt");  #delete the text file
				
		subprocess.call([targetAppPath])
	else :
		launcherPath = open("unityLauncherPath.txt", "r").readlines();
		subprocess.call([launcherPath])