import datetime
import json
import os
import random
import subprocess
import threading
import time
import psycopg2
from tempfile import NamedTemporaryFile
import vk_api
import urllib3
import requests
import certifi
from gtts import gTTS

# import textwrap
# from functools import singledispatch
# from   mysql.connector import errorcode
###########################################################
# try:
cnx = psycopg2.connect(user='rakivkbot', password='botpassword',
                       host='127.0.0.1', database='rakivkdb', port='5432', keepalives='0')
cursor = cnx.cursor()
# except mysql.connector.Error as err:
#	 if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#		 print("MYSQL: Wrong username or/and password")
#	 elif err.errno == errorcode.ER_BAD_DB_ERROR:
#		 print("MYSQL: Database does not exist")
#	 else:
#		 print(err)

tWE_del_count = 1
THREAD_REMOVER_DELAY = 30
removerAnimDelay = 6
exitFlag = 0


class removerThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting ' + self.name)
        print_time(self.name, 1, self.counter, self.threadID)
        print('Exiting ' + self.name)


def print_time(threadName, counter, delay, uid_to_remove):
    # # timeToLive = 10
    while counter:
        if exitFlag:
            threadName.exit()
# #     textWaveEdited = textWave
        time.sleep(delay)
#
# # while timeToLive:
# #	 textWaveEdited = getNextTextWave(textWaveEdited)
# #	 vk.method('messages.edit', {'peer_id': uid,'message_id': uid_to_remove,'message': textWaveEdited})
# #	 time.sleep(removerAnimDelay)
# #	 timeToLive -= 1
#
        vk.method('messages.delete', {
                  'message_ids': uid_to_remove, 'delete_for_all': 1})
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter = counter - 1


def getNextTextWave(tWE):

    if tWE_del_count == 3:
        tWE = tWE[3:] + tWE[0] + tWE[1] + tWE[2]
    elif tWE_del_count == 2:
        tWE = tWE[2:] + tWE[0] + tWE[1]
    elif tWE_del_count == 1:
        tWE = tWE[1:] + tWE[0]
    return tWE


def coin():
    if bool(random.getrandbits(1)):
        return 'Орёл!'
    return 'Решка!'

###########################################################


ROOTDIR = os.path.dirname(os.path.abspath(__file__))

textWave = '_,.=\'``\'-.,_,.-\'``\'-.,_,.=\'``\n\tViva la rakus! (⊙_◎)\n_.-\'``\'-.,_,.=\'``\'-.,_,.-\'``\'-'

# butMess = 'Снизу есть кнопки управления ботом.\nЕсли кнопок нет, то надо обновить приложение ВК до последней версии:\nAndroid: vk.cc/android\niPhone: vk.cc/iphone\n'
butMess = 'Команды:\n -- если сказать боту одно слово, то он найдёт цитату, содержащую это слово (возможны вариации)\n -- покажет актуальный гороскоп, если указать ему знак (Овен,Телец,Близнецы,Рак,Лев,Дева,Весы,Скорпион,Стрелец,Козерог,Водолей,Рыбы)\n -- от двух и более слов ботом игнорируется и выдётся эта подсказка после которой прибегает автор и, размахивая клешнями, пытается вступить в ... диалог'
butMessAttach = ['photo-110636654_456239028']

coinsAttach = ['photo-110636654_456239215', 'photo-110636654_456239216']

key = 'ключ'

vk = vk_api.VkApi(
    token='05aeaec72e0f5cab0f3f4854245372b3d65c5a070de9a8b36d8dc7e257ff79f2542a01957e738e641e885'
    )

attach = ['video323745_456239393']

jsonButton = {
    'one_time': False,
    'buttons':
        [
            [{
                'action': {
                    'type': 'text',
                    'payload': json.dumps({'button': '1'}),
                    'label': 'Случайная Цитата'
                },
                'color': 'primary'
            }],
            [{
                'action': {
                    'type': 'text',
                    'payload': json.dumps({'button': '2'}),
                    'label': 'Read Me'
                },
                'color': 'primary'
            }],
            [{
                'action': {
                    'type': 'text',
                    'payload': json.dumps({'button': '3'}),
                    'label': 'Монетка'
                },
                'color': 'default'
            }]
        ]
}

tmpdir = '%s/tmp' % ROOTDIR
horodir = '%s/horoscopes' % ROOTDIR

with open('%s/cancer.today' % horodir, 'r') as text_file:
    textAnswerCancer = text_file.read()
with open('%s/virgo.today' % horodir, 'r') as text_file:
    textAnswerVirgo = text_file.read()
with open('%s/scorpio.today' % horodir, 'r') as text_file:
    textAnswerScorpio = text_file.read()
with open('%s/leo.today' % horodir, 'r') as text_file:
    textAnswerLeo = text_file.read()
with open('%s/capricorn.today' % horodir, 'r') as text_file:
    textAnswerCapricorn = text_file.read()
with open('%s/zmee.today' % horodir, 'r') as text_file:
    textAnswerZmee = text_file.read()
with open('%s/libra.today' % horodir, 'r') as text_file:
    textAnswerLibra = text_file.read()
with open('%s/taurus.today' % horodir, 'r') as text_file:
    textAnswerTaurus = text_file.read()
with open('%s/pisces.today' % horodir, 'r') as text_file:
    textAnswerPisces = text_file.read()

with open('%s/sagittarius.today' % horodir, 'r') as text_file:
    textAnswerSagittarius = text_file.read()
with open('%s/gemini.today' % horodir, 'r') as text_file:
    textAnswerGemini = text_file.read()
with open('%s/aquarius.today' % horodir, 'r') as text_file:
    textAnswerAquarius = text_file.read()
with open('%s/aries.today' % horodir, 'r') as text_file:
    textAnswerAries = text_file.read()

# Send user the signature text


def signature(signText, ruid):
    return vk.method('messages.send', {'peer_id': uid,
                                       'random_id': ruid,
                                       'message': signText
                                       }
    )


def coinSend(coinText, ruid):
    if coinText == 'Орёл!':
        coinImgId = coinsAttach[0]
    else:
        coinImgId = coinsAttach[1]
    return vk.method('messages.send', {'peer_id': uid,
                                       'random_id': ruid,
                                       'attachment': coinImgId,
                                       'message': coinText
                                       }
    )

# Check if is user exist in DB
def uid_exist(uid):
    query = ('select uid from users where uid=%s')
    cursor.execute(query, (uid,))
    rows = cursor.fetchone()
    if rows is None:
        return False
    return True


# Update last visit of user
def uid_update(uid, timestamp):
    query = ('UPDATE users set last_visit=%s WHERE uid=%s')
    cursor.execute(query, (timestamp, uid))
    cnx.commit()
    return True


# get user local DB id by VK uid
def uid_get_id(uid):
    query = ('select id from users where uid=%s')
    cursor.execute(query, (uid,))
    rows = cursor.fetchone()
    if rows is None:
        return False
    return rows[0]


# save user command and bot answer into action table with timestamp
def action_add(uid, cmd, result):
    query = ('insert into actions (cmd,result,user_id) values (%s,%s,%s)')
    cursor.execute(query, (cmd, result, uid))
    cnx.commit()
    return True


# find citates with user words
def finder(uid, cmd):
    ttt = subprocess.check_output(
        ['%s/finder.sh' % ROOTDIR, '%s' % uid, '%s' % cmd])
    print('FIND::: %s' % ttt)
    return ttt


# send answer to user
def answer(uid, ruid, msg, lang=None):
    if lang is not None:
        tts = gTTS(text=msg.decode('utf-8'), lang=lang)
        with NamedTemporaryFile() as fp:
            tts.write_to_fp(fp)
            print(fp.name)
            vkup = vk_api.upload.VkUpload(vk)
            fpdoc = vkup.audio_message(fp.name, peer_id=uid)
            print(fpdoc)
#        fp.close()
        return vk.method('messages.send',
                         {'peer_id': uid,
                          'random_id': ruid,
                          'message': msg,
                          'keyboard': json.dumps(jsonButton,
                                                 ensure_ascii=False,
                                                 sort_keys=True),
                          'attachment': 'doc' + str(fpdoc['audio_message']['owner_id']) + '_' + str(fpdoc['audio_message']['id'])
                          })
    else:
        return vk.method('messages.send',
                         {'peer_id': uid,
                          'random_id': ruid,
                          'message': msg,
                          'keyboard': json.dumps(jsonButton,
                                                 ensure_ascii=False,
                                                 sort_keys=True)
                          })


def unsplah_answer(uid, ruid, query):
    unsplah_key = 'xfumioS5ArKhN4V7NY5kLzzRsZ0uEsWb_XHVOFjqwR4'
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                               ca_certs=certifi.where(),
                               timeout=urllib3.Timeout(connect=10.0, read=5.0),
                               retries=False
                               )
    page = http.request('GET',
                        'https://api.unsplash.com/search/photos/',
                        fields={'query': query,
                                'order_by': 'latest',
                                'per_page': 50,
                                'client_id': unsplah_key
                                }
                        )
    unsplash_results = json.loads(page.data.decode('utf-8'))
    unsplash_links = []
    for _ in unsplash_results['results']:
        unsplash_links += [_['links']['download']]
    print(unsplash_links)
    try:
        link = random.choice(unsplash_links)
    except Exception as e:
        print(f'No Unsplash pic was found for {query=}! {e}')
        link = 'Не нашлось картиночки для оформления. Представьте её сами в воображении...'
        return vk.method('messages.send', {'peer_id': uid, 'random_id': ruid, 'message': link})

    # get photo from Unsplash
    pic = http.request('GET', link, preload_content=False)
    with open(f'{tmpdir}/{uid}.jpg', 'wb') as f:
        f.write(pic.data)
    print(f'PIC SIZE IS: {len(pic.data)}')

    # get VK upload link
    vk_upload_server = vk.method('photos.getMessagesUploadServer')
    # put photo at VK
    filedata = open(f'{tmpdir}/{uid}.jpg', 'rb')
    vk_pic = requests.post(
        vk_upload_server['upload_url'], files={'photo': filedata})
    # get grant answer from VK
    vk_pic_json = vk_pic.json()
    # use grant data to finaly save photo at VK
    result = vk.method('photos.saveMessagesPhoto', {
                       'server': vk_pic_json['server'], 'photo': vk_pic_json['photo'], 'hash': vk_pic_json['hash']})
    # use this VK internal storage photo in VK message
    return vk.method('messages.send', {'peer_id': uid, 'random_id': ruid, 'attachment': f'photo{result[0]["owner_id"]}_{result[0]["id"]}'})

# send answer to user with attachment and keyboard


def answer4(uid, ruid, msg, attach, kbd):
    return vk.method('messages.send', {'peer_id': uid, 'random_id': ruid, 'attachment': attach, 'message': msg, 'keyboard': kbd})


# MAIN LOOP
while True:
    messages = vk.method('messages.getConversations', {
                         'offset': 0, 'count': 8, 'filter': 'unread'})
    if messages['count'] >= 1:

        textStoryFortuneRu = subprocess.check_output(
            ['/usr/games/fortune', '-a', 'ru'])
        textStoryFortuneEn = subprocess.check_output(
            ['/usr/games/fortune', '-a', '/usr/share/games/fortunes/'])

        # тормознём коней -- заметил, что на ифонах без этой паузы выражение пустым получается иногда, не успевает заполнить поле
        # если на ифоне потом подёргать экран, то выражение перезаполняется ОК,
        # но это не вариант. Отписался в ВК. 27.08.2018
        pause = 0.5
        trd = THREAD_REMOVER_DELAY
        uid = messages['items'][0]['last_message']['from_id']
        body = messages['items'][0]['last_message']['text']
        ruid = messages['items'][0]['last_message']['random_id']

        result = cmd = ''
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if uid_exist(uid) == False:
            nameVK = vk.method('users.get', {'user_ids': uid})
            name_First = nameVK[0]['first_name']
            name_Last = nameVK[0]['last_name']
            query = (
                'INSERT INTO users (uid,name,surname,last_visit) VALUES (%s, %s, %s, %s)')
            add_user_data = (uid, name_First, name_Last, timestamp)
            cursor.execute(query, add_user_data)
            cnx.commit()
            print(' %s NAME ===> %s %s ' % (uid, name_First, name_Last))
        else:
            uid_update(uid, timestamp)

        if body.lower() == 'случайная цитата':
            cmd = 'случайная цитата'
            result = textStoryFortuneRu
            answer(uid, ruid, result, 'ru')
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'read me':
            cmd = 'read me'
            result = textStoryFortuneEn
            answer(uid, ruid, result, 'en')
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'рак':
            cmd = 'рак'
            result = textAnswerCancer
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'дева':
            cmd = 'дева'
            result = textAnswerVirgo
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'стрелец':
            cmd = 'стрелец'
            result = textAnswerSagittarius
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'овен':
            cmd = 'овен'
            result = textAnswerAries
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'водолей':
            cmd = 'водолей'
            result = textAnswerAquarius
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'близнецы':
            cmd = 'близнецы'
            result = textAnswerGemini
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'скорпион':
            cmd = 'скорпион'
            result = textAnswerScorpio
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)
        elif body.lower() == 'лев':
            cmd = 'лев'
            result = textAnswerLeo
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)
        elif body.lower() == 'козерог':
            cmd = 'козерог'
            result = textAnswerCapricorn
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)
        elif body.lower() == 'весы':
            cmd = 'весы'
            result = textAnswerLibra
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)
        elif body.lower() == 'змееносец':
            cmd = 'змееносец'
            result = textAnswerZmee
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)
        elif body.lower() == 'телец':
            cmd = 'телец'
            result = textAnswerTaurus
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)
        elif body.lower() == 'рыбы':
            cmd = 'рыбы'
            result = textAnswerPisces
            answer(uid, ruid, result)
            time.sleep(pause)
            last_uid = signature(textWave, ruid)

        elif body.lower() == 'монетка':
            cmd = 'монетка'
            result = coin()
            trd = 13
            last_uid = coinSend(result, ruid)
            time.sleep(pause)

        else:
            cmd = str(body)
            if len(cmd.split(' ')) == 1:
                try:
                    result = finder(uid, cmd.lower())
                except:
                    print('EXCEPT')
                    result = 'Ничего не нашёл! Попробуйте другое слово...'
                    unsplah_answer(uid, ruid, cmd)
                    last_uid = vk.method(
                        'messages.send', {'peer_id': uid, 'random_id': ruid, 'message': result})
                else:
                    print('ELSE')
                    answer(uid, ruid, result)
                    unsplah_answer(uid, ruid, cmd)
                    last_uid = signature(textWave, ruid)
            # usage text and pic
            else:
                kbd = json.dumps(
                    jsonButton, ensure_ascii=False, sort_keys=True)
                result = butMess
                last_uid = answer4(uid, ruid, result, butMessAttach, kbd)
#				last_uid = vk.method('messages.send', {'peer_id': uid, 'attachment': butMessAttach,'message': butMess, 'keyboard': json.dumps(jsonButton, ensure_ascii=False, sort_keys=True)})
                print(str(uid).join('\n'))
                print(str(body).join('\n'))

        action_add(uid, cmd, result)
        thread_remover = removerThread(last_uid, 'REMOVER', trd)
        thread_remover.start()
        time.sleep(3)
