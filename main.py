from agentic_doc.parse import parse_documents
from agentic_doc.utils import viz_parsed_document
import os

# 將你的 API 金鑰存在環境變數中
os.environ["VISION_AGENT_API_KEY"] = "YTluYnhqNjBscW5xcTZsZjZhYzVzOjF1aWdBcEJMUGNWQ1pYdEtPYXdoRVhJWUw4YnBlV0xN"
# 假設有 input.pdf
pdf_path = "test1.pdf"
results = parse_documents([pdf_path])

# 顯示第一頁解析結果
viz_parsed_document(results[0])
