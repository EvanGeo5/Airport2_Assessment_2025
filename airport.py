# This is an airport with little traffic that needs to manage the landing and the take off queues.
# I decided to use lists for the planes and the random library for the simulation

import random

# This function will add the planes inside the take off que and landing que depending on the input given and later will put
# the planes that have a malfunction inside the emergency landing list
def airlines_on():
    #plane_dict = {1: "plane011",2: "plane012", 3:"plane013",4:"plane014",5:"plane015"} was my idea of using a dictionary for this task
    plane_log = ["plane011", "plane012", "plane013", "plane014", "plane015", "plane016", "plane017", "plane018"]
    takeoff_que = []#plane_dict[1], plane_dict[2]]#,plane_dict[3]] if i used a dictionary 
    landing_que = []
    emergency_land = []
    plane = random.choices(plane_log)
    if landing_que == []:
        for plane in plane_log:
            if plane not in takeoff_que:
                air_control = input(random.choice(plane_log) + " requesting take off: ") # input the plane's name
                takeoff_que.append(air_control)
                print(air_control, " added to take off list")
                print(takeoff_que)
                if air_control == False:
                    takeoff_que.remove(plane)
                    print("Wrong command was given")
            elif plane in takeoff_que:
                air_control2 = input(random.choice(plane_log) + " requesting to land: ") # input the plane's name
                landing_que.append(air_control2) 
                print(air_control2, " added to landing list")
                print(landing_que)
                if air_control2 == False:
                    print("No plane registered")
                    return "Request rejected"
                elif plane in landing_que:
                    for plane in landing_que:
                        malfunction = random.randint(1,10) #if the malfunction's scale is 8 and above then the following loop will be executed
                        if plane not in takeoff_que and malfunction >= 8:
                            emergency_landing = input(random.choice(landing_que) + " requesting emergency landing: ") # input the plane's name
                            emergency_land.append(emergency_landing)
                            landing_que.append(emergency_landing)
                            print(emergency_landing, " has started an emergency landing")
                            print(emergency_land,'\n',landing_que)
                        else:    
                            print("No emergency identified")
    else: 
        print("Landing que is full")
airlines_on()





    
    








        
    
    


            