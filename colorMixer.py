while True :
    primarycolor1 = input("Enter primary color:")
    primarycolor2 = input("Enter primary color:")
    if (primarycolor1 =='red' and primarycolor2 == 'blue') or (primarycolor1 == 'blue' and primarycolor2 == 'red'):
        print("When you mix red and blue, you get purple.")
    elif (primarycolor1 == 'red' and primarycolor2 == 'yellow') or (primarycolor1 == 'yellow' and primarycolor2 == 'red'):
        print("When you mix yellow and red, you get orange.")
    elif (primarycolor1=='blue' and primarycolor2=='yellow') or (primarycolor1=='yellow' and primarycolor2=='blue'):
        print("When you mix blue and yellow, you get green.")
    else: print("You didn't input two primary colors.")
