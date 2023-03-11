import random
import datetime

tar1 = {'view':'true', 'event':'微積分小考1', 'year':2023, 'month':3, 'day':6, 'last':1, 'add':''}
tar2 = {'view':'true', 'event':'校內志願選填截止', 'year':2023, 'month':3, 'day':13, 'last':1, 'add':''}
tar3 = {'view':'true', 'event':'微積分第一次期中考', 'year':2023, 'month':3, 'day':21, 'last':1, 'add':''}
tar4 = {'view':'true', 'event':'最後一次段考', 'year':2023, 'month':3, 'day':28, 'last':2, 'add':''}
tar5 = {'view':'true', 'event':'個申第一階段放榜', 'year':2023, 'month':3, 'day':30, 'last':1, 'add':''}
tar6 = {'view':'true', 'event':'微積分小考2', 'year':2023, 'month':4, 'day':10, 'last':1, 'add':''}
tar7 = {'view':'true', 'event':'微積分第二次期中考', 'year':2023, 'month':4, 'day':25, 'last':1, 'add':''}
tar8 = {'view':'true', 'event':'個人研究交件', 'year':2023, 'month':5, 'day':1, 'last':1, 'add':''}
tar9 = {'view':'true', 'event':'微積分小考3', 'year':2023, 'month':5, 'day':15, 'last':1, 'add':''}
tar10 = {'view':'true', 'event':'畢業典禮', 'year':2023, 'month':6, 'day':5, 'last':1, 'add':'一路順風'}
tar11 = {'view':'true', 'event':'112 分科測驗', 'year':2023, 'month':7, 'day':12, 'last':2, 'add':''}

countdown_list = [tar1, tar2, tar3, tar4, tar5, tar6, tar7, tar8, tar9, tar10, tar11]

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
            if difference.days == 0:
                ret_message += ('今天是 `' + countdown_list[i]['event'] + '`！\n')
                if countdown_list[i]['add'] != '':
                    ret_message += ('可愛的 hsindoditto 祝大家' + countdown_list[i]['add'] + ' :tada:\n')
            if countdown_list[i]['view'] == 'false':
                continue
            if difference.days < 0:
                if abs(difference.days) < int(countdown_list[i]['last']):
                    ret_message += ('今天是 `' + countdown_list[i]['event'] + '`！\n')
            if difference.days > 0:
                ret_message += ('\n距離 `' + countdown_list[i]['event'] + '` 還剩下 `' + str(difference.days) + '` 天')
        
        ret_message += '\n<:rip:900761668542414879>'
        return ret_message
    
    if now_message == 'help':
        return 'Available commands: ping, roll, countdown, help.'
    
    if now_message.startswith('admin'):
        tmp = now_message.split(' ', 1)
        
        if len(tmp) == 1:
            return 'o_o'
        
        if tmp[1] == 'time':
            return str(datetime.datetime.today())
        
        return '>_<'
    
    return 'ʕ•ᴥ•ʔ'