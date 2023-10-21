from tkinter import *
# import read_UnreadEmails_copy
import win32com.client
import ctypes # for the VM_QUIT to stop PumpMessage()
import pythoncom
import re
import time
import psutil
import json
import re
import sys
import os
from collections import OrderedDict
import datetime as dt
import tkinter as tk
# from PIL import Image, ImageTk
import datetime
import pandas as pd
from datetime import time, timedelta
import OS
import win32timezone

unread_Emails = []
unread_Emails_RcvTime = []

upcoming_Meetings = []
upcoming_Meetings_startTime = []
upcoming_Meetings_endTime = []

user_firstname, user_lastname = OS.getUserFirstAndLastName()
user_id = OS.getUserID()

def getUnreadEmails():

    # print("Hi Good Morning!! I am happy to help you to get your unread mails.")

    # user_firstname = 'Akash'
    # user_lastname = 'Chaudhary'

    name_String1 = "@" + user_lastname + ", " + user_firstname
    name_String2 = "Hi " + user_firstname

    # Outlook MAPI
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    lastWeekDateTime = dt.datetime.now() - dt.timedelta(days = 7)
    lastWeekDateTime = lastWeekDateTime.strftime('%m/%d/%Y %H:%M %p')

    # Inbox Folder
    inbox = outlook.GetDefaultFolder(6)
    root_folder = outlook.Folders.Item(1)
    # print(root_folder.Name)

    messages = inbox.Items
    # print(messages.Subject)

    messages = messages.Restrict("[ReceivedTime] >= '" + lastWeekDateTime +"'")

    # for message in messages:
    #     print(message.Subject)
    # print(
    #     "Hey " + user_firstname + " " + user_lastname + " below are the unread emails in your inbox which are unread. Please take required action.")
    #
    # label = Label(root, text="Hey " + user_firstname + " " + user_lastname + " below are the unread emails in your inbox which are unread. Please take required action.")
    # label.pack(fill = BOTH, expand = True)

    # Check for unread emails when starting the event
    # i = 1
    # while i!=3:
    for message in messages:
        # @Chaudhary, Akash / Hi Akash
        if  (message.UnRead) and (name_String1 in str(message.Body) or name_String2 in str(message.Body)):
            # print(message.Subject)
            print("Inside for loop..")
            unread_Emails.append(message.Subject)
            unread_Emails_RcvTime.append(message.ReceivedTime)
            # print(unread_Emails)
            res = list(OrderedDict.fromkeys(unread_Emails))
            res2 = list(OrderedDict.fromkeys(unread_Emails_RcvTime))
            # print("before priting res and res2")
            # print(res)
            # print(res2)
            # print("priting res and res2")

            frame4 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
            frame4.pack(side=TOP, fill="y")

            label1 = Label(frame4, text=str(res[-1])+" Mail Received Time: "+str(res2[-1]))
            label1.pack()


def recurringEmailsWithNoResponse():

    # print("Hi Good Morning!! I am happy to help you to get your unread mails.")

    # user_firstname = 'Akash'
    # user_lastname = 'Chaudhary'

    name_String1 = "@" + user_lastname + ", " + user_firstname
    name_String2 = "Hi " + user_firstname

    # Outlook MAPI
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    lastWeekDateTime = dt.datetime.now() - dt.timedelta(days = 7)
    lastWeekDateTime = lastWeekDateTime.strftime('%m/%d/%Y %H:%M %p')

    # Inbox Folder
    inbox = outlook.GetDefaultFolder(6)
    root_folder = outlook.Folders.Item(1)
    print(root_folder.Name)

    messages = inbox.Items

    messages = messages.Restrict("[ReceivedTime] >= '" + lastWeekDateTime +"'")
    # print(
    #     "Hey " + user_firstname + " " + user_lastname + " below are the unread emails in your inbox which are unread. Please take required action.")
    #
    # label = Label(root, text="Hey " + user_firstname + " " + user_lastname + " below are the read emails in your inbox for which you have not taken any action yet. Please take required action.")
    # label.pack()

    # Check for unread emails when starting the event
    # i = 1
    # while i!=3:
    for message in messages:
        # @Chaudhary, Akash / Hi Akash
        if (message.UnRead) and (name_String1 in str(message.Body) or name_String2 in str(message.Body)) and ('RE:' in message.Subject):
            # print(message.Subject)
            unread_Emails.append(message.Subject)
            unread_Emails_RcvTime.append(message.ReceivedTime)
            res = list(OrderedDict.fromkeys(unread_Emails))
            res2 = list(OrderedDict.fromkeys(unread_Emails_RcvTime))
            print(res)
            print(res2)
            # label2 = Label(root, text=str(res[-1])+" Mail Received Time: "+str(res2[-1]))
            # label2.pack(fill = BOTH, expand = True)

            frame4 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
            frame4.pack(side=TOP, fill="y")

            label1 = Label(frame4, text=str(res[-1])+" Mail Received Time: "+str(res2[-1]))
            label1.pack()


def getUpcomingMeetings():

    # user_firstname = 'Akash'
    # user_lastname = 'Chaudhary'

    name_String1 = "@" + user_lastname + ", " + user_firstname
    name_String2 = "Hi " + user_firstname

    application = win32com.client.Dispatch('Outlook.Application')
    namespace = application.GetNamespace('MAPI')

    recipient = namespace.CreateRecipient(user_id)
    resolved = recipient.Resolve()

    sharedCalendar = namespace.GetSharedDefaultFolder(recipient, 9)

    appointments = sharedCalendar.Items

    appointments.Sort("[Start]")
    appointments.IncludeRecurrences = "False"

    # Restrict to items in the next 30 days (using Python 3.3 - might be slightly different for 2.7)
    begin = datetime.date.today()
    end = begin + datetime.timedelta(days=5);
    begin1 = datetime.datetime.now()
    begin1_plus1Hr = begin1 + datetime.timedelta(hours=1);
    begin1_plus2Hr = begin1 + datetime.timedelta(hours=2);
    begin1_plus3Hr = begin1 + datetime.timedelta(hours=3);
    begin1_plus4Hr = begin1 + datetime.timedelta(hours=4);
    # begin1_plus5Hr = begin1 + datetime.timedelta(hours=5);

    # print("This is begin1", begin1)
    # print("This is begin1Plus1Hr", begin1_plus1Hr)
    # end = begin + datetime.timedelta(days = 0.5);
    # begin = datetime.datetime.now()
    # end = begin + datetime.timedelta(hours=1);
    # print(begin)
    # print(end)
    # Example: "%d/%m/%Y, %H:%M:%S"
    restriction = "[Start] >= '" + begin.strftime("%m/%d/%Y") + "' AND [End] <= '" +end.strftime("%m/%d/%Y") + "'"
    # restriction = "[Start] >= '" + begin.strftime("%H:%M:%S") + "' AND [End] <= '" +end.strftime("%H:%M:%S") + "'"
    print(restriction)
    restrictedItems = appointments.Restrict(restriction)
    print(restrictedItems)

    currentHour = str(begin1.strftime("%H"))
    print(currentHour)
    currentHourPlusOne = str(begin1_plus1Hr.strftime("%H"))
    print(currentHourPlusOne)
    currentHourPlusTwo = str(begin1_plus2Hr.strftime("%H"))
    print(currentHourPlusTwo)
    currentHourPlusThree = str(begin1_plus3Hr.strftime("%H"))
    print(currentHourPlusThree)
    currentHourPlusFour = str(begin1_plus4Hr.strftime("%H"))
    print(currentHourPlusFour)


    # label = Label(root, text="Hey " + user_firstname + " " + user_lastname + " below are the Upcoming meetings !!")
    # label.pack()
    start_Time = []

    # Iterate through restricted AppointmentItems and print them
    for appointmentItem in restrictedItems:

        start_Time = str(appointmentItem.Start.time())

        # print(start_Time)

        if currentHour in start_Time or currentHourPlusOne in start_Time or currentHourPlusTwo in start_Time or currentHourPlusThree in start_Time or currentHourPlusFour in start_Time:

            # print("{0} Start: {1}, End: {2}, Organizer: {3}".format(
            #       appointmentItem.Subject, appointmentItem.Start,
            #       appointmentItem.End, appointmentItem.Organizer))

            print(appointmentItem.Start.time())
            # print(datetime.datetime.now().time())
            upcoming_Meetings.append(appointmentItem.Subject)
            upcoming_Meetings_startTime.append(appointmentItem.Start.time())
            upcoming_Meetings_endTime.append(appointmentItem.End.time())

            res = list(OrderedDict.fromkeys(upcoming_Meetings))
            res1S = list(OrderedDict.fromkeys(upcoming_Meetings_startTime))
            res1E = list(OrderedDict.fromkeys(upcoming_Meetings_endTime))

            # res1E = sorted(res1E)

            # label3 = Label(root, text=str(res[-1])+" - "+"From: "+str(res1S[-1])+" To: "+str(res1E[-1]))
            # label3.pack(fill = BOTH, expand = True)

            frame4 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
            frame4.pack(side=TOP, fill="y")

            label1 = Label(frame4, text=str(res[-1])+" - "+"From: "+str(res1S[-1])+" To: "+str(res1E[-1]))
            label1.pack()


root = Tk()

root.title("Outlook Buddy")

root.geometry("1200x400+468+158")
    # root.resizable(0, 0)
    # # root.geometry("400x591+468+158")
    # root.configure(borderwidth="1")
    # root.configure(relief="sunken")
    # # root.configure(background="#71706E")
    # root.configure(cursor="arrow")
    # root.configure(highlightbackground="#d9d9d9")
    # root.configure(highlightcolor="black")

def run():
        # Bot Label Frame
        frame1 = Frame(root, bg="blue", borderwidth=5, relief=SUNKEN)
        frame1.pack(side=TOP, fill="x")
        l1 = Label(frame1, text="BOT", font="comicsansms 15 bold", fg='orange', bg = "blue")
        l1.pack(padx=215)

        # Outlook Emails button Frame
        frame2 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
        frame2.pack(side=LEFT, fill="y")
        b1 = Button(frame2, text="Number of Open Emails", padx=5, background = "green", fg = "white", font="comicsansms 10 bold", command=getUnreadEmails)
        b1.pack(pady=10, padx=0)
        b2 = Button(frame2, text="Recurring Emails with No Response", padx=5, background = "green", fg = "white", font="comicsansms 10 bold", command=recurringEmailsWithNoResponse)
        b2.pack(padx=0)

        # Outlook Meetings button Frame
        frame3 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
        frame3.pack(side=RIGHT, fill="y")
        b3 = Button(frame3, text="Upcoming Meetings", padx=5, background = "green", fg = "white", font="comicsansms 10 bold", command=getUpcomingMeetings)
        b3.pack(pady=10, padx=0)

        root.mainloop()

def clear_history():
    label1, label2 = printSomething()
    label1.config(text="")
    label2.config(text="")
    label1.destroy()
    label2.destroy()

def reset():
    '''Reset the list of participants'''
    for child in root.winfo_children():
        child.destroy()


# run()