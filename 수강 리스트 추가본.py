import threading
import time

# 강의 정보 초기화
_cls = [  # 강의 정보를 저장하는 리스트
    ["PHYS3305-01", 2024, 1, "양자역학1", 3, 10, 0],   # [코드, 연도, 학기, 강의명, 학점, 최대인원, 현재신청자수]
    ["PHYS2201-01", 2024, 1, "역학1", 3, 10, 0],
    ["GEC1102-S21", 2024, 1, "인간의가치탐색", 3, 20, 0],
    ["PHYS3204-00", 2024, 1, "열및통계물리1", 3, 10, 0],
    ["SOJUJOA-00", 2024, 1, "술의역사", 3, 15, 0],
    ["CHUKGUJOA-01", 2024, 1, "축구", 1, 22, 0],
    ["PHYS3203-01", 2024, 1, "전자기학2", 3, 10, 0],
    ["DISP2103-00", 2024, 1, "전자회로", 3, 10, 0],
    ["PHYS4201-00", 2024, 1, "졸업논문", 0, 100, 0],
    ["UMAYGETF-01", 2024, 1, "열및통계물리1", 3, 20, 0],
    ["PHYS3310-00", 2024, 1, "정보물리학", 3, 20, 0],
    ["GEE1345-S00", 2024, 1, "파이썬으로배우는소프트웨어코딩", 3, 20, 0],
    ["PHYS2302-00", 2024, 1, "수리물리학1", 3, 20, 0]
]

# 필수과목 리스트
todo_sugang_list = ["PHYS3305-01", "PHYS2201-01", "PHYS3204-00", "PHYS3203-01", "PHYS4201-00"]

_st = []   # 학생 정보를 저장하는 리스트

stop_auto_increment = threading.Event()  # 자동 증가 중지 이벤트
cls_lock = threading.Lock()  # 강의 정보에 대한 락
st_lock = threading.Lock()   # 학생 정보에 대한 락

# 강의 관리 클래스
class Manage:
    def add_subscription(self, cls_code):
        with cls_lock:
            f_index = self.search_index(cls_code)
            if f_index == -1:
                print(f"[ERROR] {cls_code}: 강의 코드를 찾을 수 없습니다.")
                return False
            if _cls[f_index][6] >= _cls[f_index][5]:  # 현재 신청자 수 >= 최대 수강 가능 인원
                print(f"[ERROR] {cls_code}: 수강 가능 인원을 초과했습니다.")
                return False
            else:
                _cls[f_index][6] += 1
                print(f"[SUCCESS] {cls_code}: 수강 신청 완료. 현재 신청자 수 {_cls[f_index][6]}/{_cls[f_index][5]}")
                return True

    def cancel_subscription(self, cls_code):
        with cls_lock:
            f_index = self.search_index(cls_code)
            if f_index != -1 and _cls[f_index][6] > 0:
                _cls[f_index][6] -= 1
                print(f"[INFO] {cls_code}: 수강 신청이 취소되어 현재 신청자 수 {_cls[f_index][6]}/{_cls[f_index][5]}")

    def search_index(self, cls_code):
        for i, cls in enumerate(_cls):
            if cls[0] == cls_code:
                return i
        return -1  # 찾지 못한 경우 -1 반환

    def get_lecture(self, cls_code):
        f_index = self.search_index(cls_code)
        return _cls[f_index][3] if f_index != -1 else None

    def auto_increment_subscriptions(self):
        while not stop_auto_increment.is_set():
            with cls_lock:
                for cls in _cls:
                    if cls[6] < cls[5]:  # 현재 신청자 수가 최대 인원을 넘지 않았을 때만 증가
                        cls[6] += 1
            time.sleep(1)  # 1초마다 실행

# 학생 클래스
class Student:
    def register(self, st_id, st_pass, st_num, st_name, st_dept, st_year):
        with st_lock:
            _st.append([st_id, st_pass, st_num, st_name, st_dept, st_year, [], 0])  # 빈 리스트로 수강 과목 초기화, 총 학점 0으로 초기화

# 수강신청 관리 클래스
class Sugang:
    def add_sugang_list(self, st_id, cls_code):
        with st_lock:
            f_index = self.search_index(st_id)
            if f_index == -1:
                print("[ERROR] 학생 ID를 찾을 수 없습니다.")
                return False
            if cls_code in _st[f_index][6]:  # 이미 수강 중인 과목이면 중복 수강 방지
                print(f"[ERROR] 학생 {_st[f_index][3]}({st_id})는 이미 {cls_code}를 수강 신청했습니다.")
                return False
            _st[f_index][6].append(cls_code)
            print(f"[SUCCESS] 학생 {_st[f_index][3]}({st_id}): {cls_code} 수강신청 완료.")
            return True

    def remove_sugang_list(self, st_id, cls_code):
        with st_lock:
            f_index = self.search_index(st_id)
            if f_index == -1:
                return
            if cls_code in _st[f_index][6]:
                _st[f_index][6].remove(cls_code)

    def search_index(self, st_id):
        for i, st in enumerate(_st):
            if st[0] == st_id:
                return i
        return -1

def main():
    students = Student()
    manage = Manage()
    sugang = Sugang()

    # 학생 등록은 반드시 처음에 실행되도록 설정
    print("\n=== 학생 등록 ===")
    st_id = input("학생 ID: ")
    st_pass = input("비밀번호: ")
    st_num = input("학번: ")
    st_name = input("이름: ")
    st_dept = input("학과: ")
    st_year = int(input("학년: "))
    students.register(st_id, st_pass, st_num, st_name, st_dept, st_year)
    print(f"[SUCCESS] 학생 {st_name}({st_id}) 등록 완료.")

    auto_thread = None
    logged_in = False
    logged_in_user = None
    login_attempts = 0

    while True:
        print("\n=== 수강신청 시스템 ===")
        print("1. 로그인")
        print("2. 수강 신청")
        print("3. 강의 목록 보기")
        print("4. 종료")
        choice = input("선택: ")

        if choice == "1":
            # 로그인
            while login_attempts < 5:
                login_id = input("로그인 ID: ")
                login_pass = input("비밀번호: ")
                f_index = sugang.search_index(login_id)
                if f_index == -1:
                    print("[ERROR] 등록된 ID가 없습니다.")
                elif _st[f_index][1] != login_pass:
                    print("[ERROR] 비밀번호가 올바르지 않습니다.")
                else:
                    print("[SUCCESS] 로그인 성공.")
                    logged_in = True
                    logged_in_user = login_id
                    break
                login_attempts += 1
            if login_attempts >= 5:
                print("[ERROR] 오류 가능 횟수를 초과했습니다. 시스템을 종료합니다.")
                return

        elif choice == "2":
            if not logged_in:
                print("[ERROR] 먼저 로그인 해주세요.")
                continue

            if auto_thread is None:
                # 자동 신청자 증가 스레드 시작
                auto_thread = threading.Thread(target=manage.auto_increment_subscriptions, daemon=True)
                auto_thread.start()

            # 수강 신청
            cls_code = input("수강할 강의 코드: ")

            f_index_st = sugang.search_index(logged_in_user)
            if f_index_st == -1:
                print("[ERROR] 학생 ID를 찾을 수 없습니다.")
                continue

            f_index_cls = manage.search_index(cls_code)
            if f_index_cls == -1:
                print(f"[ERROR] {cls_code}: 강의 코드를 찾을 수 없습니다.")
                continue

            course_credits = _cls[f_index_cls][4]
            current_total_credits = _st[f_index_st][7]

            if current_total_credits + course_credits > 18:
                print("수강가능학점을 초과했습니다")
                continue

            if not manage.add_subscription(cls_code):
                # 수강 신청 실패 시 (정원 초과 등)
                continue

            if sugang.add_sugang_list(logged_in_user, cls_code):
                _st[f_index_st][7] += course_credits  # 학생의 총 학점 업데이트
            else:
                # 학생 수강 목록 추가 실패 시 (학생 ID 오류 등)
                # 이미 manage.add_subscription에서 수강자 수를 증가시켰으므로 취소해야 함
                manage.cancel_subscription(cls_code)

        elif choice == "3":
            # 강의 목록 보기
            with cls_lock:
                print("\n=== 강의 목록 ===")
                for cls in _cls:
                    print(f"강의명: {cls[3]}, 코드: {cls[0]}, 현재 신청자 수: {cls[6]}/{cls[5]}")
                print("=================")

        elif choice == "4": 
            print("시스템 종료.")
            stop_auto_increment.set()  # 자동 증가 중지 이벤트 설정
            if auto_thread is not None:
                auto_thread.join()  # 스레드가 종료되길 기다림

            # 종료 시 로그인한 학생의 수강 신청한 과목 출력 및 상태 확인
            if logged_in_user is not None:
                f_index = sugang.search_index(logged_in_user)
                if f_index != -1:
                    sugang_list = _st[f_index][6]  # 학생의 수강신청 리스트
                    print("\n=== 수강 신청한 과목 목록 ===")
                    for cls_code in sugang_list:
                        lecture_name = manage.get_lecture(cls_code)
                        if lecture_name:
                            print(f"강의명: {lecture_name} (코드: {cls_code})")
                    print("=================")

                    # 상태값 계산
                    if set(sugang_list) == set(todo_sugang_list):
                        state = 0
                    elif set(todo_sugang_list).issubset(set(sugang_list)):
                        state = 1
                    else:
                        state = -1

                    # 상태에 따른 메시지 출력
                    if state == 0:
                        print("휴…큰일 날 뻔 했다.. 한학기 더 할 뻔 했는데..")
                        time.sleep(1)
                        print('듣고 싶은 과목이 좀 더 있었는데 아쉽다..졸업엔 영향 없겠지?')
                        time.sleep(1)
                        print('어디보자..양자..역학..열통..졸논.. 전자기.. 학점은 다 채웠고..뭐 빠진 건 없겠지?')
                        time.sleep(1)
                        print('음? 기본교양 3/4..? 설마..??? 맞다 토익!!')
                        time.sleep(1)
                        print('다행이도 다음주에 신청할 수 있군..근데 마지막이네..반드시 성공하여 인생의 장대한 서막을 울리리라')
                        time.sleep(1)
                        print('TOEIC GOGO')
                     
                    pass

                    break

            else:
                print('1번에서 4번까지만 고르셔요~')








# 프로그램 실행
if __name__ == "__main__":
    main()