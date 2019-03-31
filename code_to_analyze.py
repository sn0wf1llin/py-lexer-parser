if 90 == 9777:
    print("check")

my_var = 200
my_next_var = 0
my_border = 777

if my_var <= 100:
    my_var *= 100
    extra_new_var = 9
    extra_new_var *= 11
    while extra_new_var + my_var < 1000:
        my_next_var += 100

        if my_next_var > my_border:
            break
else:
    my_first_string = "helloworld"
    print("arg1", "arg2", my_var, my_next_var, my_border)

print(my_next_var)