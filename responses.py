import random
import datetime
import json

# tar1 = {'view':'true', 'event':'微積分第二次期中考', 'year':2023, 'month':4, 'day':25, 'last':1, 'add':''}
# tar7 = {'view':'true', 'event':'普物期中考', 'year':2023, 'month':4, 'day':27, 'last':1, 'add':''}
# tar2 = {'view':'true', 'event':'個人研究交件', 'year':2023, 'month':5, 'day':1, 'last':1, 'add':''}
# tar3 = {'view':'true', 'event':'分科模擬考2', 'year':2023, 'month':5, 'day':10, 'last':2, 'add':''}
# tar4 = {'view':'true', 'event':'微積分小考3', 'year':2023, 'month':5, 'day':15, 'last':1, 'add':''}
# tar5 = {'view':'true', 'event':'畢業典禮', 'year':2023, 'month':6, 'day':5, 'last':1, 'add':'一路順風'}
# tar6 = {'view':'true', 'event':'112 分科測驗', 'year':2023, 'month':7, 'day':12, 'last':2, 'add':'科科大破台'}

# countdown_list = [tar1, tar2, tar3, tar4, tar5, tar6, tar7]


def handle_response(message, admin) -> str:
    now_message = message.lower()
    data = {}
    with open('data.json', mode='r', encoding='utf8') as jfile:
        data = json.load(jfile)
    
    if now_message == 'ping':
        return 'pong'
    
    if now_message == 'roll':
        return str(random.randint(1, 6))
    
    if now_message == 'countdown':
        today = datetime.date.today()
        ret_message = ':balloon: `' + str(today) + '` :balloon:\n'
        
        for i in range(len(data['countdown_list'])):
            target_day = datetime.date(data['countdown_list'][i]['year'], data['countdown_list'][i]['month'], data['countdown_list'][i]['day'])
            difference = target_day - today
            if difference.days == 0:
                ret_message += ('今天是 `' + data['countdown_list'][i]['event'] + '`！\n')
                if data['countdown_list'][i]['add'] != '':
                    ret_message += ('可愛的 hsindoditto 祝大家' + data['countdown_list'][i]['add'] + ' :tada:\n')
            if data['countdown_list'][i]['view'] == 'false':
                continue
            if difference.days < 0:
                if abs(difference.days) < int(data['countdown_list'][i]['last']):
                    ret_message += ('今天是 `' + data['countdown_list'][i]['event'] + '`！\n')
            if difference.days > 0:
                ret_message += ('\n距離 `' + data['countdown_list'][i]['event'] + '` 還剩下 `' + str(difference.days) + '` 天')
        
        ret_message += '\n<:rip:900761668542414879>'
        return ret_message
    
    if now_message == 'help':
        return 'Available commands: ping, roll, countdown, help.'
    
    if now_message.startswith('admin'):
        tmp = now_message.split(' ')
        print(tmp[1])
        
        if admin:
            if len(tmp) == 1:
                return 'o_o'
            
            if tmp[1] == 'time':
                return str(datetime.datetime.today())
            
            if tmp[1] == 'help':
                return 'time\n add_countdown: `view, event, year, month, day, last, add`\n add_food\n'
            
            if tmp[1] == 'add_countdown':
                add_str = ''
                if len(tmp) < 8:
                    return 'Failed...'
                if len(tmp) == 9:
                    add_str = tmp[8]
                
                with open('data.json', mode='w', encoding='utf8') as jfile:
                    data['countdown_list'].append({'view':tmp[2], 'event':tmp[3], 'year':int(tmp[4]), 'month':int(tmp[5]), 'day':int(tmp[6]), 'last':int(tmp[7]), 'add':add_str, 'key':int(tmp[4]) * 10000 + int(tmp[5]) * 100 + int(tmp[6])})
                    data['countdown_list'].sort(key = lambda x : x['key'])
                    json.dump(data, jfile)
                    
                return 'Added successfully!'
        
        return '>_<'
    
    return 'ʕ•ᴥ•ʔ'