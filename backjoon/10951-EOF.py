while True:
  try:
    A, B = map(int, input().split())
    print(A + B)
  except:
    break


# EOF(End of File)란 데이터 소스로부터 더 이상 읽을 수 있는 데이터가 없음을 나타낸다.
# 파이썬에서는 예외가 발생할 때 처리할 수 있는 기능이 있다.
# try, except, else, finally
# try에는 기본적으로 실행할 수 있는 코드를 넣고 except에는 예외가 발생했을 경우 시행할 코드를 작성한다.
# else절은 예외가 발생하지 않아 except 절을 실행하지 않았을 경우 실행되는 절이다.
# finally 절은 try 절에서 예외의 발생여부에 관계없이 항상 실행되는 절이다.