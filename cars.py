import random

cars = {"Honda":2015,"Toyota":2005,"GMC":2017,"Nissan":1999,"BMW":2022}

def car():
    print("Year:",random.choice(list(cars.values())))
    
    
if __name__=="__main__":
    car()