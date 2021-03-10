# Creating a function for move to bin
def mov_to_bin(location_n):
    print("-----------------------------")
    location_n[0] = False
    location_n[2] = False
    location_n[1] = True                         # Turning location at_bin true and all other false
    print("move to bin")
    return location_n


#  Function to pick parts from bins
def pick(gripper_n, part_bins_n, j_n, single_n):
    if j_n == 0:
        part = 'red'
    elif j_n == 1:
        part = 'green'
    elif j_n == 2:
        part = 'blue'

    # If only one part present in bin pick with only right arm
    if single_n is True:
        gripper_n[0] = True                           # Picking with only right arm
        part_bins_n[j_n] = part_bins_n[j_n] - 1       # Decreasing one part from bin
        print(f"picked {part} part with RIGHT arm")

    else:
        gripper_n[0] = True                            # Picking with right arm
        gripper_n[1] = True                            # Picking with left arm
        part_bins_n[j_n] = part_bins_n[j_n] - 2        # Decreasing two parts from bin
        print(f"picked 2 {part} parts with RIGHT and LEFT arms respectively")

    return gripper_n, part_bins_n


#  Function to move to tray
def mov_to_tray(location_n):
    print("-----------------------------")
    location_n[0] = False
    location_n[1] = False
    location_n[2] = True                               # Turning location at_tray true and all other false
    print("move to tray")

    return location_n


#  A function to place parts ion tray
def place(gripper_n, current_tray_n, j_n, single_n):
    if j_n == 0:
        part = 'red'
    elif j_n == 1:
        part = 'green'
    elif j_n == 2:
        part = 'blue'

    #  if there was only one part then increase only one part in kit and turn gripper flags False
    if single_n is True:
        gripper_n[0] = False
        gripper_n[1] = False
        current_tray_n[j_n] = current_tray_n[j_n] + 1
        print(f" place {part} part with right arm")

    # Else increase two parts in kit tray and turn gripper flags false
    else:
        gripper_n[0] = False
        gripper_n[1] = False
        current_tray_n[j_n] = current_tray_n[j_n] + 2
        print(f"place two {part} parts with right and left arms respectively")

    return gripper_n, current_tray_n


# Function to check if number of parts in bins are exceeding 10 or not
def check_max(part_bins_n):
    check = False
    for m in part_bins_n:
        if m > 10:
            print("more than 10 parts in bins please reenter value")
            check = True
    return check


def plan():
    current_tray = []  # Creating empty list for currently present parts in kit tray
    final_tray = []  # Creating empty list for final number of  parts to be present in kit tray
    max_limit = True  # Creating a flag to monitor parts in bins don't exceed 10

    # A while loop which will ask user to again enter the parts of bins if parts entered were greater than 10
    while max_limit is True:
        part_bins = []  # Creating a list to store parts of bins
        b1, b2, b3 = input("how many red/green/blue parts in BINS:").split()
        part_bins.append(int(b1))
        part_bins.append(int(b2))
        part_bins.append(int(b3))
        max_limit = check_max(part_bins)

    c1, c2, c3 = input("how many red/green/blue parts ALREADY in KIT TRAY:").split()
    current_tray.append(int(c1))  # Appending list of current tray parts
    current_tray.append(int(c2))
    current_tray.append(int(c3))

    f1, f2, f3 = input("how many red/green/blue parts TO PUT in KIT TRAY:").split()
    final_tray.append(int(f1))  # Appending list of final tray parts
    final_tray.append(int(f2))
    final_tray.append(int(f3))

    n = 0
    c = 0

    # Checking if the kit tray is already complete or not
    for i in range(len(part_bins)):
        if current_tray[i] == final_tray[i]:
            #  print("kit already complete no need of further actions")
            kit_already_complete = True
            c = c + 1

    # Checking if there are enough parts present in bin or not to fulfill the requirements
    for b in range(len(part_bins)):
        if part_bins[b] >= (final_tray[b] - current_tray[b]):
            n = n + 1
        elif part_bins[b] < (final_tray[b] - current_tray[b]):
            if b == 0:
                print(
                    f"not enough parts in red    {part_bins[b]} present but {(final_tray[b] - current_tray[b])} required")
            elif b == 1:
                print(
                    f"not enough parts in green  {part_bins[b]} present but {(final_tray[b] - current_tray[b])} required")
            elif b == 2:
                print(
                    f"not enough parts in blue   {part_bins[b]} present but {(final_tray[b] - current_tray[b])} required")

    r = 0

    # Checking if current parts in kit tray is are more than the required parts or not
    for d in range(len(part_bins)):
        if current_tray[d] > final_tray[d]:
            r = r + 1
            if d == 0:
                print(" process terminating because more RED parts in kit tray than required")
            elif d == 1:
                print("process terminating because more GREEN parts in kit tray than required")
            elif d == 2:
                print(" process terminating because more BLUE parts in kit tray than required")

    kit_complete = False  # Created a flag for completion of kit tray
    at_home = True  # Created a flag for location at home
    at_bin = False  # Created a flag for location at bin
    at_tray = False  # Created a flag for location at tray
    location = [at_home, at_bin, at_tray]  # Created a list called location to store all location flags
    right_gripper = False  # Created right gripper flag
    left_gripper = False  # Created left gripper flag
    gripper = [right_gripper, left_gripper]  # Created a list to store gripper flags

    # If all preconditions are met then plan will start
    if n == 3 and c != 3 and r == 0:

        # Loop will run until kit is completed
        while kit_complete is False:
            if location[0] is True:
                print("GENERATING PLAN")
                print("-----------------------------")
                print("currently at home position, moving to bin")
                print("-----------------------------")

            for j in range(len(part_bins)):
                pbr = part_bins[j]

                while current_tray[j] != final_tray[j] and current_tray[j] < final_tray[j] and kit_complete is False:

                    # Checking all the preconditions required for MOVING TO BIN
                    if location[1] is False and (gripper[0] is False and gripper[1] is False) and kit_complete is False:
                        location = mov_to_bin(location)  # Called functiom mov_to_bin()

                        #  Checking all the preconditions required to PICK a part from bin
                        if location[1] is True and (gripper[0] is False and gripper[1] is False) and part_bins[j] > 0 and kit_complete is False:

                            # Checking if there are two or more parts remaining to be transferred from bin to tray
                            single = False
                            if final_tray[j] - current_tray[j] < 2:
                                single = True

                            gripper, part_bins = pick(gripper, part_bins, j, single)  # Calling function pick()

                            # Checking all preconditions required for MOVING TO TRAY
                            if location[2] is False and (
                                    gripper[0] is True or gripper[1] is True) and kit_complete is False:
                                location = mov_to_tray(location)  # Calling function mov_to_tray

                                # Checking all preconditions required to PLACE
                                if location[2] is True and (
                                        gripper[0] is True or gripper[1] is True) and kit_complete is False:
                                    gripper, current_tray = place(gripper, current_tray, j, single)  # Called place()

                    f = 0
                    for k in range(len(current_tray)):  # Checking if kit is completed or not
                        if current_tray[k] == final_tray[k]:
                            f = f + 1

                    if f == 3:
                        kit_complete = True  # If kit is completed then turn kit complete flag true

        print("-------------------")

        # Printing current parts in tray and bins
        for p in range(len(part_bins)):
            if p == 0:
                print(f"current tray RED parts: {current_tray[p]} and RED parts remaining in bin {part_bins[p]}")
            elif p == 1:
                print(f"current tray GREEN parts: {current_tray[p]} and GREEN parts remaining in bin {part_bins[p]}")
            elif p == 2:
                print(f"current tray BLUE parts: {current_tray[p]} and BLUE parts remaining in bin {part_bins[p]}")

        print(" PLAN GENERATED")

    elif c == 3:
        print("kit is already complete")
