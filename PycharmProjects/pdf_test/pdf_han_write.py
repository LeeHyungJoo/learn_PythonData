from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_pdf(file_path):
    # 캔버스 생성
    pdf_canvas = canvas.Canvas(file_path)

    # 한글 폰트 추가
    pdfmetrics.registerFont(TTFont('NanumBarunGothic', 'NanumBarunGothic.ttf'))

    # 한글 포함 텍스트 추가
    # 한글 폰트를 설정
    pdf_canvas.setFont('NanumBarunGothic', 12)
    # 한글 포함 텍스트를 추가. x 축과 y 축 위치 지정
    pdf_canvas.drawString(100, 750, "안녕하세요!")

    # PDF 저장
    pdf_canvas.save()


# 이 코드에서 text_lines 리스트에 여러 줄의 텍스트를 추가
# drawString 메서드를 사용하여 각 줄을 출력
# y_position 변수를 사용하여 각 줄 사이의 간격을 조절
# line_height 변수를 통해 간격 크기를 조절

def create_pdf2(file_path):
    pdf_canvas = canvas.Canvas(file_path)
    pdfmetrics.registerFont(TTFont('NanumBarunGothic', 'NanumBarunGothic.ttf'))
    pdf_canvas.setFont('NanumBarunGothic', 12)

    # 여러 줄의 텍스트를 출력
    text_lines = [
        "안녕하세요!",
        "이곳에 다른 줄의 내용을 추가할 수 있습니다.",
        "예를 들어, 새로운 줄에 특별한 내용을 넣을 수 있습니다."
    ]

    y_position = 750  # 시작 Y 좌표
    line_height = 14  # 줄 간격

    for line in text_lines:
        pdf_canvas.drawString(100, y_position, line)
        y_position -= line_height

    pdf_canvas.save()

# __main__설명
# PDF 생성 실행
if __name__ == '__main__':
    create_pdf("example2_1.pdf")
    create_pdf2("example2_2.pdf")
