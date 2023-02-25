from ART import *

NEON = '\033[92m'
RESET = '\033[0m'

print(NEON + bang)
print(bed)
print("A.wakes up in his apartment.")

if input("Stands up and looks through the window?Type yes or no ").lower() == 'yes':
    print("He gets out of bed and goes to look at the city that is still asleep. "
          "A monochromatic and lifeless city. The city where A. was born and continues to live.")
    print(window)

input("A. is about to walk up to the shelf and take his glasses.Type 'go' ")
print(shelf)
print(glasses)

print("On his way to the kitchen, he notices an old television set and remembers his natural obligation to his body.")
if input('Take a closer look at TV or go to the toilet.Type tv or toilet ').lower() == "tv":
    print("Heh.It's better to take a shit on deserted streets...")
    print(tv_set)
else:
    print(toilet)

if input("A. let out a heavy sigh and began to think about whether he should drink tea or coffee. "
         "Many thoughts were trying to break through his mind right now... "
         "But he doesn't give up under their pressure and continues to choose between tea and coffee."
         "Type tea or coffee ").lower() == 'coffee':
    print("A.goes to the kitchen and takes a cup of coffee.")
    print("Good old coffee , always stays the same")
    print(coffee)

else:
    print("A.goes to the kitchen.He takes a tea bag and puts it in a cup with boiling water.")
    print(tea_first)
    if input("A.Three days in a row with the same tea bag...what a wonderful life in the tomorrow's world."
             "To drink the tea or throw the tea bag away, that's the question.Type tea or throw ").lower() == 'tea':
        print(tea_second)
        print("Hot tea and nothing more...")
    else:
        print("When you look into a garbage bin, the garbage bin looks back at you.A.smiling")
        print(garbage_bin)

input("Perhaps it's time for my endless walk?Type anything to continue ")
print(outside)
input("The city that never ends. A. has never seen the beginning of this city, nor the end. "
      "It is an eternal, burning, monochromatic, deserted city...Type anything to continue ")
input("A. always woke up in his apartment, making the most important choice of his life."
      " Freshly brewed coffee or a three-day-old tea bag...After that, he would get ready and go for a walk..."
      "Type anything to continue ")
input("The city that never ends. A. has never seen the beginning of this city, nor the end. "
      "It is an eternal, burning, monochromatic, deserted city...Type anything to continue ")
input("What was the purpose of this walk, he did not understand..."
      "But the voice in his head said that he needed to find a place that would be different from this monotonous city."
      "Type anything to continue ")
input("He keeps walking, still walking...Type anything to continue ")
input("He keeps walking, still walking...Type anything to continue ")
input("А. unexpectedly finds himself in the middle of the road...Type anything to continue ")
print(death_On_the_road)
input("The car is traveling at the speed of sound...Type anything to continue ")
input("A. lies on the asphalt the color of the sun, and the sun shines on him the color of the asphalt..."
      "Type anything to continue ")
print("He is probably dying...The END...")
print("*Dedicated to cheap brandy.")
# print(tea_first)
# print(bed)
# print(tea_first)
# print(tea_second)
# print(coffee)
# print(outside)

