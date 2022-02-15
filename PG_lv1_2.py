def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    if len(arr) == 0:
        arr.append(-1)
    return arr

if __name__ == "__main__":
    arr = [10]
    print(solution(arr))
