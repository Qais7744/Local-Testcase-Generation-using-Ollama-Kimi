' VBScript to start BLAST server in background (no command window)
Option Explicit

Dim WshShell, strCommand, strPath

' Get the directory where this script is located
strPath = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\") - 1)

' Change to that directory
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = strPath

' Build the command to run
strCommand = "python.exe deploy.py --host 0.0.0.0 --port 5000"

' Run the command hidden (0 = hidden window)
WshShell.Run strCommand, 0, False

' Show notification
MsgBox "BLAST Testcase Generator started!" & vbCrLf & vbCrLf & _
       "Access at: http://localhost:5000" & vbCrLf & vbCrLf & _
       "To stop: Open Task Manager and end 'python.exe' process", _
       vbInformation, "BLAST Server Started"

Set WshShell = Nothing
