def solution(a, b):
    answer=0
    week=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    end=[31,29,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(a-1):
        answer+=end[i]
        
    answer+=b-1
    answer=week[answer%7]
    
    return answer


#더 나은 풀이
def solution(a, b):
    answer=0
    week=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    end=[31,29,31,30,31,30,31,31,30,31,30,31]
    
	answer=week[(sum(end[:a-1])+b-1)%7]
    
    return answer
