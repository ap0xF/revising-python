import random

random_data = (random.randint(1,11) for _ in iter(int, 1))

stop_iteration_on_ten = 0
for i in random_data:
    if stop_iteration_on_ten < 10:
        print(i)
    stop_iteration_on_ten += 1

