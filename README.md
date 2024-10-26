# 1、项目简介

使用开源的LangFlow框架，实现自主升级的大模型相关科研应用如文献理解、文献翻译和文本学术化语言润色等，并使用两种方式将创建的工作流集成到自己的项目中 。

# 2、基础概念

## 2.1 LangFlow简介

官方介绍:一种用于构建多智能体和RAG应用的可视化框架                                 GitHub地址:https://github.com/langflow-ai/langflow                           
开源协议:MIT协议   

# 3、使用前期准备

## STEP 1 GIT代码到本地

GitHub地址：https://github.com/DingHu-SEU/LangFlowApplications.git

## STEP 2 anaconda、pycharm 安装 

anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可              pycharm:提供集成开发环境，官网下载社区版本安装包安装即可

## STEP 3 python环境安装

anaconda环境安装好之后，在其上构建python环境，本项目使用python3.10版本。

```
conda create -n langflow python=3.10 # 创建langflow环境
conda activate langflow # 激活环境
```

## STEP 4 创建线上大模型的渠道和令牌

可以使用：https://sg.uiuiapi.com/        API聚合平台创建

# 4、项目初始化

## 4.1 构建项目
使用pycharm构建一个项目，为项目配置创建好的虚拟python环境langflow             
项目名称：LangFlowTest                 

## 4.2 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到新建的项目目录中               

## 4.3 安装项目依赖          
pip install -r requirements.txt            
每个软件包后面都指定了本次视频测试中固定的版本号   

# 5、项目运行

### (1)项目启动
首先，在终端命令行中启动LangFlow服务，执行 langflow run 命令启动                   启动成功后，登陆http://127.0.0.1:7860，在服务页面进入store菜单中创建API Key                            
最后进入My Collection菜单中新建工程进行工作流编排，测试没问题后，导出工作流json文件

### (2)通过调用API接口方式使用创建的工作流
进入任一文件夹下，在使用python fromApiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                        
**模型相关配置 根据自己的实际情况进行调整**                            

### (3)通过调用工作流的json文件使用工作流
进入任一文件夹下，在使用python fromJsonTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                             
**模型相关配置 根据自己的实际情况进行调整**           
**引入LangFlow的json文件** 

可参考视频：

https://www.bilibili.com/video/BV1HYpqexEDm/?spm_id_from=333.999.0.0&vd_source=0ce10c8325b331948d919a117320821a

# 6、关于使用RAG构建向量库

离线步骤:文档加载->文档切分->向量化->灌入向量数据库              
在线步骤:获取用户问题->用户问题向量化->检索向量数据库->将检索结果和用户问题填入prompt模版->用最终的prompt调用LLM->由LLM生成回复                         

### (1)Chroma数据库
向量数据库，专门为向量检索设计的中间件              
使用本地持久化存储方案 持久化一个本地文件夹             

### (2)本地开源大模型，Ollama方案
Ollama是一个轻量级、跨平台的工具和库，专门为本地大语言模型(LLM)的部署和运行提供支持          
它旨在简化在本地环境中运行大模型的过程，不需要依赖云服务或外部API，使用户能够更好地掌控和使用大型模型                
安装Ollama，进入官网https://ollama.com/下载对应系统版本直接安装即可                           
启动Ollama，安装所需要使用的本地模型，执行指令进行安装即可:    

```
ollama pull qwen2:latest                                     
ollama pull llama3.1:latest                                   
ollama pull nomic-embed-text:latest    
```

可使用的模型搭配如下:                  
chat模型:qwen2:latest(7b),对应版本有0.5b、1.5b、7b、72b;llama3.1:latest(8b)，对应版本有8b、70b、405b等                
embedding模型:nomic-embed-text:latest(也就是1.5版本)                     
具体安装相关的细节，可以参考视频:                                           
【GraphRAG+Ollama】本地开源大模型llama3.1与qwen2构建+检索全流程实操对比评测，打造基于知识图谱的本地知识库，本地搜索、全局搜索二合一             
https://www.bilibili.com/video/BV1mpH9eVES1/?vd_source=30acb5331e4f5739ebbad50f7cc6b949               
https://youtu.be/thNMan45lWA 

