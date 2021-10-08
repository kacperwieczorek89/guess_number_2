def guess_number_2():
    print("""
    Think number between 1 and 1000,
    I'll guess it in max. 10 trials.    
    """)

    minimum = 0
    maximum = 1000
    guess = int((maximum-minimum) / 2) + minimum
    answers = ['too big', 'too small', 'you win']
    while True:
        print(f"I guess: {guess}")
        answer = input("Tell me...too big,too small or you win?  ")

        if answer == answers[2]:
            print("I won!")
            break
        if answer == answers[0]:
            guess = maximum


    return


guess_number_2()