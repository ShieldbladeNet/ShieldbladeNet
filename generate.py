import requests, json, random, time
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
nameid = "ShieldbladeNet"
f = open("./README.md", "w")

f.write(f'''

<h3 align="center"><b>{timestr}</b></h3>
<h3 align="center">Have a nice day!</h3>
<p align="center">
  <a href="https://github.com/{nameid}">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username={nameid}&hide=issues&hide_title=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff" />
    </a>     
    
<p align="center">

[![build_firmware](https://github.com/{nameid}/Nano-Openwrt/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/{nameid}/Nano-Openwrt/actions/workflows/build-firmware.yml)

</p> 

# Nano R1S R2S R4S x86 Openwrt 
 
### Download Link：

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{nameid}/Nano-Openwrt?style=for-the-badge&label=Download)](https://github.com/{nameid}/Nano-Openwrt/releases) 

(Files do not need to be decompressed, you can directly use the flashing tool to flash in img.gz)

### Use suggestions:
The default user name is root, the password is password, and the LAN IP is 192.168.2.1
After burning the firmware, insert the tf card and start it up. After the computer displays "Network (Connected)", enter http://immortalwrt/ in the browser to directly open the router background without modifying the local connection settings or checking the IP address.
If the network status has been unrecognized (more than 5 minutes after power-on), please plug in and unplug the power directly and restart it.

### Online upgrade method in the terminal:
```bash
wget -qO- https://github.com/{nameid}/Nano-Openwrt/raw/main/scripts/autoupdate.sh | sh
```
slim Version
```bash
wget -qO- https://github.com/{nameid}/Nano-Openwrt/raw/main/scripts/autoupdate.sh | ver=-slim sh
```
(Script provided by Gary Lau, thank you very much!)

#### Firmware source code:
https://github.com/immortalwrt/immortalwrt


''')
f.close()
