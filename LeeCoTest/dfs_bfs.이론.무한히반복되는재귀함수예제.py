def recurisve_function():
    print("재귀함수를 호출합니다.")
    recurisve_function()
recurisve_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# : 재귀의 최대 깊이를 초과했다는 내용.