# https://blog.hanlee.io/2022/hwp-rs
#pip install libhwp==0.2.0

from libhwp import HWPReader

# 실습1. ok
hwp = HWPReader('한글테이블1.hwp')

# 실습2. ok
# hwp = HWPReader('선형대수의기초참고문서_write.hwp')

# 아래 문서는 에러. 아래아 한글의 버전때문인듯
# hwp = HWPReader('선형대수의기초참고문서.hwp')
# 아래 코드는 에러. ~.hwpx 는 지원하지 않음
#hwp = HWPReader('한글테이블1.hwpx')

# 모든 문단 출력 (표, 캡션 포함)
for paragraph in hwp.find_all('paragraph'):
    print(paragraph)
print("=" * 30)

# 표 내용 출력 (표 안의 표 포함)
for table in hwp.find_all('table'):
    for cell in table.cells:
        for paragraph in cell.paragraphs:
            print(paragraph)

