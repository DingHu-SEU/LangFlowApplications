# 使用JSON文件进行调用
from langflow.load import run_flow_from_json
import json
import logging

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1、模型相关配置
# # openai模型相关配置 根据自己的实际情况进行调整
MODEL_API_BASE = "https://sg.uiuiapi.com/v1"
MODEL_CHAT_API_KEY = "sk-BT6qbPpS2XxwH52aAdNOg51c9EfWx33woetUyrRxwEWm43Rt"
MODEL_CHAT_MODEL = "gpt-4o"

# oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整
# MODEL_API_BASE = "http://139.224.72.218:3000/v1"
# MODEL_CHAT_API_KEY = "sk-DoU00d1PaOMCFrSh68196328E08e443a8886E95761D7F4Bf"
# MODEL_CHAT_MODEL = "qwen-max"

EMBEDDING_API_BASE = "https://sg.uiuiapi.com/v1"
EMBEDDING_API_KEY = "sk-BIE3lMENbxsn5EEp2jV5sDeKFrteUILJ72rWXNcOj3fPVszW"
EMBEDDING_MODEL = "text-embedding-3-small"

# 2、prompt相关配置  引入外部的文件内容
sys_file_path = "prompt_template_system.txt"
# user_file_path = "prompt_template_user.txt"
with open(sys_file_path, 'r', encoding='utf-8') as file:
    PROMPT_TEMPLATE_TXT_SYS = file.read()
# with open(user_file_path, 'r', encoding='utf-8') as file:
#     PROMPT_TEMPLATE_TXT_USER = file.read()

# 3、引入LangFlow的json文件
TASKFLOW = 'PDFREADER.json'

# 4、构造测试消息体
input_text = "UNet++几句话简单概述"

TWEAKS = {
    "ChatInput-sRMFh": {
        "files": "",
        # "input_value": "UNet++几句话简单概述",
        "sender": "User",
        "sender_name": "User",
        "session_id": "",
        "should_store_message": True
    },
    "ParseData-jPkdE": {
        "sep": "\n",
        "template": "{text}"
    },
    "Prompt-BAX0m": {
        "context": "",
        "question": "",
        "template": "{context}\n\n---\n\nGiven the context above, answer the question as best as possible.\n\nQuestion: {question}\n\nAnswer: "
    },
    "ChatOutput-XVLBc": {
        "data_template": "{text}",
        # "input_value": "",
        "sender": "Machine",
        "sender_name": "AI",
        "session_id": "",
        "should_store_message": True
    },
    "SplitText-adnBP": {
        "chunk_overlap": 200,
        "chunk_size": 1000,
        "separator": "\n"
    },
    "OpenAIEmbeddings-c2HYk": {
        "chunk_size": 1000,
        "client": "",
        "default_headers": {},
        "default_query": {},
        "deployment": "",
        "dimensions": None,
        "embedding_ctx_length": 1536,
        "max_retries": 3,
        "model": EMBEDDING_MODEL,
        "model_kwargs": {},
        "openai_api_base": EMBEDDING_API_BASE,
        "openai_api_key": EMBEDDING_API_KEY,
        "openai_api_type": "",
        "openai_api_version": "",
        "openai_organization": "",
        "openai_proxy": "",
        "request_timeout": None,
        "show_progress_bar": False,
        "skip_empty": False,
        "tiktoken_enable": True,
        "tiktoken_model_name": ""
    },
    "OpenAIEmbeddings-Lvb2W": {
        "chunk_size": 1000,
        "client": "",
        "default_headers": {},
        "default_query": {},
        "deployment": "",
        "dimensions": None,
        "embedding_ctx_length": 1536,
        "max_retries": 3,
        "model": EMBEDDING_MODEL,
        "model_kwargs": {},
        "openai_api_base": EMBEDDING_API_BASE,
        "openai_api_key": EMBEDDING_API_KEY,
        "openai_api_type": "",
        "openai_api_version": "",
        "openai_organization": "",
        "openai_proxy": "",
        "request_timeout": None,
        "show_progress_bar": False,
        "skip_empty": False,
        "tiktoken_enable": True,
        "tiktoken_model_name": ""
    },
    "OpenAIModel-aCvur": {
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
    "File-XgdcD": {
        "path": "D:\\Desktop\\代码学习\\langflow\\UNet",
        "silent_errors": False
    },
    "Chroma-TFYmy": {
        "allow_duplicates": False,
        "chroma_server_cors_allow_origins": "",
        "chroma_server_grpc_port": None,
        "chroma_server_host": "",
        "chroma_server_http_port": None,
        "chroma_server_ssl_enabled": False,
        "collection_name": "langflow",
        "limit": None,
        "number_of_results": 10,
        "persist_directory": "PDFa",
        "search_query": "",
        "search_type": "Similarity"
    },
    "Chroma-UMQ9z": {
        "allow_duplicates": False,
        "chroma_server_cors_allow_origins": "",
        "chroma_server_grpc_port": None,
        "chroma_server_host": "",
        "chroma_server_http_port": None,
        "chroma_server_ssl_enabled": False,
        "collection_name": "langflow",
        "limit": None,
        "number_of_results": 10,
        "persist_directory": "PDFa",
        "search_query": "",
        "search_type": "Similarity"
    },
    "Prompt-7rOHR": {
        "template": PROMPT_TEMPLATE_TXT_SYS
    }
}

result = run_flow_from_json(flow=TASKFLOW,
                            input_value=input_text,
                            fallback_to_env_vars=True,  # False by default
                            tweaks=TWEAKS)

# # 解析具体回复的内容
logger.info(f"输出响应内容是: {result}\n")
content = result[0].outputs[0].results['message'].text
logger.info(f"输出响应内容是: {content}\n")
