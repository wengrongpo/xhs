# 安装 Appium
FROM appium/appium:v1.22.3-p3

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . .

# 安装 Python 和其他必要工具
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

# 安装 Python 依赖
RUN pip3 install -r requirements.txt 

# 容器启动命令
CMD [ "python3", "app.py" ]