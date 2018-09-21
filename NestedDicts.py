# IST303 I/O Group 5
# Abinash Adhikari, Chukwudi Oguejiofor, William Wagner, Siyu Xiang, Manar Al-kayed


import sys
# print('Program arguments:', sys.argv)

clubMembers = {   
    '523-8943' : {'Name': 'Ariel Gonzalez', 'Address': '3 Wisteria Lane', 'Sex': 'M'},
    '112-7832' : {'Name': 'Anna-Marie Smith', 'Address': '221B Baker Street', 'Sex': 'F', 'Role': 'Chair'},
    '334-9054' : {'Name': 'Jie Zhang', 'Address': '18 George Street', 'Sex': 'F', 'Role': 'Secretarey'},
    '521-4104' : {'Name': 'Babak Ali', 'Address': '46 Haley Street', 'Sex': 'M', 'Role': 'Treasurer'},
    '763-8223' : {'Name': 'Grace Mendonda', 'Address': '186 Fleet Street', 'Sex': 'F'}
}

def lookupMember(phNumber):

    print ("Details for person with phone number " + phNumber + ':')
    for x,y in clubMembers[phNumber].items():
        print (x + ": "+ y )
    print ()

phNumber = sys.argv[1]

lookupMember(phNumber)