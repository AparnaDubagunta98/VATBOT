from google.cloud import texttospeech
import os
import speech_recognition as sr
from sent import *
from bot import *



qure = {'q1':0,'q2':0,'q3':0,'q4':0,'q5':0}
issues = []

res_file = open("results.txt","w")

def phase1():
    say("Lets Gets Started! I'm here to plan your Birthday Bash with you this year! Are you excited to plan your birthday?")
    resp = get_resp()
    if(analyze(resp) == 1):
        qure['q1'] =1
        say("Are your parents invited??")
        resp = get_resp()
        if(analyze(resp) == 1):
            qure['q2'] =1
            say("Great!")
        else:
            say("Oh! Thats okay! Do you not want them?")
            if(analyze(get_resp) == 0):
                issues.append("parent issues")
        say("Excited about your friends showing up at the party?")
        resp = get_resp()
        if(analyze(resp) == 1):
            qure['q3'] = 1
            say("Awesome!! Should we have it at home or does outdoors sound more fun?")
            if(get_resp() in ["home","at home","here"]):
                issues.append("prefers home environment")

            else:
                say("Great where?")
                get_resp()
        else:
            issues.append("friend issues")
            say("Thats okay! I'll be an awesome friend!!")

        say("All right looks like we're good to get the party started! Lets Talk about the best part!! Gifts!!")
        phase2()


    else:
        issues.append("dis interest in social event")
        say("Thats okay, Should we just jump to gifts!")
        phase2()


def phase2():
    say("What Sounds better? Video Games or Outdoor Sports?")
    gm = get_resp()
    if("sports" in gm):
        qure['q4'] = 1
        say("Would you like to play alone or with others?")
        lon = get_resp()
        if("alone" in lon):
            issues.append("introvert")
            issues.append("likes to be alone")

        else:
            qure['q5'] = 1
            say("Great!! We're going to have some fun options set up for you!!!")
    else:
        say("Would you like to play alone or with others?")
        lon = get_resp()
        if("alone" in lon):
            qure['q5'] = 1
            issues.append("introvert")
            issues.append("social anxiety")
            say("Thats cool!! I know so many people just like you! I would love to make you guys meet soon!")
    say("All right!! We are all set up! You should get geared up for the amazing decor thats about to make the best birthday you ever had!")
    say("Take care! Bye")
    send_results()


def send_results():
    pos = 0
    neg = 0
    for i in qure.keys():
        if(qure[i] == 1):
            pos +=1
        else:
            neg +=1
    if(pos > neg):
        res_file.write("You have a lovely happy child!")
    else:
        res_file.write("Your child might be suffering from slight Anxiety or depression.\note The following are some Symptoms we detected:\n ")
        for iss in issues:
            res_file.write(iss+"\n")
        res_file.write("Take care!\n")
    res_file.close()




def analyze(text):
    t = text
    print("here")
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)

    if(ss['neg'] > ss['pos']):
        return 0
    else:
        return 1



def begin_game():
        say("My name is Robo. Say Hello to get this game started.")
        user_response = get_resp()
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                say(" You are welcome..")
            else:
                if(greeting(user_response)!=None):
                    say(greeting(user_response))
                    phase1()

        else:
            flag=False
            say("Bye! take care..")
            exit(0)


begin_game()
