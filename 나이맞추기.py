birth_year=int(input("당신이 태어난 연도를 입력하세요.")) #하..미친 input은 print를 쓰지않아도 반환을 하기때문에 불필요하고, input의 반환값은 None이라는것을 알게됨..
age=2023-birth_year+1                                        

if 20<=age<=26:
    print("대학생")
elif 17<=age<20:
    print("고등학생")
elif 14<=age<17:
    print("중학생")
elif 8<=age<14:
    print("초등학생")
else:
    print("학생이 아닙니다.")