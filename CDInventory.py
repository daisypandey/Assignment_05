#------------------------------------------#
# Title: CDInventory.py
# Desc: Use dictionaries as the inner data type (list of dictionaries)
#       Allows the user to load inventory from file, add CD data, view the current inventory,
#       delete CD from inventory, save data to a text file, and exit the program.
# Change Log: (Who, When, What)
# Daisy Pandey, August 9, 2020, Assignment 5: CD Inventory Script
# Daisy Pandey, August 11, 2020, updated code as suggested from code review
#------------------------------------------#

# Declare variables
dicRow = {} # dic of data row
lstTbl = []  # list of dictionaries to hold data
strChoice = '' # User input
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print()
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses to
        break
    
    if strChoice == 'l':
        # Load existing data
        lstTbl.clear()       
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)            
            print(row)
        print('Above are the items loaded from the file into the memory.')
        objFile.close()
                
    elif strChoice == 'a': 
        # Add data to the table (list of dictionaries) each time the user wants to add data    
        cdId = int(input('Enter an ID: '))
        cdTitle = input('Enter the CD\'s Title: ')
        cdArtistName = input('Enter the Artist\'s Name: ')     
        dicRow = {'id':cdId, 'title': cdTitle, 'artist': cdArtistName}       
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        
    elif strChoice == 'd':
        # Delete an entry from inventory
        delEntry = int(input('What entry do you want to delete? '))
        for entry in range(len(lstTbl)):
            if lstTbl[entry]['id'] == delEntry:
                del lstTbl[entry]
                print()
                print('Your entry is deleted from inventory.')       
                break       
        
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        print('Your data has been saved to the file.')
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')



