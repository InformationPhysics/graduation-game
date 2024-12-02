import subprocess 
try:
 subprocess.run(["python", "TOEIC_수정본.py"], check=True)
except subprocess.CalledProcessError as e:
 print(f"TOEIC수정.py 실행 중 에러가 발생했습니다: {e}")
