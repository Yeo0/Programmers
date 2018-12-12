#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:53:49 2018

@author: yeoyoung
"""

#문제 설명
#네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
#컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
#제한사항
#컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
#각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
#i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
#computer[i][i]는 항상 1입니다.
#입출력 예
#n	computers	return
#3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
#3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1



n=6
computers=[[1,0,1,0,0,1],[0,1,0,0,1,0],[1,0,1,1,0,1],[0,0,1,1,0,0],[0,1,0,0,1,0],[1,0,1,0,0,1]]
def solution(n, computers):
    answer = 1
    i=0 #row
    j=0 #col
    visited=[]
    
    #처음꺼 들어가있는 상태
    for j in range(n):
        if computers[0][j]==1:
            visited.append((i,j))
            answer+=1
            
    for i in range(1,n): #행기준
        for j in range(n-i,n): #열 하나씩
            if computers[i][j]==1:
                
                #처음 방문했으면 (튜플 앞이나 뒤중 하나라도 안ㅜ똑같다면)
                for vis in visited:
                     if vis[0]!=i or vis[0]!=j or vis[1]!=i or vis[1]!=j:
                         answer+=1 #처음일때만 카운트
                     visited.append((i,j)) #처음이든 아니든 다 넣어줌
    return answer
solution(3,computers)
#--
def solution(n, computers):
    answer = 1
    i=0 #row
    j=0 #col
    k=0 #visited index
    visited=[]

    for i in range(n): #행기준
        row_visit=[]
        for j in range(i,n): #열 하나씩
            if computers[i][j]==1:
                row_visit.append(j)
        if row_visit!=[]:
            visited.append(set(row_visit))
            
    finding(visited,0)
    
def dfs(numbers, target, n):
    if n==len(numbers):
        sum = 0
        for number in numbers:
            sum += number
        if sum == target:
            answer+=1
            return
    else:
        numbers[n] = numbers[n]*1
        dfs(numbers, target, n+1)
        numbers[n] = numbers[n]*(-1)
        dfs(numbers, target, n+1)
    
    
    
    
    
    
def finding(list,index):
    for i in range(len(index)):
        if not list[i].isdisjoint(list[index]):#공통원소를 안가지면
            answer+=1
            flag+=1
            f'list{flag}'=list[index]
            f'list{flag+1}'=list[index+1]
        
    else: #공통원소를 가지면 
        f'list{flag}'=list
        
        
def finding(list,index):
    if not        
    
    
    
    
    
    
    newset=visited[0]
    for k in range(len(visited)):
        if not newset.isdisjoint(visited[k+1]): #공통원소를 안가지면 
            answer+=1
            new_setvisited[k]
        else:
            newset=newset.union(visited[k+1])
            
    

                f'list{i}'=[]
                list.append(i)
            else:
                f'list{i+1}'.append(i)

#---

computer[][i]

a=[1,2,3,4]
a[1],a[3]









----

def solution2(n,computers):
    dfs(computers,[],0,0,0)
    answer=count
    return answer

def dfs(computer,visited,count,i,j):
    if computer[i][j]==1:
        if (i,j) not in visited:
            visited.append((i,j))
            count+=1
    dfs(computer,visited,count,i+1,j)
    dfs(computer,visited,count,i,j+1)
   
    if i==len(computer) and j==len(computer):
        return
    
solution2(3,computers)
        
#---
def solution3(n,computers):
    ans=[]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                ans.append((i,j))
computers
 visited = [[0] * n for i in range(n)]
 

#----
def solution4(n,computers):
    
    for i in range(n):
        for j in range(n):
            if computers
arr=[]
arr.append[0]
def search(n,computers)  
    for i in range(n):
        for j in range(n):
            if computers[i][n-j]==1:
                f'list{i}'=[]
                list.append(i)
            else:
                f'list{i+1}'.append(i)


l
f'grid{i}{j}'


---
ㅇ



   
def bfs(ans,):
    computers
    arr=[]
    arr.append([0])
    visited[0][0]=1
    while arr:
        current=arr.pop(0)
        if computers[1][0]==1:
            l
            
            
        if cu                
        x=current[0]
        y=current[1]
        if current==[row-1,col-1]:
            
    
    map = [""] * m
visit = [[0] * n for _ in range(m)]

for i in range(m):
map[i] = input()
    
num
    
    
def bfs





#---
map = [""] * m
visit = [[0] * n for _ in range(m)]

for i in range(m):
map[i] = input()

def bfs():
    arr = []
    arr.append([0, 0])
    visit[0][0] = 1
    while arr:
        cur = arr.pop(0)
        x = cur[0]
        y = cur[1]
        if cur == [row - 1, col - 1]:
            print(visit[x][y])
        break
    now = visit[x][y]

    for i in range(4):
        wx = x + dir[i][0]
        wy = y + dir[i][1]
        if wx >= m or wy >= n or wx < 0 or wy < 0:
            continue
        if visit[wx][wy] == 0 and map[wx][wy] == '1':
            visit[wx][wy] = now + 1
            arr.append([wx, wy])






-----

def dfs(numbers, target, n): #n 인덱스
    if n==len(numbers):
        sum = 0
        for number in numbers:
            sum += number
        if sum == target:
            answer+=1
            return
    else:
        numbers[n] = numbers[n]*1
        dfs(numbers, target, n+1)
        numbers[n] = numbers[n]*(-1)
        dfs(numbers, target, n+1)









def dfs(grap,x,y):
    visited=[]
    stack=graph[0][0]
    while stack:
        data=stack.pop()
        if data not in visited:
            if data==1:
                count+=1
        stack+=graph[da]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            
    return visited






computers[0][0]=1
len(computers)


n,e,v=input().split()
n=int(n);e=int(e);v=int(v)
N=[[0 for x in range(computers)]for y in range(computers)]
visit=[ 0 for x in range(computers) ]
for i in range(computers):
    N[i][j]=N[j][i]=1
    
def dfs(i):
    print(i)
    visit[i]=1
    j=1
    while j < n:
        if N[i][j] == 1 and visit[j]==0 :
            dfs(j)
        j=j+1
dfs(v)