import requests
import datetime
import json
import telegram

now = datetime.datetime.now()
today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
data = today.strftime('%Y-%m-%d')
result = ['***오늘 {day}의 환율입니다.***\n주말 혹은 당일 정보 업데이트가 되지 않으면 전일(주말의 경우 금요일)의 정보가 표시됩니다.\n'.format(day=today)]
cur_list = {'AED': 0, 'AUD': 1, 'BHD': 2, 'CAD': 3, 'CHF': 4, 'CNH': 5, 'DKK': 6, 'EUR': 7, 'GBP': 8, 'HKD': 9,
            'IDR': 10, 'JPY': 11, 'KRW': 12, 'KWD': 13, 'MYR': 14, 'NOK': 15, 'NZD': 16, 'SAR': 17, 'SEK': 18,
            'SGD': 19, 'THB': 20, 'USD': 21}

currency = ('USD', 'CNH', 'JPY', 'EUR')

my_token = '1177997136:AAHQVOxzfK8c73e93cVsSVrmv1MbKAiZqrw'  # botfather로 받은 토큰
chatbot = telegram.Bot(token=my_token)
#chat_id = 1260390472 # 챗봇 chat_id
chat_id = -1001396381643 # 공개채널 chat_id
#https://api.telegram.org/bot1177997136:AAHQVOxzfK8c73e93cVsSVrmv1MbKAiZqrw/getUpdates
#https://api.telegram.org/bot1177997136:AAHQVOxzfK8c73e93cVsSVrmv1MbKAiZqrw/sendMessage?chat_id=@asffgh5678&text=123
#https://api.telegram.org/bot1177997136:AAHQVOxzfK8c73e93cVsSVrmv1MbKAiZqrw/sendMessage?chat_id=@channelName&text=123

def api_set(day):
    date = day.strftime('%Y-%m-%d')
    api_key = 'wySRP0gWD8lLdxxG5nlX8Ws0gehXbPOR'
    api = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={key}&searchdate={date}&data={data}'.format(
        key=api_key, date=date, data='AP01')
    req = requests.get(api)
    get_data = req.text
    currency_json = json.loads(get_data)

    return currency_json


if not api_set(today):
    raw = api_set(yesterday)
    print(raw)
else:
    raw = api_set(today)

for curr in currency:
    num = cur_list[curr]
    data = (raw[num]['cur_nm'], raw[num]['cur_unit'], raw[num]['deal_bas_r'])
    draft = '현재 {cur_name}({cur_unit})의 기준환율은 {currency}원입니다.'.format(cur_name=data[0], cur_unit=data[1],currency=data[2])
    result.append(draft)
    

text = "\n".join(result)
print(text)

chatbot.sendMessage(chat_id=chat_id, text=text)