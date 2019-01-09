def func():
    people = int(raw_input("Enter the number of people: "))
    cats = int(raw_input("Enter the number of cats: "))
    dogs = int(raw_input("Enter the number of dogs: "))

       
    if people < cats:
        print "Too many cats! The world is doomed!"
    elif people > cats:
        print "Not many cats! The world is saved!"
    elif people < dogs:
        print "The world is drooled on!"
    elif people > dogs:
        print "The world is dry!"
        dogs += 5
        print dogs
    elif people >= dogs:
        print "People are greater than or equal to dogs."
    elif people <= dogs:
        print "People are less than or equal to dogs."
    else:
        people == dogs
        print "People are dogs."
        
        
def main():
    raw_input("Entered")
    func()
main()
