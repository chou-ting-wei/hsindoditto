import random
import datetime
import json

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
    
    if now_message == 'countdown_list':
        ret_message = ':balloon: 倒數事件列表 :balloon:\n'
        for i in range(len(data['countdown_list'])):
            if data['countdown_list'][i]['view'] == 'false':
                continue
            ret_message +=  ('`' + str(data['countdown_list'][i]['year']) + '`/`' + str(data['countdown_list'][i]['month']) + '`/`' + str(data['countdown_list'][i]['day']) + '` `' + str(data['countdown_list'][i]['event']) + '`\n')
        return ret_message
    
    if now_message == 'food':
        return 'hsindoditto 決定這餐要吃 `' + data['food_list'][random.randint(0, int(len(data['food_list']) - 1))] + '`'
    
    if now_message == 'food_list':
        ret_message = ':balloon: 店家列表 :balloon:\n'
        for i in range(len(data['food_list'])):
            ret_message += (str(i + 1) + '. `' + data['food_list'][i] + '` ')
        return ret_message
    
    if now_message == 'help':
        return 'Available commands: ping, roll, countdown, countdown_list, food, food_list, help.'
    
    if now_message.startswith('admin'):
        tmp = now_message.split(' ')
        
        if admin:
            if len(tmp) == 1:
                return 'o_o'
            
            if tmp[1] == 'time':
                return str(datetime.datetime.today())
            
            if tmp[1] == 'add_countdown':
                add_str = ''
                if len(tmp) < 8:
                    return 'Error: expected more data to add countdown.'
                if len(tmp) == 9:
                    add_str = tmp[8]
                if len(tmp) > 9:
                    return 'Error: expected less data to add countdown.'
                
                countdown_index = 0 
                for i in range(len(data['countdown_list'])):
                    if data['countdown_list'][i]['event'] == tmp[3]:
                        countdown_index = i + 1

                if countdown_index > 0:
                    return 'Countdown already exists!'
                
                with open('data.json', mode='w', encoding='utf8') as jfile:
                    data['countdown_list'].append({'view':tmp[2], 'event':tmp[3], 'year':int(tmp[4]), 'month':int(tmp[5]), 'day':int(tmp[6]), 'last':int(tmp[7]), 'add':add_str, 'key':int(tmp[4]) * 10000 + int(tmp[5]) * 100 + int(tmp[6])})
                    data['countdown_list'].sort(key = lambda x : x['key'])
                    json.dump(data, jfile)
                    
                return 'Countdown added successfully!'
            
            if tmp[1] == 'delete_countdown':
                countdown_index = 0 
                for i in range(len(data['countdown_list'])):
                    if data['countdown_list'][i]['event'] == tmp[2]:
                        countdown_index = i + 1

                if countdown_index == 0:
                    return 'Countdown does not exist!'
                
                with open('data.json', mode='w', encoding='utf8') as jfile:
                    data['countdown_list'].pop(countdown_index - 1)
                    json.dump(data, jfile)
                
                return 'Countdown deleted successfully!'
            
            if tmp[1] == 'countdown_list':
                ret_message = ':balloon: 倒數事件列表 :balloon:\n'
                for i in range(len(data['countdown_list'])):
                    ret_message +=  ('`' + str(data['countdown_list'][i]['year']) + '`/`' + str(data['countdown_list'][i]['month']) + '`/`' + str(data['countdown_list'][i]['day']) + '` `' + str(data['countdown_list'][i]['event']) + '`\n')
                return ret_message
                
            if tmp[1] == 'add_food':
                if len(tmp) < 3:
                    return 'Error: expected more data to add food.'
                if len(tmp) > 3:
                    return 'Error: expected less data to add food.'
                
                food_index = 0 
                for i in range(len(data['food_list'])):
                    if data['food_list'][i] == tmp[2]:
                        food_index = i + 1
                
                if food_index > 0:
                    return 'Food already exists!'
                  
                with open('data.json', mode='w', encoding='utf8') as jfile:
                    data['food_list'].append(tmp[2])
                    json.dump(data, jfile)
                      
                return 'Food added successfully!'
            
            if tmp[1] == 'delete_food':
                food_index = 0 
                for i in range(len(data['food_list'])):
                    if data['food_list'][i] == tmp[2]:
                        food_index = i + 1
                
                if food_index == 0:
                    return 'Food does not exist!'
                
                with open('data.json', mode='w', encoding='utf8') as jfile:
                    data['food_list'].pop(food_index - 1)
                    json.dump(data, jfile)
                
                return 'Food deleted successfully!'
            
            if tmp[1] == 'help':
                return 'Available commands:\n time\n add_countdown: `view, event, year, month, day, last, add`\n delete_countdown\n add_food: `food`\n delete_food'
        
        return '>_<'
    
    return 'ʕ•ᴥ•ʔ'