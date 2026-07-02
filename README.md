# E7-Auto-Shop-Refresh

Basically what the name implies...<br>

It looks for covenant and mystic summons and then buy them<br>

I made and tested it for google play pc launcher at full screen with a monitor set on 1980x1080 so i won't guarantee it will work anywhere else.<br>

Use this as your own risk as this is bannable and i don't know how much SG protects it's game, just don't go crying on anywhere. Be responsible for your actions.<br>

I can't asure you this program will pick up 100% of the summons shown on screen but I'm fairly certain it'll either pick most of them or crash.<br>

If you want 100% you should probably do it manualy. <br>



## Download



[Download e7shopreroller.exe](https://github.com/LucaLabio/e7shopreroller/raw/main/downloads/e7shopreroller.exe)



The exe still requires [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) installed on your PC.<br>

If the app stops due to an error, check the `log/` folder next to the exe for a file named like `2-July-17-55.log` with suggestions on which screenshot may need updating.<br>



## Run from source



Requires Python (python 3.14+ recommended) 

https://www.python.org/downloads/ - MUST be installed with path

https://github.com/UB-Mannheim/tesseract/wiki - no special config needed, just spam "next" and make sure that it is installed on PATH, otherwise the code won't work



After installing both, run the following command on CMD/Terminal, if it fails you probably installed something wrong

pip install -r requirements.txt<br>



If it isn't working very well try to make small adjustments on "confidence" values or take your own screenshots instead of my default ones use them only as examples and if you overwrite them, make sure to keep the same file name