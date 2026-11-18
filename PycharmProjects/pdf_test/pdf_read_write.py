# 필요한 라이브러리 import 하기
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# docstring 추가
# 함수 , 클래스, 모듈 구현부의 첫번째 문자열은 docstring 으로 인식
# PDF 파일에서 텍스트를 추출하는 함수
# path 파라미터로 PDF 파일의 경로를 받음
def extract_text_from_pdf(pdf_path):
    """
    PDF 파일에서 텍스트를 추출하는 함수
    :param pdf_path: 경로 포함한 PDF 파일 이름
    :return: 추출된 텍스트
    """

    # open 함수를 사용하여 pdf 파일을 바이너리 모드로 열기
    # with 구문은 파일을 자동으로 close 해주는 예약어
    with open(pdf_path, 'rb') as fp:

        # PDFParser 클래스를 이용하여 파일을 파싱
        parser = PDFParser(fp)

        # PDFDocument 객체 생성
        doc = PDFDocument(parser)

        # PDFResourceManager 클래스를 이용하여 공유 리소스(폰트, 이미지 등)를 관리
        rsrc = PDFResourceManager()

        # LAParams 클래스를 이용하여 레이아웃 분석 파라미터를 설정
        params = LAParams()

        # StringIO 클래스를 이용하여 텍스트를 저장할 출력 버퍼를 생성
        output = StringIO()


        # TextConverter 클래스를 이용하여 PDF를 텍스트로 변환
        device = TextConverter(rsrc, output, laparams=params)


        # PDFPageInterpreter 클래스를 이용하여 PDF 페이지를 해석하고 TextConverter로 전달
        interpreter = PDFPageInterpreter(rsrc, device)

        # PDFPage 클래스의 create_pages 메서드를 사용하여 PDF 페이지를 생성
        for page in PDFPage.create_pages(doc):
            # process_page() 를 사용하여 페이지 처리
            interpreter.process_page(page)


        # 출력 버퍼에 담겨져 있는 텍스트를 꺼낸다
        text = output.getvalue()

        device.close()
        output.close()

    print(text)
    return text

# save_text(text, filename) 함수는 추출된 텍스트를 인자로 받아서 지정된 파일 이름으로 저장
# text 인자는 저장할 텍스트이며, filename은 저장할 파일 이름
def save_text(text, filename):
    '''
    전달받은 텍스트를 txt 파일로 저장하는 함수.
    :param text: 저장할 텍스트
    :param filename: 저장할 파일 이름
    '''
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(text)


# pdf_sample.pdf 파일에서 텍스트를 추출
text = extract_text_from_pdf("pdf_sample.pdf")
save_text(text, "test.txt")


# 추출된 텍스트를 text 파일로 저장하기


