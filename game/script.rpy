define m = Character("Esther")
define u = Character("[player_name]")

init python:
    inventory = []
    has_clocked_in = False
    player_name = "Me"

label start:
    scene bg_store_entrance with fade: 
        size (1920, 1080)

    play music "store_bg.wav"

    "The automatic doors slide open as you step into the bustling store. The scent of perfume fills the air as that is the first section from the entrance."

    u "Wow... This place feels different now that I'm actually an employee."
    u "Come on, Day 1, let's do this!"
    u "Let's see, since I work at the pharmacy, I should probably head there first."

    scene bg_pharmacy_entrance with dissolve: 
        size (1920, 1080)

    play sound "landline_bg.wav"

    "You walk up to the pharmacy counter. It's already busy. Phones are ringing, and the customers are waiting."
    "You feel incredibly awkward just standing there. You decide you should probably ask someone for the manager."

    default chose_awkward_option = False

    menu ask_for_manager:
        "Excuse me, I'm the new hire. Is the manager around?":
            jump manager_appears
        "I should probably just wait here until someone comes by." if not chose_awkward_option:
            $ chose_awkward_option = True
            play sound "customer_ahem.mp3"
            "A customer glares at you, thinking you're cutting the line. Oops."
            stop sound fadeout 0.5
            "You probably should have just asked for the manager. Maybe next time."
            jump ask_for_manager

label manager_appears:
    show esther_friendly at center with dissolve

    m "Ah! You must be the new hire..."
    $player_name = renpy.input("What's your name?", length=20).strip()
    if not player_name:
        $player_name = "Jane"

    m "Welcome to the team, [player_name]! I'm Esther, the pharmacy manager. Let me show you around and get you clocked in."
    m "Follow me to the back!"

    stop music fadeout 0.5

    scene bg_break_room with fade:
        size (1920, 1080)
    m "This is the break room. You can relax here during your breaks and have your meals."
    m "This is also where you would come in first to clock in, leave your jackets and bags, if any."
    m "Here's a neat little locker for you to use. Just put your stuff in there and lock it up."

    call screen personalized_locker
    u "Thanks, Esther! This locker is really nice."
    m "No problem! Now, let's get you clocked in so you can start working."
    m "To do that, you're going to need this. It's your employee swipe card. Just swipe it here at the clock-in station, and you'll be good to go."

    "Esther hands you the swipe card, and you take it, feeling a bit more official now that you have it in your hand."
    $ inventory.append("Employee Swipe Card")

    "{b}System:{/b} You have received an Employee Swipe Card! It has been added to your inventory."

    u "Got it! Thanks, Esther. I'll make sure to keep it safe."
    m "Go ahead and swipe it at the clock-in station to get started. I'll be around if you have any questions or need help with anything."

scene bg_clock_in_station with fade
play sound "clock_in.wav"
"You walk over to the clock-in station, swipe your card, and hear a satisfying beep. The screen confirms that you've successfully clocked in for your shift."
$ has_clocked_in = True

"{b}System:{/b} You have successfully clocked in! You're now ready to start your shift."

u "Alright, I'm clocked in! Time to get to work!"
m "Great! Follow me to the pharmacy counter, and I'll show you how everything works."

return