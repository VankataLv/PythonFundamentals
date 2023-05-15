list_soldiers = input().split(" ")
counter = int(input()) - 1                                     # IOT convert from soldiers to list indexes
initial_length_list = len(list_soldiers)
executed_order = list()
current_executed_index = 0

for execution_iteration in range(initial_length_list + 1):
    if counter > len(list_soldiers):                               # in case counter has more elements than soldiers
        counter -= len(list_soldiers)

    executed_order.append(list_soldiers[counter])             # store executed soldier in execution list
    list_soldiers.remove(list_soldiers[counter])              # remove executed soldier from soldier alive list
    counter += counter                                        # store the index location for next iteration

