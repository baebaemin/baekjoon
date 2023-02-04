"""
블랙잭 룰: N장의 카드를 받아 3장을 뽑는다.
딜러가 외치는 숫자 M을 넘지 않으면서 M과 최대한 가깝게 만든다.
"""


def black_jack():
    N, M = map(int, input().split())
    min_num = M  # 3장의 합과 M과의 차이값 중 최소인 수를 저장할 예정
    card_lst = sorted(list(map(int, input().split())))
    rlt = 0

    for i in range(N - 2):
        card1 = card_lst[i]
        for card2 in card_lst[i+1:-1]:
            for card3 in card_lst[i+2:]:
                sum_card = card1 + card2 + card3
                if sum_card == M:  # 3장의 합이 M과 같으면 리턴, 종료
                    return sum_card
                if sum_card < M and M - sum_card < min_num:  # 3장의 합이 M보다 작을 때, M과 제일 가까운 수를 저장
                    min_num = M - sum_card  # 3장의 합과 M과의 차이값 중 최소인 수를 업데이트
                    rlt = sum_card  # 업데이트 될 때 덱에 세 장의 합을 저장
    else: 
        return rlt


print(black_jack())