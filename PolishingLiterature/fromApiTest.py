# 使用API接口进行调用
import requests
import json
import logging

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1、模型相关配置
# # openai模型相关配置 根据自己的实际情况进行调整
MODEL_API_BASE = "https://sg.uiuiapi.com/v1"
MODEL_CHAT_API_KEY = "sk-HGh1fXkzJphvPtLVarO3rIZBJan0d7rTlOMgrV7AyCIowzGM"
MODEL_CHAT_MODEL = "gpt-4o-mini"

# oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整
# MODEL_API_BASE = "http://139.224.72.218:3000/v1"
# MODEL_CHAT_API_KEY = "sk-DoU00d1PaOMCFrSh68196328E08e443a8886E95761D7F4Bf"
# MODEL_CHAT_MODEL = "qwen-max"


# 2、prompt相关配置  引入外部的文件内容
# sys_file_path = "prompt_template_system.txt"
# user_file_path = "prompt_template_user.txt"
# with open(sys_file_path, 'r', encoding='utf-8') as file:
#     PROMPT_TEMPLATE_TXT_SYS = file.read()
# with open(user_file_path, 'r', encoding='utf-8') as file:
#     PROMPT_TEMPLATE_TXT_USER = file.read()


# 3、API请求相关配置
url = "http://127.0.0.1:7860/api/v1/run/PolishingLiterature"
headers = {"Content-Type": "application/json"}


# 4、构造测试消息体

data = {
    "input_value": "message",
    "output_type": "chat",
    "input_type": "text",
    "tweaks": {
      "SequentialCrewComponent-V4nfT": {
        "max_rpm": 100,
        "memory": False,
        "share_crew": False,
        "use_cache": True,
        "verbose": 0
      },
      "OpenAIModel-zwyyU": {
        "api_key": MODEL_CHAT_API_KEY,
        # "input_value": "",
        "json_mode": False,
        "max_tokens": None,
        "model_kwargs": {},
        "model_name": MODEL_CHAT_MODEL,
        "openai_api_base": MODEL_API_BASE,
        "output_schema": {},
        "seed": 1,
        "stream": False,
        "system_message": "",
        "temperature": 0.1
      },
      "ChatOutput-HH5Tg": {
        "data_template": "{text}",
        # "input_value": "",
        "sender": "Machine",
        "sender_name": "AI",
        "session_id": "",
        "should_store_message": True
      },
      "Prompt-NFnav": {
        "template": "Document: {document}\n\nPolish the document using academic language.",
        "document": ""
      },
      "SequentialTaskAgentComponent-kGAEz": {
        "agent_kwargs": {},
        "allow_code_execution": False,
        "allow_delegation": False,
        "async_execution": False,
        "backstory": "你是世界上最卓越的学术化语言编辑",
        "expected_output": "高学术化的经润色后的英文文本",
        "goal": "你应该提供基于输入文本的高学术化的经润色后的英文文本，使用SCI期刊标准的论文语言 ",
        "memory": True,
        "role": "SCI Editor",
        "task_description": "",
        "verbose": True
      },
      "ParseData-rKIr6": {
        "sep": "\n",
        "template": "{text}"
      },
      "File-i8joV": {
        "path": "D:\\Desktop\\代码学习\\langflow\\test.txt",
        "silent_errors": False
      }
    }
}


# 5、发送post请求进行测试
response = requests.post(url, headers=headers, data=json.dumps(data))
# 检查响应状态码
if response.status_code == 200:
    try:
        logger.info(f"输出响应内容是: {response.status_code}\n")
        logger.info(f"输出响应内容是: {response.json()}\n")
        # 解析具体回复的内容
        content = response.json()['outputs'][0]['outputs'][0]['results']['message']['data']['text']
        logger.info(f"输出响应内容是: {content}\n")
    except requests.exceptions.JSONDecodeError:
        # 响应不是JSON格式
        logger.info("Response content is not valid JSON")
else:
    logger.info(f"Request failed with status code {response.status_code}")



