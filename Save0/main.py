HalfWorldSize = get_world_size()
WorldSize = HalfWorldSize * HalfWorldSize

# Check if list contains item
def ListContains(llist, item):
    for listItem in llist:
        if listItem == item:
            return True

def DinoFinder():

    # Clear Settings
    clear()

    # Hats
    change_hat(Hats.Dinosaur_Hat)

    #
    GoEast = False
    GoNorth = False

    # Loop
    while True:

        if (GoNorth == False):
            GoNorth = True
        else:
            GoNorth = False
    
        # Loop over Rows
        for row in range(HalfWorldSize - 1):
            if (GoEast == False):
                GoEast = True
            else:
                GoEast = False

            # Loop over Cols
            for col in range(HalfWorldSize - 1):

                # Move East
                if GoEast:
                    DinoMove(East)
                else:
                    DinoMove(West)

            # Move North
            if GoNorth:
                DinoMove(North)
            else:
                DinoMove(South)

def DinoMove(Direction):
    
    IsMoved = move(Direction)
    
    if (IsMoved == False):

        # Hats
        change_hat(Hats.Straw_Hat)

        # Hats
        change_hat(Hats.Dinosaur_Hat)

        DinoFinder()

# Main
def Main():

    DinoFinder()

    # Clear Settings
    clear()

    #
    PlotsReadyForHarvest = 0
    LastWorldSize = 0
    HarvestedSunflower = 0
    FirstRun = True
    
    # Loop
    while True:

        # Get Half the size of the world
        HalfWorldSize = get_world_size()

        # Set World Size
        WorldSize = HalfWorldSize * HalfWorldSize

        # Reset
        if WorldSize != LastWorldSize:
            clear()
        LastWorldSize = WorldSize
        
        # Sunflower
        HarvestedSunflower = 0
        SunflowerArea = [
            HalfWorldSize * 0, 
            HalfWorldSize * 0 + 1, 
            HalfWorldSize * 1, 
            HalfWorldSize * 1 + 1, 
            HalfWorldSize * 2,
            HalfWorldSize * 2 + 1, 
            HalfWorldSize * 3,
            HalfWorldSize * 3 + 1, 
            HalfWorldSize * 4,
            HalfWorldSize * 4 + 1, 
            HalfWorldSize * 5,
            HalfWorldSize * 5 + 1, 
        ]

        # Items
        hayCount = num_items(Items.Hay)
        carrotCount = num_items(Items.Carrot)
        woodCount = num_items(Items.Wood)
        pumpkinCount = num_items(Items.Pumpkin)

        #
        HarvestOnlyOnFull = False
        if hayCount <= 10000:
            WhatToMake = Entities.Grass
        elif woodCount <= 10000:
            WhatToMake = Entities.Bush
        elif carrotCount <= 10000:
            WhatToMake = Entities.Carrot
        elif pumpkinCount <= 10000:
            WhatToMake = Entities.Pumpkin
            HarvestOnlyOnFull = True
        else:
            WhatToMake = Entities.Grass

        # The current field number
        fieldNum = 0

        # Loop over Rows
        for row in range(HalfWorldSize):

            # Loop over Cols
            for col in range(HalfWorldSize):

                # What if needed
                if num_items(Items.Water) > 0:
                    if get_water() < 0.5:
                        use_item(Items.Water)

                if ListContains(SunflowerArea, fieldNum):

                    if get_ground_type() != Grounds.Soil:
                       till()
                    
                    if get_entity_type() != Entities.Sunflower:
                       plant(Entities.Sunflower)

                    if can_harvest():
                        if measure() > 7:
                            HarvestedSunflower = HarvestedSunflower + 1
                            harvest()

                    if get_ground_type() != Grounds.Soil:
                        till()

                    if get_entity_type() != Entities.Sunflower:
                        plant(Entities.Sunflower)     

                else:

                    # Before Harvest
                    if can_harvest():

                        if HarvestOnlyOnFull:

                            if get_entity_type() == WhatToMake:
                                PlotsReadyForHarvest = PlotsReadyForHarvest + 1

                            if PlotsReadyForHarvest >= WorldSize:
                                harvest()
                                PlotsReadyForHarvest = 0

                        else:
                            #if get_entity_type() == WhatToMake:
                            harvest()
                            PlotsReadyForHarvest = 0

                    # Plant
                    if WhatToMake == Entities.Grass:
                        if get_ground_type() != Grounds.Grassland:
                            till()
                        if get_entity_type() != Entities.Grass:
                            plant(Entities.Grass)

                    elif WhatToMake == Entities.Carrot:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        if get_entity_type() != Entities.Carrot:
                            plant(Entities.Carrot)

                    elif WhatToMake == Entities.Bush:
                        if get_ground_type() != Grounds.Grassland:
                            till()
                        if get_entity_type() != Entities.Bush:
                            plant(Entities.Bush)
                    
                    elif WhatToMake == Entities.Pumpkin:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        if get_entity_type() != Entities.Pumpkin:
                            plant(Entities.Pumpkin)
                        
                    elif WhatToMake == Entities.Sunflower:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        if get_entity_type() != Entities.Sunflower:
                            plant(Entities.Sunflower)         

                # Move East
                move(East)
                fieldNum = fieldNum + 1

            # Move North
            move(North)

        # Reset world if the sunflowers are fucked
        if (FirstRun == False and HarvestedSunflower <= 0):
            FirstRun = True
            clear()
        else:
            FirstRun = False

Main()