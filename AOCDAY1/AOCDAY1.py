# # PART 1
# # //////////////////////////////////////

# open mass file
f = open('AOCDAY1.txt', 'r')
# create mass list
mass_list = []
for i in f.readlines():
    mass_list.append(int(i))

# fuel calculations
def fuel_calculation(mass_list_var):
    fuel_list = []
    for mass in mass_list_var:
        fuel = (mass/3)-2
        fuel_list.append(fuel)
    return fuel_list

def main1():
    fuel_needed_list = fuel_calculation(mass_list)
    fuel_needed = sum(fuel_needed_list)
    # display result
    return fuel_needed


# print(main1())


# # PART 2
# # //////////////////////////////////////

def main2():
    # get fuel mass of each module from part 1
    fuel_needed_list = fuel_calculation(mass_list)
    # create list for calculations
    excess_fuel_mass_list = []
    # calculate fuel mass until mass is none for each module
    for fuel_mass in fuel_needed_list:
        module_fuel_mass_list = []
        # while loop to calculate to none
        while fuel_mass > 0:
            module_fuel_mass_list.append(fuel_mass)
            # fuel calculation
            fuel_mass = (fuel_mass/3)-2
        # append the total mass of the module and all fuel needed to the excess fuel mass list
        excess_fuel_mass_list.append(sum(module_fuel_mass_list))
        # sum the list
    new_mass_total = sum(excess_fuel_mass_list)
    new_fuel_total = new_mass_total
    return new_fuel_total

print(main2())
