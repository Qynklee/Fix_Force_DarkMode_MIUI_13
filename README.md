# Fix Force Dark Mode for app in MiUI 13

- This tools will be:
  - Run adb to get all user installed package name
  - Create a magisk module with all this package name, this module will be add all app to Dark mode options setting in Settings MIUI.

- How to use:
  - By source code:
    - Run code.py with python 3.7 or above in Windows host with your phone connected via adb.
    - Flash output file: CUSTOM..zip in Magisk
  - By exe file:
    - Download zip file tool in release.
    - Extract and run FixForceDarkMode.exe
    - Follow instruction
    - Copy output CUSTOM... .zip file to your phone and flash in Magisk