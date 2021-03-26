print("Welcome to Sebastian's Wacky Adventure! Made by yours truly Sebastian!")


answer = input("Would you like to start? Yes/No ").lower()

if answer == "yes":
    print("Good job! Now lets start")
    answer = input("Your alarm wakes you up? What will you do? Wake up or stay asleep. ").lower()

    if answer == "wake up":
        answer = input("Now you're awake! Will you go outside or brush your teeth? ").lower()

    else:
        print("Welp you stayed asleep, goodnight!")
else:
    print("Boo! you're mean.")