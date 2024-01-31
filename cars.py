import random

cars = ["Honda","Toyota","GMC","Nissan","BMW"]

def car():
    # for i in range(len(cars)):
    #     print(f"{i}. {cars[i]}")
    print(random.choice(cars))
    
    
if __name__=="__main__":
    car()