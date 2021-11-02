import pymysql
import matplotlib.pyplot as plt
import numpy as np

conn = pymysql.connect(
    host='',
    port=, # mysql포트
    user='',  # 접속 계정
    password='', # 루트계정 본인 비번
    db='',  # 접속하려는 데이터베이스 명
    charset='utf8'
)

# Step3 - 커서(cursor) 객체 생성
# 커서는 SQL문을 실행하거나, 결과를 돌려받는 통로이다.
# 객체명 = 연결객체(conn).cursor()
cursor = conn.cursor()

# Step4 - sql 명령을 실행
# 커서(cursor)객체.execute(sql명령문)
cursor.execute('select ~~ 쿼리문 입력 ')
## sva_meta.pose  -> (len, 1, frame_num     ) size tuple  return!
# Step5 - sql 실행 결과 저장
result = cursor.fetchall()
#result = np.array(result)
# 0,1,2,3 index -> 2~6 / 7 / 8~11 / 12~14
# 데이타베이스 종료
conn.close()

# 5만개 영상을 갖고와서 result에 fetchall하면,  len(result) = 50000
# len(result[0]) = 1 ==> 왜? : result는 1개의 str을 담고있는 tuple을 5만개 담고있는 큰 하나의 tuple
# len(result[0][0]) ==> 427 과 같이 나옴 ( 그str의 길이 )

temp = []
video_num = len(result)
###### 2~6 / 7 / 8~11 / 12~14 를 각 영상이 몇개씩 갖고있는지 저장해주는 배열 tong_result ==> 영상갯수 * 4 의 2차원 np.array #########

tong_result = np.zeros((video_num,4)).astype('int16')
# 각 영상 별 2~6 / 7 / 8~11 / 12~14 가 몇개 씩 있는지 조사하는 곳 - index찾는 것으로 훨씬 빠르게 할 수 있다.
for i in range(len(result)):
    temp = result[i][0].split(',')
    # 맨 앞, 맨 뒤 대괄호 지워주는 과정
    temp[0] = temp[0][1:]
    temp[-1] = temp[-1][:-1]
    temp = list(map(int, temp))
    # swing pose number가 담긴 list이다 (temp)
    for j in range(len(temp)):
        if temp[j] < 2 :
            continue
        elif temp[j] > 14:
            break
        elif 2 <= temp[j] <= 6:
            tong_result[i][0] += 1
        elif temp[j] == 7:
            tong_result[i][1] += 1
        elif 7 < temp[j] < 12:
            tong_result[i][2] += 1
        else:
            tong_result[i][3] += 1


what = ['2~6','7', '8~11','12~14']
for i in range(4):
    fig, ax = plt.subplots()
    plt.hist(tong_result[:,i], bins = range(np.min(tong_result[:,i]),np.max(tong_result[:,i]),1),  histtype = 'stepfilled', color = 'blue')

    plt.title( 'motion_range = ' + what[i] )
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    # 앞에 두 숫자가 위치의 비율이다!!
    plt.text(0.73,0.95, 'mean='+str(np.mean(tong_result[:,i]))[:8] +'\n'+'std=' + str(np.std(tong_result[:, i]))[:8]+'\n'+'vnum=' + str(video_num), transform=ax.transAxes,fontsize = 10,verticalalignment='top', bbox=props)
    plt.show()




