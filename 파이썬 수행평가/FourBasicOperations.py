import random as r # 문제 출제
import time as t # 푸는 타임 리미트
import json as j # 파일
import os # 파일
from playsound import playsound # 맞출때, 못 맞출 때 소리 내기
import pygame

class FourBasicOperations:
    def __init__(self):
        self.scores_file = "game_scores.json"
        self.scores = self.load_scores()
        self.difficulty = None
        self.username = None
        self.count = 0
        self.time_limit = 300  # Default time
        self.range_limit = 30  # Default range

    def load_scores(self): # 파일 읽기
        if os.path.exists(self.scores_file):
            with open(self.scores_file, "r", encoding="utf-8") as f:
                return j.load(f)
        else:
            return {}

    def save_scores(self): # 파일 쓰기
        with open(self.scores_file, "w", encoding="utf-8") as f:
            j.dump(self.scores, f, ensure_ascii=False, indent=4)

    def record_score(self, username, difficulty, title): # 난이도, 칭호
        self.scores[username] = {"difficulty": difficulty, "title": title}
        self.save_scores()

    def give_title(self, score): # 맞춘 갯수에 따른 칭호
        if 1 <= score <= 5:
            return "초보자"
        elif 6 <= score <= 10:
            return "중급자"
        elif 11 <= score <= 15:
            return "고급자"
        elif 16 <= score <= 20:
            return "달인"
        elif 21 <= score <= 25:
            return "명인"
        elif 26 <= score <= 29:
            return "전설"
        elif score == 30:
            return "봉봉"
        else:
            return "바보"

    def title_order(self): # 칭호 순위
        return ["봉봉", "전설", "명인", "달인", "고급자", "중급자", "초보자", "바보"]

    def show_rankings(self): # 랭킹 보여주기
        order = self.title_order()
        print("\n======= 🏆 랭킹 🏆 =======")
        sorted_scores = []
        for username, info in self.scores.items():
            title = info["title"]
            difficulty = info["difficulty"]
            index = order.index(title) if title in order else len(order)
            sorted_scores.append((username, difficulty, title, index))

        sorted_scores.sort(key=lambda x: x[3])

        # 각 난이도, 칭호에 따른 색상 부여
        color_map_difficulty = {
            "Easy": "\033[32m",     # 초록색
            "Normal": "\033[33m",   # 노랑색
            "Hard": "\033[38;5;208m",  # 주황색
            "Expert": "\033[31m",   # 빨강색
            }
        title_color = "\033[34m"   # 칭호 : 파랑색
        reset = "\033[0m"

        for idx, (username, difficulty, title, _) in enumerate(sorted_scores, start=1):
            difficulty_color = color_map_difficulty.get(difficulty, "\033[37m")  # 기본값 흰색
            print(f"{idx}. [ {difficulty_color}{difficulty}{reset} ] [ {title_color}{title}{reset}] {username}")
        print("==========================\n")

    def reset_scores(self): # 랭킹 초기화
        confirm = input("정말 모든 랭킹을 초기화하시겠습니까? (Y/N): ")
        if confirm.strip().upper() == "Y":
            self.scores = {}
            self.save_scores()
            print("랭킹이 초기화되었습니다.\n")
        else:
            print("초기화를 취소했습니다.\n")

    def delete_user_score(self, username): # 특정 사용자 제거
        if username in self.scores:
            del self.scores[username]
            self.save_scores()
            print(f"{username}님의 랭킹 기록이 삭제되었습니다.\n")
        else:
            print(f"{username}님의 기록이 존재하지 않습니다.\n")

    def settings_menu(self): # 메뉴
        while True:
            print("\n=== 설정 메뉴 ===")
            print("1. 랭킹 보기")
            print("2. 랭킹 초기화")
            print("3. 특정 사용자 삭제")
            print("4. 뒤로가기")
            choice = input("원하는 번호를 입력하세요 : ")

            if choice == "1":
                self.show_rankings()
            elif choice == "2":
                self.reset_scores()
            elif choice == "3":
                name = input("삭제할 사용자 이름을 입력하세요 : ")
                self.delete_user_score(name)
            elif choice == "4":
                print("메인으로 돌아갑니다.\n")
                break
            else:
                print("올바른 번호를 입력해주세요.")

    def start_Game(self): # 게임 시작
        FBO.play_bgm("MP3/BGM.mp3")
        print("??? : 안녕하세요! ??? 스테이션에 오신걸 환영합니다")
        t.sleep(2)
        self.username = input("??? : 먼저.. 사용자님의 이름을 입력해주세요! : ")
        print(f"좋습니다 {self.username}님.. 환영합니다!")
        t.sleep(1)

        while True:
            print("\n??? : 난이도를 선택해주세요:")
            t.sleep(0.5)
            print("1. Easy\n2. Normal\n3. Hard\n4. Expert")
            t.sleep(1.5)
            d = input("번호를 입력하세요: ")
            if d == "1":
                self.difficulty = "Easy"
                self.time_limit = 360
                self.range_limit = 20
                break
            elif d == "2":
                self.difficulty = "Normal"
                self.time_limit = 300
                self.range_limit = 30
                break
            elif d == "3":
                self.difficulty = "Hard"
                self.time_limit = 240
                self.range_limit = 40
                break
            elif d == "4":
                self.difficulty = "Expert"
                self.time_limit = 180
                self.range_limit = 50
                break
            else:
                print("올바른 번호를 입력해주세요.")

        while True:
            n = input("??? : ..준비가 되셨나요? (Y / N / 설정) : ")
            if n.upper() == "Y":
                print("??? : 좋습니다! 게임을 10초 후 시작합니다.")
                return True
            elif n.upper() == "N":
                print("??? : 아쉽군요.. 준비가 되면 다시 돌아오세요!")
                return False
            elif n == "설정":
                self.settings_menu()
            else:
                print("??? : Y / N / 설정 중에서만 골라주세요!")

    def explain_Game(self): # 게임 룰 설명
        print("??? : 본격적인 게임을 시작하기 전 안내사항을 전달하겠습니다!")
        t.sleep(1.5)
        print("??? : 사칙연산 문제 30개를 제한시간 내에 풀어야 합니다!")
        t.sleep(1.5)
        print(f"??? : 난이도: {self.difficulty}, 제한시간: {self.time_limit // 60}분")
        t.sleep(1.5)
        print("??? : 나눗셈 문제는 소수 둘째 자리까지 반올림하여 입력해주세요.")
        t.sleep(1.5)
        while True:
            n = input(f"??? : ..{self.username}님 게임을 시작하시겠습니까? (Y / N / 설정) : ")
            if n.upper() == "Y":
                print("??? : 좋습니다! 게임을 10초 후 시작합니다.")
                return True
            elif n.upper() == "N":
                print("??? : 아쉽군요.. 준비가 되면 다시 돌아오세요!")
                return False
            elif n == "설정":
                self.settings_menu()
            else:
                print("??? : Y / N / 설정 중에서만 골라주세요!")

    def create_list(self): # 숫자, 사직연산 만들기
        return list(range(-self.range_limit, self.range_limit + 1)), ['+', '-', '*', '/'], list(range(-self.range_limit, self.range_limit + 1))

    def extraction(self): # 수 뽑기
        first_num, signs, second_num = self.create_list()
        f_n = r.choice(first_num)
        Sign = r.choice(signs)
        if Sign == '/':
            s_n = r.randint(1, 10)
        else:
            s_n = r.choice(second_num)
        return f_n, Sign, s_n

    def Main_Game(self): # 메인 게임 기능
        self.count = 0
        start_time = t.time()

        for i in range(30):
            if t.time() - start_time > self.time_limit:
                print("제한 시간이 지나 게임을 종료합니다!")
                break

            f_n, Sign, s_n = self.extraction()
            print(f'{f_n} {Sign} {s_n} = ???')

            if Sign == '/' and s_n == 0:
                print("0으로 나눌 수 없어 문제 스킵!")
                continue

            try:
                answer = eval(f"{f_n}{Sign}{s_n}")
                if Sign == '/':
                    answer = round(answer, 2)
                user_input = float(input("Answer : "))
            except:
                print("숫자로 입력해주세요!")
                continue

            if abs(user_input - answer) < 0.01:
                self.count += 1
                print("Right!")
                playsound("./MP3/correct-6033.mp3")
            else:
                print(f"Wrong! 정답은 {answer}입니다.")
                playsound("MP3/buzzer2-6109.mp3")

        FBO.stop_bgm()
        FBO.play_bgm("MP3/Congratulation.mp3")

        print("게임이 종료되었습니다..")
        t.sleep(1.5)
        print(f"{self.username}님이 맞춘 갯수는...? {self.count}개 입니다~~")
        t.sleep(1.5)
        title = self.give_title(self.count)
        print("사용자님께 지급될 칭호는....?")
        t.sleep(1)
        print(f'\033[33m{title}\033[0m 입니다!')
        self.record_score(self.username, self.difficulty, title)

    def play_bgm(self, file, loop=-1): # bgm출력
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(loop)

    def stop_bgm(self): # bgm 중지 ( 리셋 용 )
        pygame.mixer.music.stop()


    def close_Game(self):
        print("프로그램 종료 중...")
        t.sleep(3)
        print("프로그램을 종료합니다.")     

# Main
FBO = FourBasicOperations()
a = None
isTrue = FBO.start_Game()
if isTrue:
    t.sleep(10)
    a = FBO.explain_Game()
    if a:
        t.sleep(5)
        FBO.Main_Game()
    else:
        t.sleep(5)
        FBO.close_Game()
else:
    t.sleep(3)
    FBO.close_Game()