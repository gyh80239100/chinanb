# JGM Automator-v2

>优化了Opencv识别速度慢的脚本
>增加了升级建筑功能
## 安装与运行

```bash
# 安装依赖
python -m pip install uiautomator2
# adb 连接
# 使用 MuMu 模拟器，确保屏幕大小为 1920（长） * 1080（宽）
adb connect 127.0.0.1:7555（不同模拟器端口不一样）
# 获取 device 名称,并填写至 main.py
adb devices
# 在已完成 adb 连接后，在手机安装 ATX 应用
python -m uiautomator2 init

# 打开 ATX ，点击“启动 UIAutomator”选项，确保 UIAutomator 是运行的。

# 进入游戏页面，启动自动脚本。
python main.py
```

## 说明

+ 建筑编号

<img src="./assets/Screenshot.png" style="zoom:40%" />

+ 升级建筑设置 automator.py中

<img src="./assets/UpdateBuiling.png" style="zoom:100%" />