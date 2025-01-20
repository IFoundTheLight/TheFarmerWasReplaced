# Imports
from SmartPlant.py import *

# Clear Settings
clear()

PlotsReadyForHarvest = 0

# Loop
while True:

    # Set World Size
    WorldSize = get_world_size() * get_world_size()

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

    # Loop over Rows
    for row in range(get_world_size()):

        # Loop over Cols
        for col in range(get_world_size()):

            # What if needed
            if num_items(Items.Water) > 0:
                if get_water() < 0.5:
                    use_item(Items.Water)

            # Before Harvest
            if can_harvest():

                if HarvestOnlyOnFull:

                    if get_entity_type() == WhatToMake:
                        PlotsReadyForHarvest = PlotsReadyForHarvest + 1

                    if PlotsReadyForHarvest >= WorldSize:
                        harvest()
                        PlotsReadyForHarvest = 0

                else:
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

            # Move East
            move(East)

        # Move North
        move(North)