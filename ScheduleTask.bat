@ECHO OFF
SET var1="C:\Users\Hubert\Documents\Projekty Python\2020.04\1 - days to DEATH counter in a pseudo-widget format\python.exe"
SET var2="C:\Users\Hubert\Documents\Projekty Python\2020.04\1 - days to DEATH counter in a pseudo-widget format\main.pyw"
schtasks /Create /SC DAILY /TN DeathClock /TR %var1=%~1% %var2=%~1%
PAUSE
