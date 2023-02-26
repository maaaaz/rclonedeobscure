Rclone deobscure
================

Description
-----------
A simple script to decrypt [obscured/encrypted passwords](https://rclone.org/commands/rclone_obscure/) from Rclone

Features
--------
Can deobscure, and also obscure (equivalent of `rclone obscure`)


Options
-------
```
$ python rclonedeobscure.py -h
usage: rclonedeobscure.py [-h] [-d DEOBSCURE | -o OBSCURE]

version: 1.0

options:
  -h, --help            show this help message and exit
  -d DEOBSCURE, --deobscure DEOBSCURE
                        Obscured/encrypted password to deobscure/decrypt
  -o OBSCURE, --obscure OBSCURE
                        Plain-text password to obscure/encrypt
```

Examples
--------
#### deobscure
```
$ python rclonedeobscure.py -d "j_NGTXg4iQHiNwmNXTT6goDab0un-q6XvHXbSuhxzqprLGUZXSNCWwI_qAl1iLTIIRtNug"
[+] obscured password	: j_NGTXg4iQHiNwmNXTT6goDab0un-q6XvHXbSuhxzqprLGUZXSNCWwI_qAl1iLTIIRtNug
[+] deobscured password	: CorrectHorseBatteryStaple0123456789!
```

#### obscure
```
$ python rclonedeobscure.py -o "passw0rd"
[+] plaintext password	: passw0rd
[+] obscured password	: F7VL23kUgcFtx9AFXtflKP5PHLiUxzl9

$ python rclonedeobscure.py -d "F7VL23kUgcFtx9AFXtflKP5PHLiUxzl9"
[+] obscured password	: F7VL23kUgcFtx9AFXtflKP5PHLiUxzl9
[+] deobscured password	: passw0rd
```

Dependencies and installation
-----------------------------
* The **easiest way** to setup everything: `pip install rclonedeobscure` and then directly use `$ rclonedeobscure`
* Or manually install requirements: `pip install -r requirements.txt`

Changelog
---------

* version 1.0 - 2023-02-26: Initial commit

Copyright and license
---------------------
Licenced under the MIT Licence, as the Rclone project is.  
All trademarks, service marks, trade names and product names appearing on this repository are the property of their respective owners.  
I don't own anything on rclone, neither am I affiliated or working on the project.

Contact
-------
* Thomas Debize < tdebize at mail d0t com >