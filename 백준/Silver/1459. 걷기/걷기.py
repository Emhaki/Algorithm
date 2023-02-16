import sys
input = sys.stdin.readline
def solution(x,y,w,s):
    if s <= w: # 대각선 시간이 일직선 시간보다 작거나 같을 경우
        min_value = min(x,y)
        if abs(x-y) % 2 == 0: # 도착지점이 짝수위치라면
            result = ((min_value) * s) + (abs(x-y) * s)
        else: # 대각선으로 이동 후 일직선으로 이동
            result = ((min_value) * s) + ((abs(x-y)-1) * s) + w
    elif s > w * 2: # 대각선으로 가는 방법이 일직선보다 무조건적으로 비용이 클 경우
        result = (x+y) * w
    else:
        min_value = min(x,y)
        result = ((min_value) * s) + (abs(x-y) * w)
    
    return result

if __name__ == "__main__":
    x, y, w, s = map(int, input().split())
    print(solution(x,y,w,s))