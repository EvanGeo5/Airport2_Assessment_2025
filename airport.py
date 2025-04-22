# This is an airport with little traffic that needs to manage the landing and the take off queues.
# I decided to use lists for the planes and the random library for the simulation

import random

# This function will add the planes inside the take off que and landing que depending on the input given
def airlines_on():
    #plane_dict = {1: "plane011",2: "plane012", 3:"plane013",4:"plane014",5:"plane015"}
    plane_log = ["plane011", "plane012", "plane013", "plane014", "plane015"]
    takeoff_que = []#plane_dict[1], plane_dict[2]]#,plane_dict[3]] 
    landing_que = []
    plane = 0
    for plane in plane_log: #range(len(plane_dict)):
        if plane not in takeoff_que or landing_que == None:
            air_control = input(random.choice(plane_log) + " requesting take off: ")
            if air_control == "take off":
                takeoff_que.append(plane)
                print(plane, " added to take off list")
                print(takeoff_que)
            else:
                print("Wrong command was given")
                takeoff_que.remove(plane)
        elif plane in takeoff_que or landing_que == None:
            air_control2 = input(random.choice(plane_log) + " requesting to land")
            if air_control2 == "land":
                landing_que.append(plane)
                print(plane, " added to landing list")
                print(landing_que)
            else:
                return "Request rejected"
        else:
            emergencyLandings()
    print("No plane registered")

# This function will add the planes from the take off que to the emergency landing que depending on the input
def emergencyLandings():
    emergency_land = []
    takeoff_que = []

    for plane in range(len(takeoff_que)):
        emergency_landing = input(random.choice(takeoff_que) + " requesting emergency landing: ")
        if emergency_landing == "land":
            emergency_land.append(plane)
            print(plane, " has started an emergency landing")
            print(emergency_land)
        return "Denied"
    print("No emergency identified")
airlines_on()
    
    








        
    
    


            