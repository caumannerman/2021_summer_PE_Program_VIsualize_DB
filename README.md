# 2021_summer_PE_Program_VIsualize_DB
이 프로그램은 resnet50모델로 추출해낸 연속 이미지들의 관절 Keypoint들을 =>  Bi-Directional LSTM 모델을 거쳐 나온 골프 구분동작이 DB에 저장되어 있을 때, 쿼리에 입력한 조건들을 만족하는 이미지을 구분동작 구간별로 나누어 시각화하는 프로그램이다. 
아래오 같이 지정한 구분동작 구간별로 4개의 히스토그램이 각각의 평균, 표준편차와 함께 나타나도로 하였다.

<img width="709" alt="스크린샷 2021-11-02 오후 11 58 40" src="https://user-images.githubusercontent.com/75043852/139872557-4b094c10-6060-4a07-ac87-fc80c1ffa079.png">
