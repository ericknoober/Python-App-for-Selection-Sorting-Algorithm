def selectionSort(arr):
    length = len(arr)
    
    for i in range(length):

        print(f"Pass#{i+1}:")
        #tracks index
        min_index = i
        #tracks value
        min_value = arr[i]
        print(f"Minimum value is:{min_value}")
        
        for j in range(i+1, length):

            #checks if current index is smaller than minimum value
            print(f"Checking if {arr[j]} is smaller than {min_value}.")
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
                print(f"{arr[j]} is smaller, so it is new minimum value.")
            else:
                print(f"{arr[j]} is not smaller, minimum value is still {min_value}.")
        
        #after all elements are checked
        #swap lowest element with unsorted element to the left
        print(f"Swapping {arr[i]} and {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Pass#{i+1} array: {arr[::]}")
    
    return arr

def userInput():
    i = 1
    input_arr = []
    print("Create your array and input -1 to begin sorting.")
    
    while True:
        userValue = input(f"Input value#{i}: ")

        #check if user wants to begin sorting
        if userValue == "-1":
            break

        #convert string to integer
        try:
            num = int(userValue)
            input_arr.append(num)
            i+=1
        except (ValueError):
            print("Enter a valid integer.")
        

    print(selectionSort(input_arr))

userInput()
