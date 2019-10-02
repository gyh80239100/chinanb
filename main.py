from automator import Automator

if __name__ == '__main__':

    # 连接 adb 。
    instance = Automator('127.0.0.1:62001')

    # 启动脚本。
    instance.start()
