# Python program for implementation 
# check criteria
def checkcriteria(arr):
    w = 0
    for i in range(0, len(arr), 1):
        # avoid division/modulo by zero: skip index 0
        if i == 0:
            continue

        # perform checks safely
        if i % arr[i] == 0 or arr[i] % i == 0:
            w = w + 1
    if w > 0:
        return 1
    else:
        return 0
    	
# Find combinations 		
def bubbleSort(arr): 
    matches = 1
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1):
            # traverse the array from 0 , n-i-1
            arr[j], arr[j+1] = arr[j+1], arr[j]
            result = checkcriteria(arr)
            if result == 1:
                matches = matches + 1
    return matches
                    
#create an array
def createAnArray(m):
    createdarray = []
    if m > 1 and m < 20:
        for i in range(1, m, 1):
            createdarray.append(i)
    else:
        print("Given number is out of range")
    return createdarray

# Driver code to test above
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # support passing the number as the first CLI argument or via prompt
    if len(argv) >= 1:
        user_input_raw = argv[0]
    else:
        # In some environments (like VS Code/PowerShell) the integrated run command can be
        # prepended to stdin; protect by stripping and validating below.
        user_input_raw = input("Enter a number >1 and <20 to create an array and to find possible arrays condition i%arr[i] == 0 or arr[i]%i == 0 :")

    # robust int conversion
    try:
        # strip possible leading shell command parts (common when run configuration is wrong)
        # attempt to extract the first integer-looking token
        token = user_input_raw.strip().split()[-1]
        userintinput = int(token)
    except Exception as e:
        print(f"Could not parse an integer from input: {user_input_raw!r} -> {e}")
        return 1

    print("Number entered by you is: {}".format(userintinput))
    arr = createAnArray(userintinput)
    print(arr)
    outputvalue = bubbleSort(arr)
    print("matches found are {}".format(outputvalue))
    return 0


if __name__ == '__main__':
    # Allow passing the input via CLI e.g. `python script.py 5`
    sys.exit(main())
