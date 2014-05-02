'''
---hash table---dictonary
etos={}
etos= {'hello':'hola','goodbye':'adios'}
etos['horse']='caballo'
print etos['hello']

for key in etos.keys():
    print key+":"+etos[key]
    '''
    
    
    
'''
In-Class Assignment:

Write a Python program that uses Python's built-in dictionary structure. Your program should:
creates a dictionary mapping company names to phone numbers. Put three items in your hash table to begin.
Allows the end-user to 1) add new mappings to the table by entering a name and a number, or 2) enter a name to see the corresponding phone number. Within a loop, prompt the end-user to choose operation 1 or 2, then prompt for the necessary inputs, then call the chosen operation.
'''
  
pbook={}
pbook={'A':100,'B':200,'C':300}

def function(option):
    if option==1:
        print "adding new record\n"
        name=raw_input("please input the company name:")
        number=raw_input("please input the company phone number:")
        pbook[name]=number
        print name+":"+number
        return
    elif option==2:
        name=raw_input("please input the company name:")
        try:
            print "Company phone number is:"+str(pbook[name])
            return
        except:
            print "Company name not found"
            return
            
option=raw_input("which function?")
option=int(option)
function(option)

for key in pbook.keys():
    print key+":"+str(pbook[key])


