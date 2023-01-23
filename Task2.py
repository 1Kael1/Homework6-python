# состоит ли число из одинаковых цифр

def sameDigits(numArr):

   # print(numArr)

   for i, el in enumerate(numArr):

       if el !=numArr[len(numArr)-1]:
           print('NO')
           break
   else:
       print('YES')


numArr = list(map(int, input()) ) # преобразование на лету в массив
sameDigits(numArr)