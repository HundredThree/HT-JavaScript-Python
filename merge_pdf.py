from PyPDF2 import PdfMerger
import io

def merge_pdfs(pdf_files):
    """合并传入的 PDF 文件，并返回合并后的二进制数据"""
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(io.BytesIO(pdf_file))
    output = io.BytesIO()
    merger.write(output)
    merger.close()
    return output.getvalue()
