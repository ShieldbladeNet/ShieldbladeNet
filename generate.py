import requests, json, random, time
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
f = open("./README.md", "w")

f.write(f'''

<h3 align="center"><b>{timestr}</b></h3>
<h3 align="center">Have a nice day!</h3>
<p align="center">
  <a href="https://github.com/ShieldbladeNet">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=ShieldbladeNet&hide=issues&hide_title=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff" />
    </a>
</p>
<p align="center">

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/ShieldbladeNet/Nano-Openwrt?style=for-the-badge&label=Download)](https://github.com/ShieldbladeNet/Nano-Openwrt/releases)

</p>       

OpenWrt (from open wireless router) is an open-source project for embedded operating systems based on Linux, primarily used on embedded devices to route network traffic. The main components are Linux, util-linux, musl,[4] and BusyBox. All components have been optimized to be small enough to fit into the limited storage and memory available in home routers.

OpenWrt is configured using a command-line interface (ash shell) or a web interface (LuCI). There are about 3500 optional software packages available for installation via the opkg package management system.

OpenWrt can run on various types of devices, including CPE routers, residential gateways, smartphones, pocket computers (e.g. Ben NanoNote). It is also possible to run OpenWrt on personal computers and laptops, which are most commonly based on the x86 architecture.

[![build_firmware](https://github.com/ShieldbladeNet/Nano-Openwrt/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/ShieldbladeNet/Nano-Openwrt/actions/workflows/build-firmware.yml)

''')
f.close()
