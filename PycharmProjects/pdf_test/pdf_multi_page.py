# 라이브러리 import
from fpdf import FPDF
import warnings
warnings.filterwarnings("ignore")

# FPDF 객체 생성
pdf = FPDF()

# 페이지 추가
pdf.add_page()

# 한글 폰트 설정
pdf.add_font("NanumBarunGothic", "", "NanumBarunGothic.ttf", uni=True)
pdf.set_font("NanumBarunGothic", "", 16)

# 첫 페이지에 출력할 내용. 가로, 세로, 텍스트, 보더, 가로축마진
# cell(self, w,h=0,txt='',border=0,ln=0,align='',fill=0,link='')
# pdf.cell(0, 10, '첫 번째 페이지입니다.', 0, 1)
# pdf.cell(10, 10, '첫 번째 페이지입니다.', 0, 1)

for i in range(10):
    pdf.cell(i, 10, f"첫번재 페이지 {i+1:0>2}번째 라인입니다.", 0, 1);


# 다음 페이지로 이동
pdf.add_page()

# 두 번째 페이지에 출력할 내용
for i in range(10):
    pdf.cell(i, 10, f"두번재 페이지 {i+1:0>2}번째 라인입니다.", 0, 1);

# 파일로 저장
pdf.output("fpdf_ex.pdf")

