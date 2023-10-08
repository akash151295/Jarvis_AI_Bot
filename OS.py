import os
import re

def getUserFirstAndLastName():
    user_id = os.getlogin()
    firstName = re.compile(r"\w*[.]")
    lastName = re.compile(r"[.]\w*")
    firstName_Matches = firstName.findall(user_id)
    lastName_Matches = lastName.findall(user_id)
    FirstNameWithDot = firstName_Matches[0]
    LastNameWithDot = lastName_Matches[1]
    FirstName_UserID = FirstNameWithDot.replace(".","")
    LastName_UserID = LastNameWithDot.replace(".","")
    FirstName_UserID = FirstName_UserID.capitalize()
    LastName_UserID = LastName_UserID.capitalize()
    print(FirstName_UserID, len(FirstName_UserID))
    print(LastName_UserID, len(LastName_UserID))
    return FirstName_UserID, LastName_UserID

def getUserID():
    user_id = os.getlogin()
    return user_id



