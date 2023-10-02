Set objShell = CreateObject("WScript.Shell")

' Specify the path to your executable here
exePath = "client.exe"

' Build the command to run the executable silently
command = "cmd /c start /min """" """ & "client.exe" & """"

' Run the command silently
objShell.Run command, 0, True
