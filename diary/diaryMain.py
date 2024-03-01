# from apps.diary.diaries import Diaries
# from apps.diary.diaryClass import Diary
# from apps.diary.diayNotFoundException import DiaryNotFoundError
# from apps.diary.invalidCommandException import InvalidCommandException
#
#
# class DiaryMain:
#     def __init__(self):
#         self.diaries = Diaries
#         self.diary = Diary
#
#     def validate(self, anything: str):
#         if len(anything) == 0:
#             raise InvalidCommandException
#         pass
#
#     def home_page(self):
#         choice: int = int(input("""
#         1. Create Dairy
#         2. Find Diary by username
#         3. Delete Diary
#         4. Exit
#         """))
#         return choice
#
#     def create_diary(self):
#         name = input("Enter your preferred username: ")
#         self.validate(name)
#         password = input("Enter your password: ")
#         self.validate(password)
#         self.diaries.addDiary(name, password)
#         print("Diary created Succesfully.")
#         self.home_page()
#
#     def find_by_username(self):
#         try:
#             user_name: str = input("find username: ")
#             self.validate(user_name)
#             diary_found = self.diaries.findByUserName(user_name)
#         except DiaryNotFoundError:
#             print("Diary not found")
#         finally:
#             self.home_page()
#
#     def home_page1(self, choice: int):
#         match choice:
#             case 1:
#                 self.create_diary()
#             case 2:
#                 self.find_by_username()
#             case 3:
#                 self.