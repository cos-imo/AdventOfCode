import sys

def main():

    file=open('input','r')
    data=((file.readlines())[0]).split(', ')

    coordinates=[0,0]
    sign=[1, 1, -1, -1]
    directions=["north", "south", "east", "west"]
    pointing=0
    #0 North
    #1 East
    #2 South
    #3 West

    sys.stdout.write("initialised facing " + str(directions[pointing]) + "\n")

    for element in data:
        pointing+=((element[0]=='L')-(element[0]=='R'))
        pointing=pointing%4
        coordinates[0]+=int(element[1:])*(sign[pointing])*(pointing in [1,3])
        coordinates[1]+=int(element[1:])*(sign[pointing])*(pointing in [0,2])
        sys.stdout.write("turned " + element[0] + " now facing " + directions[pointing] + "\nmoved " + element[1:] + "blocs. Current coordinates: " + str(coordinates) + "\n\n")
    
    sys.stdout.write("position x: " + str(coordinates[0]) + "\nposition y: " + str(coordinates[1]) + "\n\ntotal: " + str(abs(coordinates[0])+abs(coordinates[1])) + "\n")

if __name__=="__main__":
    main()