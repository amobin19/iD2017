# Ayman Mobin (Walmart Interview Problem) 09/15/2017
north_south = 0 # vertical grid counter
east_west = 0 # horizontal grid counter
grid = [] # list to hold each new grid position [similar to (x,y) coordinate system]
while(True):
    direction = input("Select ^, >, <, or v to tell the driver where to go: ") # arrow input is taken
    if(direction == "^"):
        north_south += 1 # if north increase vertical by 1 on grid
        if((east_west, north_south) not in grid): 
            grid.append((east_west, north_south)) # add to grid list if new position
    elif(direction == "v"):
        north_south -= 1 # if south decrease vertical by 1 on grid
        if((east_west, north_south) not in grid):
            grid.append((east_west, north_south)) # add to grid list if new position
    elif(direction == ">"): 
        east_west += 1 # if east increase horizontal by 1 on grid
        if((east_west, north_south) not in grid):
            grid.append((east_west, north_south)) # add to grid list if new position
    elif(direction == "<"):
        east_west -= 1 # if west decrease horizontal by 1 on grid
        if((east_west, north_south) not in grid):
            grid.append((east_west, north_south)) # add to grid list if new position 
    else:
        break # break out of loop if not arrow input
print("The driver has been to a total of", len(grid), "Walmart stores.") # prints total stores visited 
