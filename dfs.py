import subprocess
try:
 subprocess.run(["python", "수강 리스트 추가본.py"], check=True)
except subprocess.CalledProcessError as e:
 print(f"TOEIC_수정본.py 실행 중 에러가 발생했습니다: {e}")
