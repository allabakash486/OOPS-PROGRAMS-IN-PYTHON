class swiggy:
    print("Welcome to swiggy ....")
    def Order(slef):
        print('Order please !.....')
        print('Venue is here \n 1) Biryani \n 2)DOsa \n 3) Anna sambar')
        value = int(input('Enter number'))
        if value == 1:
            print(f'biryani is order successfully !....')
        elif value ==2:
            print(f'Dosa is order successfully !....')
        elif value ==3:
            print(f'Anna Sambar is order successfully !....')
Customer1 = swiggy()
Customer1.Order()
    