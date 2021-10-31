def main():     #main for Acroym
    print("This program builds acroyms.")
    x = input("Enter a Phrase : ")      #takes input from user.
    strArr = x.split()                  #split by spaces and store in array
    acro = " "
    for a in strArr:                    #using for loop to store first alphabets 
        firstChar = a[0]                #for each word and store in uppercase.
        acro = acro + firstChar.upper()

    print("The acronym is ", acro)
        

main()
    
