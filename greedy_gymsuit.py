#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 02:48:29 2018

@author: yeoyoung
"""

#문제 설명
#오늘은 체육수업이 있는 날입니다. 그런데 점심시간에 도둑이 들어 몇몇 학생의 체육복이 도난을 당했습니다. 
#다행히 일부 학생들이 여벌의 체육복을 가져왔습니다. 
#학생들의 번호는 체격 순으로 매겨져 있기 때문에 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려주려고 합니다.
#
#예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 당연히 체육복을 2벌 가져온 학생의 체육복이 도난을 당했다면, 여벌의 체육복을 빌려줄 수 없습니다.
#
#체육복이 없으면 체육수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 듣고 싶습니다.
#
#전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
#
#제한사항
#전체 학생의 수는 2명 이상 30명 이하입니다.
#체육복을 도난당한 학생의 수는 2명 이상 n명 이하이고 중복되는 번호는 없습니다.
#여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
#입출력 예
#n	lost	reserve	return
#5	[2, 4]	[1, 3, 5]	5
#5	[2, 4]	[3]	      4
#입출력 예 설명
#예제 #1
#1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.
#
#예제 #2
#3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

모든학생들 다 가져왔따는 가정하에 1씩
한번씩 가져온애들을 2 
잃어버린애ㄴ들은 0
앞에서부터 내가 2일때 오른쪽이 0이면 하나 줌
뒤에서부터 내가 2일때 왼쪽에 0 하나줌
두번한게 1이상인것 

n=5
lost=[2,4]
reserve=[1,3,5]
def solution(n, lost, reserve):
    answer=0
    total=[i for i in range(1,n+1)]
    lostarr=[1 for i in range(1,n+1)]
    reservearr=[0 for i in range(1,n+1)]
        
   #있나 확인
    for lo in lost:
        if lo in total:
            lostarr[lo-1]=0
   
    for re in reserve:
        if re in total:
            reservearr[re-1]=1

    #본인,앞,뒤 인덱스 확인 후 lost에 0이 있는 부분이 있으면 lost배열 +1로 바꿔줌 (왼쪽 ㅈ먼저 )
    for i in range(n):
        for j in range(i-1,i+2):
            if j==-1:continue

            if n>j: break
            if reservearr[i]==1 and lostarr[j]==0:
                lostarr[j]==1
                continue
       
       

    answer=sum(lostarr)
    return answer
        
                
                
                
                lost[i-1]lost[i]lost[i+1]
                
            
1 2 3 4 5

1 0 1 0 1 lost j
1 0 1 0 1 reserve i           
            
    
모든학생들 다 가져왔따는 가정하에 1씩
한번씩 가져온애들을 2 
잃어버린애ㄴ들은 0
앞에서부터 내가 2일때 오른쪽이 0이면 하나 줌
뒤에서부터 내가 2일때 왼쪽에 0 하나줌
두번한게 1이상인것 
    
    
    #한칸씩 왼쪽이동 오른쪽이동 (열별 1의 개수 합, 2인건 1로 바꾸)
    #왼쪽이동(reservearr 앞에 0 추가, 뒤에 지움)
    reservearr.insert(0,0)
    del reservearr[n]
    
    for i in range(n):
        _sum.append(lostarr[i]+reservearr[i])
        if _sum[i]==2:
            _sum[i]=1
            
    left=sum(_sum) 
    
    #오른쪽이동(reservearr 뒤에 0 추가, 앞에 지움)
    reservearr.insert(n,0)
    del reservearr[0]
    
    for i in range(n):
    
    #둘중에 큰거
            
        
            
    
    
    return answer

if 하나뺀게 붙어있으면
전체-(lost-reserve)
1 2 3 4 5

1 0 1 0 1 lost j
1 0 1 0 1 reserve i


1 0 1 0 1 lost
0 1 0 1 0 reserve

1 0 1 0 1 lost 
0 0 1 0 0 reserve

1 0 0 0 1 lost
1 0 0 1 1 reserve
