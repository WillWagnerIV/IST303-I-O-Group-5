# IST303 I/O Group 5
# Abinash Adhikari, Chukwudi Oguejiofor, William Wagner, Siyu Xiang, Manar Al-kayed


import sys

#Given Nested distionary data for clubMembers
clubMembers = {   
    '523-8943' : {'Name': 'Ariel Gonzalez', 'Address': '3 Wisteria Lane', 'Sex': 'M', 'Role':''},
    '112-7832' : {'Name': 'Anna-Marie Smith', 'Address': '221B Baker Street', 'Sex': 'F', 'Role': 'Chair'},
    '334-9054' : {'Name': 'Jie Zhang', 'Address': '18 George Street', 'Sex': 'F', 'Role': 'Secretarey'},
    '521-4104' : {'Name': 'Babak Ali', 'Address': '46 Haley Street', 'Sex': 'M', 'Role': 'Treasurer'},
    '763-8223' : {'Name': 'Grace Mendonda', 'Address': '186 Fleet Street', 'Sex': 'F', 'Role':''}
}

#Function to display information for give phone number
def displayLookupMember(phNumber):
    #get keys from data dictonary
    keys = tuple(clubMembers.keys());
    #check if the phonenumber is in keys of clubmember else return error message
    if(phNumber in keys ):
        #if phone number exits print the detail information
        print ("Details for person with phone number " + phNumber + ':')
        for x,y in clubMembers[phNumber].items():
            print (x + ": "+ y )
    else:
        print("Key not found")  
    

# get 1st argument from command line if given
args = []
args = sys.argv
if(len(args) > 1): 
    phNumber=args[1] 
else: 
    phNumber=""

# if argument was not passed in command line get from input instead
if(phNumber == ""):
    phNumber = input("Enter phone number: ")

displayLookupMember(phNumber)