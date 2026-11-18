# pip install pyhwpx==0.10.30
from pyhwpx import Hwp

hwp = Hwp()

# 텍스트 삽입
hwp.insert_text("Hello world!\r\n")
hwp.insert_text("안녕 세상~\r\n")
hwp.insert_text("안녕 세상~\r\n")

# 다른이름으로 저장. hwp 와 hwpx 파일로 저장 가능
# hwp.save_as("./helloworld.hwp")
hwp.save_as("한글문서생성1.hwpx")

# 한/글 종료
hwp.quit()



