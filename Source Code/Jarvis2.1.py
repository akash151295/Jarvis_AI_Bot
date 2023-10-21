import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser as wb
import pywhatkit
import weatherAPI
import pyjokes
from newsapi import NewsApiClient
import time
import smtplib
from secrets import sender_email, sender_pwd, to_email
from email.message import EmailMessage


engine = pyttsx3.init()

rate = str(engine.getProperty('rate'))
# print(rate)
engine.setProperty('rate', 150)
# print(rate)

volume = str(engine.getProperty('volume'))
# print(volume)
engine.setProperty('volume', 1.0)

def userQuestions(user_txt):
    print("this is user text", user_txt)
    if 'change voice' in user_txt or 'change' in user_txt or 'voice' in user_txt:
        setAIVoiceType(user_txt)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'time' in user_txt:
        getcurrentTime()
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'date' in user_txt:
        getcurrentDate()
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'open document' in user_txt or 'document' in user_txt or 'directory' in user_txt:
        openDocument(user_txt)
        time.sleep(5)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'search' in user_txt or 'google' in user_txt or 'Google' in user_txt:
        googleSearch()
        time.sleep(5)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'youtube' in user_txt or 'Youtube' in user_txt or 'utube' in user_txt or 'YouTube' in user_txt:
        youtubeSearch()
        time.sleep(5)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'offline' in user_txt or 'stop' in user_txt or 'shutdown' in user_txt:
        engine.say("Thanks you !! I am going for sleep now !! Good Night !!")
        engine.runAndWait()
        quit()
    elif 'jokes' in user_txt or 'joke' in user_txt:
        engine.say(pyjokes.get_joke(language='en'))
        engine.runAndWait()
        time.sleep(5)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'find document with name' in user_txt or 'find document' in user_txt or 'find' in user_txt:
        findDocumentsWithWildcardName(user_txt)
        time.sleep(5)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'weather' in user_txt or 'wether' in user_txt:
        engine.say("Can you Please tell me the city name ?")
        engine.runAndWait()
        City = takeVoiceCommand()
        temperature, feelsLike_temperature, humidity, grnd_level, City_NotFound = weatherAPI.getweather(City, 'YOUR API KEY')
        engine.say(f"{City} weather is {'%.f' % temperature} degree C but it feels like {'%.f' % feelsLike_temperature} degree Celcius.")
        engine.runAndWait()
        engine.say(f"{City} humidity is {humidity} gram per cubic meter")
        engine.runAndWait()
        engine.say(f"{City} groud level is {grnd_level} MD.")
        engine.runAndWait()
        time.sleep(5)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif 'news' in user_txt or 'headlines' in user_txt or 'headline' in user_txt:
        getLatestNews()
        time.sleep(2)
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()
    elif user_txt == '' or user_txt == ' ':
        engine.say("Sorry Unable to Recognize you Can you please repeat your query sir ?")
        engine.runAndWait()
    elif 'No' in user_txt or 'Thanks You' in user_txt or 'no' in user_txt or 'Thank You' in user_txt:
        engine.say("Thanks you !! I am going for sleep now !! Good Night !!")
        engine.runAndWait()
        quit()
    elif 'send email' in user_txt or 'send mail' in user_txt or 'email' in user_txt or 'mail' in user_txt:
        speak("Okay sir can you please type the email ID of the person which you wants to drop a mail?")
        Reciever_EmailID = getCMDText()
        speak("Okay sir can you please tell me the email subject content?")
        Email_Subject = takeVoiceCommand()
        speak("Okay sir can you please tell me the email body content?")
        EmailBody = takeVoiceCommand()
        time.sleep(5)
        speak("Okay sir let me drop a mail as per your request")
        sendEmail(Reciever_EmailID, EmailBody, Email_Subject)
        # Reciever_EmailID, EmailBody, Email_Subject
        speak("Mail sent sir!!")
        time.sleep(5)
        speak("Please let me know in case you want me to help on any other topic !!")
    else:
        engine.say("Sorry currently I am not trained to do this!!")
        engine.runAndWait()
        engine.say("Please let me know in case you want me to help on any other topic !!")
        engine.runAndWait()


def getAIVoiceType():
    gender = []
    voice = engine.getProperty('voices')
    print(voice[0].id)
    voice_type = voice[0].id
    if 'DAVID' in voice_type:
        gender.clear()
        gender.insert(0, "MALE")
    elif 'ZIRA' in voice_type:
        gender.clear()
        gender.insert(0, "FEMALE")
    return gender[0]


def setAIVoiceType(user_txt):
    if 'change voice' in user_txt or 'change' in user_txt or 'voice' in user_txt:
        engine.say("What will be your Gender Preference ? Male OR Female ?")
        engine.runAndWait()
        user_choice_voice = takeVoiceCommand()
        # user_choice_voice = int(input(""))
        voices = engine.getProperty('voices')
        if user_choice_voice == 'Male' or user_choice_voice == 'male' or user_choice_voice == 'mail':
            engine.setProperty('voice', voices[0].id)
            engine.say("Hi I am Henry !!")
            engine.runAndWait()
        elif user_choice_voice == 'Female' or user_choice_voice == 'female' or user_choice_voice == 'femail':
            engine.setProperty('voice', voices[1].id)
            engine.say("Hi I am kerry !!")
            engine.runAndWait()
    else:
        engine.say("Unable to understand. Please Retry")
        engine.runAndWait()


def getCMDText():
    user_txt = str(input())
    return user_txt


def speak_initalNotes():
    greetings()
    # wishme()
    engine.say(f'''I am your AI bot!!
               Please let me know how can I help you ??
               ''')
    engine.runAndWait()


def speak_userTextFromCMD(audio):
    engine.say(f'''Okay !! You are asking me  {audio}''')
    engine.runAndWait()


def speak_userTextFromAudio(audio):
    engine.say(f'''Okay !! You are asking me  {audio}''')
    engine.runAndWait()


def getcurrentTime():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    time_str = str(time)
    engine.say(f'''Current time is {time_str}''')
    engine.runAndWait()


def getcurrentDate():
    date = datetime.datetime.now().date()
    date_str = str(date)
    engine.say(f'''Current date is {date_str}''')
    engine.runAndWait()


def openDocument(user_txt):
    os.system('explorer C://{}'.format(user_txt.replace('open', '')))


def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        return " "
    return query


def googleSearch():
    engine.say("What you want me to search on Google ??")
    engine.runAndWait()
    user_search_txt_onGoogle = takeVoiceCommand()
    wb.open('https://www.google.co.in/search?q=' + user_search_txt_onGoogle)


def youtubeSearch():
    engine.say("What you want me to play on youtube ??")
    engine.runAndWait()
    topic = takeVoiceCommand()
    pywhatkit.playonyt(topic)


def findDocumentsWithWildcardName(user_txt):
    engine.say("What you please provide me the document name ??")
    engine.runAndWait()
    doc_Name = takeVoiceCommand()
    doc_Name = doc_Name.replace(" ", "")
    print(doc_Name)
    path = "C:/Users/akash.d.chaudhary/OneDrive - Accenture/Desktop/Projects/CiscoVPNDocs/APP-CISC-AnyConnectVPNClient-4.4.03034-MUI/APP-CISC-AnyConnectVPNClient-4.4.03034-MUI/Files"
    dir = os.listdir(path)
    Match_files = []
    # matchFile = [ ]

    for file in dir:
        if file.startswith(doc_Name):
            Match_files.append(file)
    print(Match_files)

    # for docs in files:
    #     # if doc_Name in docs:
    #     files.startswith("prefix")
    #         print(docs)
    #         matchFile = docs
    if len(Match_files) != 0:
        engine.say(f'''I found below documents with having name {doc_Name}.
                {Match_files}''')
        engine.runAndWait()
    else:
        engine.say(f"Sorry it seems there are no documents with name {doc_Name} in your directory!!")
        engine.runAndWait()

def getLatestNews():
    engine.say("Do you want me to tell you today's headlines or any perticular topic !!")
    engine.runAndWait()
    user_input_news = takeVoiceCommand()
    if 'headline' in user_input_news or 'headlines' in user_input_news:
        newsapi = NewsApiClient(api_key='c0dc2a40e8ff4e68b1f6b0eb005a5c28')
        data = newsapi.get_top_headlines(sources='bbc-news')
        newsdata = data["articles"]
        # print(newsdata)
        for x,y in enumerate(newsdata):
            print(f'{x}{y["description"]}')
            engine.say(f'{x}{y["description"]}')
            engine.runAndWait()
    elif 'topic' in user_input_news or 'perticular' in user_input_news or 'any' in user_input_news:
        engine.say("Can you tell me which topic you wants to hear?")
        engine.runAndWait()
        user_input_news_topic = takeVoiceCommand()
        newsapi = NewsApiClient(api_key='c0dc2a40e8ff4e68b1f6b0eb005a5c28')
        data = newsapi.get_everything(q=user_input_news_topic, page_size=5)
        newsdata = data["articles"]
        # print(newsdata)
        for x,y in enumerate(newsdata):
            print(f'{x}{y["description"]}')
            engine.say(f'{x}{y["description"]}')
            engine.runAndWait()
    engine.say("Thats it for now. Thank you !!")
    engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetings():
    hour = datetime.datetime.now().hour
    if hour >= 3 and hour < 12:
        speak("Good Morning Sir !!")
    elif hour > 24 and hour <= 8:
        speak("Good Morning Sir !!")
    elif  hour >= 12 and hour <= 15:
        speak("Good Afternoon Sir !!")
    elif  hour > 15 and hour <= 20:
        speak("Good Evening Sir !!")
    elif  hour > 20 and hour <=24:
        speak("Good Night Sir !!")
    else:
        speak("Code issue !!")
    # speak(f"Current Time is {hour} hour.")

def wishme():
    getcurrentDate()
    getcurrentTime()

def sendEmail(Reciever_EmailID, EmailBody, Email_Subject):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_pwd)
    # server.sendmail(sender_email, Reciever_EmailID, EmailBody)
    email_dic = EmailMessage()
    email_dic['From'] = sender_email
    email_dic['To'] = Reciever_EmailID
    email_dic['Subject'] = Email_Subject
    email_dic.set_content(EmailBody)
    server.send_message(email_dic)
    server.close()


# Questions Scope - Change voice, tell today date, tell current time, open my documents, search on google


def Hello():
    gender = getAIVoiceType()
    speak_initalNotes()
    while True:
        # user_Question = getCMDText()
        user_Question = takeVoiceCommand()
        # speak_userTextFromCMD(user_Question)
        # speak_userTextFromAudio(user_Question)
        # print(user_Question)
        userQuestions(user_Question)

Hello()





