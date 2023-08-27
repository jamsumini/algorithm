print("키와 몸무게를 입력하면 체질량지수를 계산합니다.")
height=int(input("키(cm): "))
weight=int(input("몸무게(kg): "))


BMI=weight/((height/100)**2)
rounded_BMI=round(BMI, 2)   #round함수는 괄호 안에 2개의 인자를 받고 (반올림하고싶은거, 소수 몇째자리)를 의미함.
print("*체질량지수:", rounded_BMI)

if BMI>=30:
    print("*고도 비만")
elif 25<=BMI<30:
    print("*비만")
elif 23<=BMI<25:
    print("*과체중")
elif 18.5<=BMI<23:
    print("*정상")
elif BMI<18.5:
    print("*저체중")
else:
    print("다시 입력하세요.")