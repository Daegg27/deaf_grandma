def deaf_grandma():

   
    print("HEY KID!")
    
    number_of_goodbyes = 0
    
    while number_of_goodbyes < 2:
        user_input = input("Enter Input: ")
        
        if user_input == "GOODBYE!" and number_of_goodbyes < 1:
            print("LEAVING SO SOON?")
            number_of_goodbyes = 1
        elif user_input == "GOODBYE!" and number_of_goodbyes == 1:
            print("LATER, SKATER!")
            number_of_goodbyes = 2
        elif len(user_input) == 0:
            print("WHAT?!")
            number_of_goodbyes = 0
        elif user_input.isupper():
            print("NO, NOT SINCE 1946")
            number_of_goodbyes = 0
        elif user_input.isupper() == False:
            print("SPEAK UP, KID!")
            number_of_goodbyes = 0





deaf_grandma()