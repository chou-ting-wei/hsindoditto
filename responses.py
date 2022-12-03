import random
import datetime

tar1 = {'event':'第四次模考', 'year':2022, 'month':12, 'day':14}
tar2 = {'event':'微積分小考', 'year':2022, 'month':12, 'day':19}
tar3 = {'event':'期末考', 'year':2022, 'month':12, 'day':29}
tar4 = {'event':'微積分期末考', 'year':2023, 'month':1, 'day':6}
tar5 = {'event':'112 學科能力測驗', 'year':2023, 'month':1, 'day':13}
tar6 = {'event':'結業式', 'year':2023, 'month':1, 'day':19}
tar7 = {'event':'高中最後一次開學', 'year':2023, 'month':2, 'day':13}
tar8 = {'event':'畢業旅行', 'year':2023, 'month':2, 'day':15}

countdown_list = [tar1, tar2, tar3, tar4, tar5, tar6, tar7, tar8]

def handle_response(message) -> str:
    now_message = message.lower()
    
    if now_message == 'ping':
        return 'pong'
    
    if now_message == 'roll':
        return str(random.randint(1, 6))
    
    if now_message == 'countdown':
        today = datetime.date.today()
        ret_message = ':balloon: `' + str(today) + '` :balloon:\n'
        
        for i in range(len(countdown_list)):
            target_day = datetime.date(countdown_list[i]['year'], countdown_list[i]['month'], countdown_list[i]['day'])
            difference = target_day - today
            if difference.days >= 0:
                ret_message += ('\n距離 `' + countdown_list[i]['event'] + '` 還剩下 `' + str(difference.days) + '` 天')
        
        ret_message += '\n:rip:'
        return ret_message
    
    if now_message == 'help':
        return 'Available commands: ping, roll, countdown, help.'
    
    return 'ʕ•ᴥ•ʔ'