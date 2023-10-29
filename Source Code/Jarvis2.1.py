import pyttsx3
import datetime
import speech_recognition as sr
import os
import pywhatkit
import weatherAPI
import pyjokes
from newsapi import NewsApiClient
import time
import smtplib
from secrets import sender_email, sender_pwd, to_email
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
import clipboard
import time as tt


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
    elif 'Thanks You' in user_txt or 'Thank You' in user_txt:
        engine.say("Thanks you !! I am going for sleep now !! Good Night !!")
        engine.runAndWait()
        quit()
    elif 'send email' in user_txt or 'send mail' in user_txt or 'email' in user_txt or 'mail' in user_txt:
        # speak("Okay sir can you please type the email ID of the person which you wants to drop a mail?")
        # Reciever_EmailID = getCMDText()
        Reciever_EmailID = {
            'akash': 'akash151295@gmail.com',
            'Aakash': 'akash151295@gmail.com',
            'kannu': 'kannuchaudhary518@gmail.com',
            'Kannu': 'kannuchaudhary518@gmail.com',
            'no': 'kannuchaudhary518@gmail.com',
            'ullu': 'kannuchaudhary518@gmail.com',
            'Kaniskha': 'kannuchaudhary518@gmail.com',
            'Kanishka': 'kannuchaudhary518@gmail.com'
        }

        speak("Okay sir can you please tell me the name of the person which you wants to drop a mail?")
        user_inputForMail = takeVoiceCommand()
        Reciever_EmailID = Reciever_EmailID[user_inputForMail]

        speak("Okay sir can you please tell me the email subject content?")
        Email_Subject = takeVoiceCommand()
        speak("Okay sir can you please tell me the email body content?")
        EmailBody = takeVoiceCommand()
        time.sleep(2)
        speak("Okay sir let me drop a mail as per your request")
        sendEmail(Reciever_EmailID, EmailBody, Email_Subject)
        # Reciever_EmailID, EmailBody, Email_Subject
        speak("Mail sent sir!!")
        time.sleep(5)
        speak("Please let me know in case you want me to help on any other topic !!")
    elif 'send message' in user_txt or 'send whatsapp message' in user_txt or 'whatsapp' in user_txt or 'Send whatsapp' in user_txt or 'send WhatsApp message' in user_txt or 'send WhatsApp' in user_txt or 'WhatsApp message' in user_txt or 'WhatsApp' in user_txt:
        Reciever_PhoneNumber = {
            'akash': '+91 97603 27132',
            'Aakash': '+91 97603 27132',
            'Kaniskha': '+91 63987 56633',
            'Kanishka': '+91 63987 56633',
            'Anushka': '+91 639875 6633'
        }
        try:
            speak("Okay sir can you please tell me the name of the person which you wants to send whatsapp message?")
            user_inputForMessage = takeVoiceCommand()
            Reciever_PhoneNumber = Reciever_PhoneNumber[user_inputForMessage]

            speak("Okay sir can you please tell me what message you wants to send")
            Message_Content = takeVoiceCommand()

            time.sleep(2)
            speak("Okay sir let me drop a message as per your request")
            sendWhatsAppMsg(Reciever_PhoneNumber, Message_Content)
            # Reciever_EmailID, EmailBody, Email_Subject
            speak("Whatsapp message sent sir!!")
        except Exception as e:
            print(e)
            speak("Sorry unable to send message")
        time.sleep(5)
        speak("Please let me know in case you want me to help on any other topic !!")
    elif 'read text' in user_txt or 'Read text' in user_txt or 'Read Text' in user_txt:
        readText()
        time.sleep(5)
        speak("Please let me know in case you want me to help on any other topic !!")
    elif 'start application' in user_txt or 'application' in user_txt or 'start' in user_txt or 'Start' in user_txt or 'Application' in user_txt:
        openDesktopApplication()
        time.sleep(5)
        speak("Please let me know in case you want me to help on any other topic !!")
    elif 'screenshot' or 'Screenshot' in user_txt:
        TakeScreenshot()
    elif 'add note' or 'Add note' in user_txt:
        addnote()
    elif 'read note' or 'Read note' in user_txt:
        readnote()
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

def sendWhatsAppMsg(phoneNumber, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phoneNumber+'&text='+Message)
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(5)

def readText():
    speak("Have you already selected any text to read?")
    ans = takeVoiceCommand()
    if 'yes' in ans or 'Yes' in ans:
        text = clipboard.paste()
        print(text)
        speak(text)
    elif 'no' in ans or 'No' in ans:
        speak("Please select the text to read, I will wait for 10 seconds!")
        time.sleep(10)
        text = clipboard.paste()
        print(text)
        speak(text)
    else:
        speak("Sorry something went wrong!!")

def openDesktopApplication():
    speak("Can you please tell me which application you want me to opem for you?")
    applicationName_Usr = takeVoiceCommand()
    if 'pycharm' in applicationName_Usr or 'Pycharm' in applicationName_Usr:
        pycharm_Path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.2\\bin\pycharm64.exe"
        os.startfile(pycharm_Path)
        time.sleep(5)
        speak(f"{applicationName_Usr} is started sir!!")
    elif 'Visual studio' in applicationName_Usr or 'visual studio' in applicationName_Usr or 'visual' in applicationName_Usr or 'Visual' in applicationName_Usr or 'studio' in applicationName_Usr or 'Studio' in applicationName_Usr:
        vs_Path = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vs_Path)
        time.sleep(5)
        speak(f"{applicationName_Usr} is started sir!!")
    else:
        speak("Sorry something went wrong !!")

def TakeScreenshot():
    speak("Taking Screenshot Sir!!")
    nameIMG = tt.time()
    nameIMG = f'C:\\Users\\asus\\OneDrive\\Pictures\\JarvisSS\\${nameIMG}.png'
    img = pyautogui.screenshot(nameIMG)
    img.show()
    speak("Screenshot has been taken and saved inside pictures folder with folder name as JarvisSS")

def addnote():
    speak("what you want me to add into your notes today ?")
    note = takeVoiceCommand()
    remember = open('data.txt', 'w')
    remember.write(note)
    remember.close()
    speak("Added sir !!")

def readnote():
    speak("Below are you notes for Today!!")
    remember = open('data.txt', 'r')
    note = remember.read()
    remember.close()
    speak(note)

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





