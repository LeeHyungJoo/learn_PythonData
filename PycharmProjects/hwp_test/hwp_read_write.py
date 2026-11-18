# pip install pyhwpx==0.10.30
from pyhwpx import Hwp

hwp = Hwp()

result = []
with open('선형대수의기초참고문서.txt', encoding='utf-8') as f:
    # r = f.read()
    # print(r)
    # result.append(r)
    lines = f.readlines()
    for line in lines:
        print(line)
        result.append(line)

for r in result:
    hwp.insert_text(r+ "\r\n")

# 이미지 추가
hwp.insert_picture("image01.png")


# 다른이름으로 저장. hwp 와 hwpx 파일로 저장 가능
# hwp.save_as("./helloworld.hwp")
# hwp.save_as("선형대수의기초참고문서_write.hwpx")
hwp.save_as("선형대수의기초참고문서_write.hwp")

# 한/글 종료
hwp.quit()



