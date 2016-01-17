WifiPineapple Mark 5 Infusion downloader
=======================================

    Why this?
    I found the resources of [WifiPineapple](https://www.wifipineapple.com) were not so *OPEN*. So I did a bit hack into it.
    And everyone can build his or her own WifiPineapple System.
    I bought a cheap portable router which is only $20, **Lenovo PWR G-60**, which has Atheros 9331 with 64MB RAM, 16MB ROM, SD socket, USB 2.0 socket,  6000 MHA Lipo bettery built inside. Battery life can be upto 14 hours.
    And I hacked it a bit with a better antenna.
    All your need is a compatible router which can run OpenWRT.

    --Alexander Liu


Requiresments
-------------
* A Linux/Unix system that has installed *python, curl, wget*
* Good internet connection -- In some region, internet was almost down. So you would need proxies, such as *shadowsocks* or *proxychains* and etc..


Download all infusions
----------------------
* Usage as followings:

    ![demo](http://i.imgur.com/S8hrByh.png)

    ```bash
    python download_infusions.py
    # Or use a proxy
    proxychains4 python download_infusions.py
    ```

#### Happy hacking!
