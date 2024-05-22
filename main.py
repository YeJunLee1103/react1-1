# string_a = input("입력A> ")
# int_a = int(string_a)

# string_b = input("입력B> ")
# int_b = int(string_b)

# print("문자열 자료:", string_a + string_b)
# print("숫자 자료:", int_a + int_b)




# number = input("점수 입력> ")
# number = int(number)

# if number > 0:
#     print("양수입니다.")

# if number < 0:
#     print("음수입니다.")

# if number == 0:
#     print("0입니다.")        
    

import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

