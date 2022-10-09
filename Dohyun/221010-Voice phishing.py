import time
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    computeLPS(pat, lps)

    i = 0 
    j = 0 
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
       
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            print(f"Found {pat} at index " + str(i-j))
            j = lps[j-1]

def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

txt1 = '네 안녕하십니까 혹시 홍길동 씨 핸드폰 맞습니까 본인 앞으로 몇 가지 확인사항 때문에 전화 드렸습니다'
txt2 = '두 계좌에 대해서 아시는 지 전화를 드린 겁니다 메모 가능 하신 거죠 사건 번호하고 제 성함하고 말씀 드릴겁니다'
txt3 = '알겠습니다 저희가 본인 앞으로 피해자 입증 확인서도 보내드릴 겁니다 그걸 가지고 해당 구청 일 층에 가시면은 민원 보상 과라고 있습니다 백 이십만원 개인 정보 유출로 인해서 피해 보상금을 받을 수도 있는 겁니다 본인께서 직접 통장 개설하시지 않으셨지 않습니까'
txt4 = '네 수고하십니다 여기는 서울중앙지검검찰청입니다 혹시 김민수라는 분을 아십니까 지난주에 김민수 일당의 검거 현장에 다량의 신용카드와 대포통장을 압수했습니다 그중에 본인의 명의로 된 농협은행과 신한은행 통장을'
patterns = ['서울중앙지검', '불법거래', '통장', '도용', '보상']
txts = [txt1, txt2, txt3, txt4]
for txt in txts :
    for pat in patterns :
        print(f"--txt : {txt}--")
        start = time.time()
        KMPSearch(pat, txt)
        end = time.time()
        print("소요시간 : ", end-start)

# This code is contributed by Bhavya Jain