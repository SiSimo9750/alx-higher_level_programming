#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    for i in range(list_length):
        try:
            rsult = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            rsult = 0
        except ZeroDivisionError:
            print("division by 0")
            rsult = 0
        except IndexError:
            print("out of range")
            rsult = 0
        finally:
            my_new_list.append(rsult)
    return (my_new_list)
