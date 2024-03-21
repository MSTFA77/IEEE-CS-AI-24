if __name__ == '__main__':
    n = int(input())  
    scores = list(map(int, input().split()))  
    unique_scores = sorted(set(scores), reverse=True)
    if len(unique_scores) >= 2:
        runner_up_score = unique_scores[1]
        print(runner_up_score)
    else:
        print("No runner-up score exists.")
