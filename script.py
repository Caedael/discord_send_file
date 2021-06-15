#!/usr/bin/python

import sys, getopt

from discord_webhook import DiscordWebhook

def main(argv):
    inputfile=''
    webhookurl=''
    username='File Bot'
    
    try:
        opts, args = getopt.getopt(argv, "i:w:u:", ["inputfile=", "webhookurl=", "username="])
    except getopt.GetoptError:
        print("input error")
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-i", "--inputfile"):
            inputfile=arg
        elif opt in("-w", "--webhook"):
            webhookurl=arg
        elif opt in("-u", "--username"):
            username=arg

    webhook=DiscordWebhook(url=webhookurl, username=username)
    print(inputfile.partition('/')[1])
    with open(inputfile, "rb") as f:
        webhook.add_file(file=f.read(), filename=inputfile)

    response = webhook.execute()
    print(response)


if __name__ == "__main__":
    main(sys.argv[1:])


