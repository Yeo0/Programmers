#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:10:48 2018

@author: yeoyoung
"""

#0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
#예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
#0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#

#제한 사항
#numbers의 길이는 1 이상 100,000 이하입니다.
#numbers의 원소는 0 이상 1,000 이하입니다.
#정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

#입출력 예
#numbers    return
#[6, 10, 2] 6210
#[3, 30, 34, 5, 9]  9534330


#정수를 이어 붙여 만들수 있는 가장 큰수


##정렬알고리즘
#6 10 2 정렬 하는 모든 경우의 수 구함 -> 리스트에 어팬드
#그중 최대값 구함



def solution(numbers):
    answer = ''
    kv_array = []
    
    largest=len(new_numbers[0])
    for list in new_numbers:
        if len(list)>largest:
            largest=len(list)
    
    for number in numbers:
        kv_array.append((str(number), str(number).ljust(largest, str(number)[0])))
    
    #value크기순으로 딕셔너리 정렬
    sort_=sorted(kv_array, key=lambda kv_array: kv_array[0] , reverse=True)
    sort_=sorted(sort_, key=lambda kv_array: kv_array[1] , reverse=True)
    
    #key순서대로 리턴
    for i in range(len(sort_)):
        answer = answer + sort_[i][0]

    return answer