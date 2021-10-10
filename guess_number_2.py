def guess_number_2():
    print("""
    Think number between 1 and 1000,
    I'll guess it in max. 10 trials.    
    """)

    minimum = 0
    maximum = 1000

    answers = ['too big', 'too small', 'you win']
    try_no = 1
    while True:

        guess = int((maximum - minimum) // 2) + minimum
        print(f"Try no.{try_no}. I guess: {guess}")
        answer = input("""Tell me...
too big, too small or you win?  """).lower()
        if answer not in answers:
            print('Input is not in ["too big", "too small", you win"]')
            continue

        if answer == 'you win':
            print("I won!")
            break
        if answer == 'too big':
            maximum = guess
            try_no +=1
            continue
        elif answer == 'too small':
            minimum = guess
            try_no += 1
            continue

    return


guess_number_2()
