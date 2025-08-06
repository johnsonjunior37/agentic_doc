from agentic_doc.parse import parse_documents
from agentic_doc.utils import viz_parsed_document

# 假設有 input.pdf
pdf_path = "test1.pdf"
results = parse_documents([pdf_path])

# 顯示第一頁解析結果
viz_parsed_document(results[0])
