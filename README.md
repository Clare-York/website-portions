# README

运行环境：windows/linux/macOS

语言：python3.5+

### 设计思想

通过爬虫程序，对站点进行简单爬取，通过相应码和关键词判断网站是否发生异常，如有异常则通过邮件和短信通知负责人及时处理

##### 依赖安装

```python
pip install -r requirements.txt
```

#### 配置

项目目录>config>settings.py

邮箱使用smtp，短信使用的云片SDK

##### 运行：

```shell
python3 manager.py
```

