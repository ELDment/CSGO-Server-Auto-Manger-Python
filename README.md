# ✨CSGO服务器自动管理✨
![Language](https://img.shields.io/badge/language-python-green.svg?style=plastic)
![License](https://img.shields.io/badge/license-GPL-orange.svg?style=plastic)
![Python](https://img.shields.io/badge/python-3.10+-blue)<br />
**前言：**<br />
**我花了大约12天来写这个很烂的项目**<br />
**因为我在写这个项目的时候我遇到了许多难题**<br />
**感谢茶糜的服务器！**<br />
**如有问题请发起Issue或者加我QQ：3612903372**<br />
## 现有功能
**CSGO服务端批量自动更新**<br />
**CSGO服务端自动重启（如果崩溃）**<br />
## 使用教程
**AUToolConfig.ini中内容**<br />
```css
{"ClearCoolDown":"清屏冷却间隔", "ServerNum":"服务器个数", "IPAddress":"你当前服务器的IP", "Port0": "第一个服务端端口", "Port1": "第二个服务端端口", ..., "Portn": "第n+1个服务端端口"}
{"SteamcmdPath":"Steamcmd所在路径", "CsgoServerPath":"安装路径（如使用Force_install_dir直接填写dir即可，如未使用不填或者填写'Def'或'def'）", "ServerStartConfig":"启动参数"}
...有多少个服务端这里就写入多少条
{"SteamcmdPath":"Steamcmd所在路径", "CsgoServerPath":"安装路径（如使用Force_install_dir直接填写dir即可，如未使用不填或者填写'Def'或'def'）", "ServerStartConfig":"启动参数"}
```
**举个例子**<br />
```css
{"ClearCoolDown":"5", "ServerNum":"3", "IPAddress":"202.189.7.59", "Port0": "27900", "Port1": "27400", "Port2": "27600"}
{"SteamcmdPath":"C:/steamcmd", "CsgoServerPath":"Def", "ServerStartConfig":"-game csgo -console -ip 0.0.0.0 -usercon +game_type 0 +game_mode 0 +port 27015 +map de_dust2 -tickrate 128 -maxplayers_override 32 +mapgroup mg_active"}
{"SteamcmdPath":"D:/steamcmd", "CsgoServerPath":"D:/CSGO", "ServerStartConfig":"-game csgo -console -ip 0.0.0.0 -usercon +game_type 0 +game_mode 0 +port 27015 +map de_dust2 -tickrate 128 -maxplayers_override 32 +mapgroup mg_active"}
{"SteamcmdPath":"D:/steam", "CsgoServerPath":"def", "ServerStartConfig":"-game csgo -console -ip 0.0.0.0 -usercon +game_type 0 +game_mode 0 +port 27015 +map de_dust2 -tickrate 128 -maxplayers_override 32 +mapgroup mg_active"}
```
