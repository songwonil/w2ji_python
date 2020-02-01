'''
unit 04 기본 그래프 그리기
'''
'''
import matplotlib.pyplot as plt
plt.plot([10, 20, 30, 40])
plt.show()

import matplotlib.pyplot as plt
plt.plot( [1,2,3,4],[12,43,25,15] )
plt.show()
'''
'''
#범례
import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([30, 40, 50, 60] , label='aaa')
plt.plot([50, 50, 50, 50] , label='center')
plt.legend(loc=10)
plt.show()
'''
'''
#색상
import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([30, 40, 50, 60] , label='aaa' , color='skyblue')
plt.plot([50, 50, 50, 50] , label='center' , color='pink')
plt.legend(loc=10)
plt.show()
'''
'''
#그래프 선 모양 바꾸기
import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([30, 40, 50, 60] , label='aaa' , color='skyblue' , linestyle='--')
plt.plot([50, 50, 50, 50] , label='center' , color='pink' , linestyle='-.')
plt.legend(loc=10)
plt.show()
'''
#마커 모양 바꾸기
import matplotlib.pyplot as plt
plt.title('marker')
plt.plot([10, 20, 30, 40], 'r.--', label='circle')  # 빨간색 원형 마커 그래프
# 초록색 삼각형 마커 그래프 => 색상, 마커모양, 선모양 으로 정의된다. = 'g^:'
plt.plot([40, 30, 20, 10], 'g^:', label='triangle up')
plt.legend(loc=10)
plt.show()

