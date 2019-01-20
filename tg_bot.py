import telegram
from time import sleep
from urllib import request
BOT_TOKEN = 'TOKEN'
Bot = telegram.Bot(BOT_TOKEN)
lastMessageId = 0
def getText(Update):
    return Update["message"]["text"]

def getMessageId(Update):
    return Update["update_id"]

def getChatId(Update):
    return Update["message"]["chat"]["id"]

def getUserId(Update):
    return Update["message"]["from_user"]["id"]

def getIp():
    print(request.urlopen('http://ip.42.pl/raw').read())
    return str(request.urlopen('http://ip.42.pl/raw').read(),encoding="utf-8")

def checkIp(Update,userId):
    Bot.sendMessage(userId,getIp())
    return;

def messageHandler(Update):
    global lastMessageId
    text = getText(Update)
    msg_id = getMessageId(Update)
    userId = getUserId(Update)
    lastMessageId = msg_id
    if(text=='/checkip'):
        checkIp(Update,userId)
    print(msg_id, text , userId)
    return


def main():
    global lastMessageId
    Updates = Bot.getUpdates()

    if(len(Updates) > 0):
        lastMessageId = Updates[-1]["update_id"]

    while(True):
        # return a list of object
        Updates = Bot.getUpdates(offset=lastMessageId)
        Updates = [Update for Update in Updates if Update["update_id"] > lastMessageId]
        for Update in Updates:
            messageHandler(Update)
        sleep(2)


if __name__ == "__main__":
    main()
