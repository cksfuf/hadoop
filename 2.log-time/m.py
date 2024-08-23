import sys
import re

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()
    # line.split(':')[1] 콜론(:)을 기준으로 분류하고, 분류한 데이터 1번째 자리를 가져오는 식임 이렇게해도됨
    # 오늘은 정규표현식 사용해보기

    # time_pattern에 작성한 패턴에 일치하는 부분 찾기
    match = time_pattern.search(line)    
    if match: # 만약 일치하는 부분이 있다면
        hour = match.group(1)
        print(f'{hour}\t1')