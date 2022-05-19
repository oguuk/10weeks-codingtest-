# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#데이터 N, M, S을 입력받는다
n, m, s = map(int, input().split())

#공백으로 구분된 N개의 정수(사람들의 키)를 입력받는다
data = map(int, input().split())

#사람들의 수를 셀 변수 count를 0으로 초기화한다

#[BEGIN ]
#count 변수에 정답(조사해야 할 사람의 수)이 저장되도록 코드를 작성해보자


#[END]


print(sum([1 for height in data if height == m or height == s]))
