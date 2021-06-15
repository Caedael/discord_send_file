#!/usr/bin/python

import sys, getopt

from discord_webhook import DiscordWebhook, DiscordEmbed

def main(argv):
    inputfiles=[]
    webhookurl=''
    username='File Bot'
    
    try:
        opts, args = getopt.getopt(argv, "hi:w:u:", ["help", "inputfile=", "webhookurl=", "username="])
    except getopt.GetoptError:
        print("input error")
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-h", "--help"):
            print("-w; --webhook            Webhook URL")
            print("-i; --inputfile          Inputfile (one file per inputfile argument)")
            print("-u; --username           Username")
            print("-h; --help               this message")
        if opt in("-i", "--inputfile"):
            inputfiles.append(arg)
        elif opt in("-w", "--webhook"):
            webhookurl=arg
        elif opt in("-u", "--username"):
            username=arg

    webhook=DiscordWebhook(url=webhookurl, username=username)
    for inputfile in inputfiles:
        with open(inputfile, "rb") as f:
            webhook.add_file(file=f.read(), filename=inputfile)

    response = webhook.execute()
    print(response)


if __name__ == "__main__":
    main(sys.argv[1:])


