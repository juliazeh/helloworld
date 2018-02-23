
def helloworld(militarytime=None, age=None):
    """
    prints 'good morning', 'good afternoon', or 'good night'
    converts age to dog years
    """

    # print greeting
    if militarytime < 12:
        print("good morning")
    elif 12 < militarytime < 18:
        print("good afternoon")
    elif 18 < militarytime < 24:
        print("good night")

    # print age in dog years
    if age:
        dogyears = age*7
        print("you are {} dog years old".format(dogyears))