# TODO
# os 모듈을 사용해서 명령 프롬프트에서 실행할 명령들을 파이썬 코드에서 실행. (os 명령 가능)

import os

# path = "변환하고 싶은 한글 파일의 경로"
path = "선형대수의기초참고문서.hwp"
exefile = "hwp5txt"


filename = path[:path.rfind(".")] + ".txt"

print(filename)

# output = '--output ' + '"' + dirname + filename + '"'
output = "--output " + "\"" + filename + "\""
result = "\"" + path + "\""

os.system(exefile + " " + output + " " + result)
