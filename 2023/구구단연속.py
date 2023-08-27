i=1
while i<10:
        print("구구단 몇 단을 계산할까?(1~9), (프로그램 종료: 0)")
        n=int(input())

        if n==0:
            print("프로그램 종료")
            break
        elif n<0 or n >9:
             print("주어진 범위를 확인하세요.")
            #continue의역할: 현재루프의 나머지를 건너뛰고 다시 반복을 시작하게됨 따라서 continue를 for뒤에 와야하는게 맞음(다음부터 어딘가에쓰일때)
            
        else:
            for i in range(1, 10):
               print(n,"x",i,"=",n*i)

#나는 늘 for문을 맨 앞에 두고 while을 중간에 두려는 방법으로 시도하고 실패함 그리고 i=1로 지정하고 while i<10도 좋지만 아예 while True도 시작해도 있어보일듯?ㅎ