def minmax():
    nums = []  
    while True:
        num = input("Enter a number (-1 to terminate): ")
        if num == '-1':
            break
        nums.append(int(num))

    if not nums:
        print("No numbers entered.")
    else:
        maximum = max(nums)
        minimum = min(nums)
        print("Largest number:",  maximum)
        print("Smallest number:", minimum)

minmax()
