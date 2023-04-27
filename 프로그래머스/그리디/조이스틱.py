def solution(name):
    chr = 'A'
    name_list = list(name)
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_list = list(alph)
    cnt = 0
    for i in name_list:
        # chr에서의 index - i에서의 인덱스 < 0이면 A<J
        if alph.index(chr) - alph.index(i) < 0:
            # i - chr 인덱스 < 13 이면
            if alph.index(i) - alph.index(chr) < 13:
                # cnt += i - chr 인덱스 + 1
                cnt += alph.index(i) - alph.index(chr) + 1
            # i - chr 인덱스 > 13 이면
            elif alph.index(i) - alph.index(chr) > 13:
                # 맨 뒤 인덱스로 이동
                chr = alph[-1]
                # 맨 뒤 인덱스 - i 인덱스 + 1
                cnt += alph.index(chr) - alph.index(i) + 1
            # chr = i
        # chr에서의 index - i에서의 인덱스 > 0이면 Z > B
        if alph.index(chr) - alph.index(i) > 0:
            # chr 인덱스 - i 인덱스 < 13 이면
            if alph.index(chr) - alph.index(i) < 13:
                # cnt += chr 인덱스 - i+ 1
                cnt += alph.index(chr) - alph.index(i) + 1
            # chr 인덱스 - i 인덱스 > 13 이면
            elif alph.index(chr) - alph.index(i) < 13:
                # 맨 앞 인덱스로 이동
                chr = alph[0]
                # i 인덱스 - 맨 앞 인덱스 + 1
                cnt += alph.index(i) - alph.index(chr) + 1
            # chr = i
        
    return cnt