@ECHO OFF
SET var1="FULL_PATH_TO_PYTHONW_EXE_HERE"
SET var2="FULL_PATH_TO_DEATH_CLOCK.PYW_HERE"
schtasks /Create /SC DAILY /TN DeathClock /TR "%var1% '%var2%'"
PAUSE