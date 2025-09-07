import requests
from typing import Dict

url: str="http://localhost:8000"

body: Dict={
     "jsonrpc": "2.0",
     "id": 1,
     "method": "tools/list",
     "params": {
          "name": "read_docs",
          "arguments": {
              "doc_url": "D:\\mcp_openai-agent-sdk\\doc_1.txt"
          }
          
     }
}

response: str= requests.post(url, headers={"Accept": "application/json,text/event-stream"}, json= body)
print(response.text)