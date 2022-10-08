import requests, time, linecache, os, subprocess, sys, json, threading
    
def Check_Update():
    while True: 
        try:
            GetVersion = (linecache.getline(InfPath,3)).split('PatchVersion=')[1]
            APIGet = requests.get('http://api.steampowered.com/ISteamApps/UpToDateCheck/v1/?appid=730&version=' + GetVersion)
            APIGet.encoding = 'utf-8'
            APIGetJson = json.loads(APIGet.text)
            if str(APIGetJson["response"]["up_to_date"]) == 'True':
                print("[AU] 未检测到更新...持续探测中...\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
            else:
                print("[AU] 版本已超时\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                thread2.updating = False
                time.sleep(2)
                os.system('taskkill /f /t /im srcds.exe>nul')
                try:
                    for UpdateNum in range(int(ServerNum)):
                        UpdatePath = str((json.loads(linecache.getline('AUToolConfig.ini',int(int(UpdateNum) + 2))))["SteamcmdPath"])
                        UpdateDir = str((json.loads(linecache.getline('AUToolConfig.ini',int(int(UpdateNum) + 2))))["CsgoServerPath"])
                        print("[AU] 正在更新端口为" + str(AllPort[UpdateNum]) + "的服务器...\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                        if UpdateDir == 'Def' or UpdateDir == 'def' or UpdateDir == '':
                            try:
                                os.system('cd /d ' + UpdatePath + '&&echo @echo off >AUDownLoad.bat')
                                os.system('cd /d ' + UpdatePath + '&&echo steamcmd +login anonymous +app_update 740 validate +quit >>AUDownLoad.bat')
                                os.system('echo @echo off >AUDownLoadStart.bat')
                                os.system('echo cd /d ' + UpdatePath + ' >>AUDownLoadStart.bat')
                                os.system('echo call AUDownLoad.bat >>AUDownLoadStart.bat')
                                UpdateShell = subprocess.Popen(['AUDownLoadStart.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1, encoding='utf-8')
                                while UpdateShell.poll() is None:
                                    print(UpdateShell.stdout.readline())
                                print("[AU] 端口为" + str(AllPort[UpdateNum]) + "的服务器更新成功！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                            except:
                                print("[AU] 端口为" + str(AllPort[UpdateNum]) + "的服务器更新失败！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                        else:
                            try:
                                os.system('cd /d ' + UpdatePath + '&&echo @echo off >AUDownLoad.bat')
                                os.system('cd /d ' + UpdatePath + '&&echo steamcmd +login anonymous +force_install_dir ' + UpdateDir + ' +app_update 740 validate +quit >>AUDownLoad.bat')
                                os.system('echo @echo off >AUDownLoadStart.bat')
                                os.system('echo cd /d ' + UpdatePath + ' >>AUDownLoadStart.bat')
                                os.system('echo call AUDownLoad.bat >>AUDownLoadStart.bat')
                                UpdateShell = subprocess.Popen(['AUDownLoadStart.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1, encoding='utf-8')
                                while UpdateShell.poll() is None:
                                    print(UpdateShell.stdout.readline())
                                print("[AU] 端口为" + str(AllPort[UpdateNum]) + "的服务器更新成功！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                            except:
                                print("[AU] 端口为" + str(AllPort[UpdateNum]) + "的服务器更新失败！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                        time.sleep(5)
                        os.system('cd /d ' + UpdatePath + '&&del /f /s /q AUDownLoad.bat')
                        time.sleep(15)
                    UpdateNum = UpdateNum + 1
                    print("[AU] 全部服务器更新成功！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                    os.system('del /f /s /q AUDownLoadStart.bat')
                    time.sleep(3)
                    thread4.start()
                except:
                    print("[AU] 在更新Srcds时发生未知错误，故全部/部分服务器更新失败\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
        except:
            print("[AU] 无法连接SteamAPI服务器，将于5分钟后重试\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
            time.sleep(180)
        time.sleep(120)

def Check_Crash():
    Current_Thread = threading.current_thread()
    while getattr(Current_Thread, "updating", True):
        try:
            for CurPort in range(int(ServerNum)):
                Test1Get = requests.get('http://43.143.135.75:18888/index.php?method=xPaw&host=' + str(IPAddress) + '&port=' + str(AllPort[CurPort]) + '&type=info')
                Test1Get.encoding = 'utf-8'
                Test1GetJson = json.loads(Test1Get.text)
                CurPort = CurPort + 1
            print("[AS] 全部服务器状态正常！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
        except:
            Test2Get = requests.get('http://43.143.135.75:18888/Test.test')
            Test2Get.encoding = 'utf-8'
            if Test2Get.text == 'True':
                InstallMode = str((json.loads(linecache.getline('AUToolConfig.ini',int(int(CurPort) + 2))))["CsgoServerPath"])
                StartConfig = str((json.loads(linecache.getline('AUToolConfig.ini',int(int(CurPort) + 2))))["ServerStartConfig"])
                print("[AS] 端口为" + str(AllPort[CurPort]) + "的服务器已崩溃，正在重启...\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                if InstallMode == 'Def' or InstallMode == 'def' or InstallMode == '':
                    try:
                        SrcdsPath = str((json.loads(linecache.getline('AUToolConfig.ini',int(int(CurPort) + 2))))["SteamcmdPath"]) + '\steamapps\common\Counter-Strike Global Offensive Beta - Dedicated Server'
                        os.popen("cd /d " + SrcdsPath + "&&srcds.exe " + StartConfig)
                        print("[AS] 端口为" + str(AllPort[CurPort]) + "的服务器重启成功！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                    except:
                        print("[AS] 端口为" + str(AllPort[CurPort]) + "的服务器重启失败！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                else:
                    try:
                        SrcdsPath = str((json.loads(linecache.getline('AUToolConfig.ini',int(int(CurPort) + 2))))["CsgoServerPath"])
                        os.popen("cd /d " + SrcdsPath + "&&srcds.exe " + StartConfig)
                        print("[AS] 端口为" + str(AllPort[CurPort]) + "的服务器重启成功！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                    except:
                        print("[AS] 端口为" + str(AllPort[CurPort]) + "的服务器重启失败！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                time.sleep(30)
            else:
                print("[AS] 无法连接API服务器，将于15分钟后重试\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
                time.sleep(900)
        time.sleep(30)

def Clear_Out():
    ClearCount = 1
    while True:
        CoolDown = int((json.loads(linecache.getline('AUToolConfig.ini',1)))["ClearCoolDown"])
        time.sleep(int(CoolDown * 60))
        os.system("cls")
        TitleSet = "[AM] 已成功完成第[" + str(ClearCount) + "]次清屏 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]"
        os.system('title' + TitleSet)
        ClearCount = ClearCount + 1

def Restart():
    os.system('cd %cd%&&echo ping -n 6 127.0.0.1^>nul>AutoUpdateRestart.bat&&echo start ' + os.path.basename(sys.argv[0]) + '>>AutoUpdateRestart.bat')
    time.sleep(1)
    os.system('start AutoUpdateRestart.bat')
    os._exit(0)
    
if __name__ == '__main__':
    os.system('color 0f')
    os.system('title CSGO Server Auto Manger Tool')
    thread1 = threading.Thread(target=Check_Update)
    thread2 = threading.Thread(target=Check_Crash)
    thread3 = threading.Thread(target=Clear_Out)
    thread4 = threading.Thread(target=Restart)
    ServerNum = str((json.loads(linecache.getline('AUToolConfig.ini',1)))["ServerNum"])
    if linecache.getline('AUToolConfig.ini',int(int(ServerNum) + 1)) == '\n' or linecache.getline('AUToolConfig.ini',int(int(ServerNum) + 1)) == '' :
        print("[AM] 配置文件配置错误！\t\t\t [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
    IPAddress = str((json.loads(linecache.getline('AUToolConfig.ini',1)))["IPAddress"])
    AllPort = []
    for Port in range(int(ServerNum)):
        AllPort.append(str((json.loads(linecache.getline('AUToolConfig.ini',1)))['Port' + str(Port)]))
        Port = Port + 1
    InstallPath = str((json.loads(linecache.getline('AUToolConfig.ini',2)))["CsgoServerPath"])
    if InstallPath == 'Def' or InstallPath == 'def' or InstallPath == '':
        InfPath = str((json.loads(linecache.getline('AUToolConfig.ini',2)))["SteamcmdPath"]) + '\steamapps\common\Counter-Strike Global Offensive Beta - Dedicated Server\csgo\steam.inf'
    else:
        InfPath = str((json.loads(linecache.getline('AUToolConfig.ini',2)))["CsgoServerPath"]) + '\csgo\steam.inf'
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
