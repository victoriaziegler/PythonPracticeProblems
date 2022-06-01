# Planning

## Research

* [ ] Vocab
* [ ] Functions
* [ ] Methods

## Problem decomposition

* [ ] Input
* [ ] Output
* [ ] Examples
* [ ] Conditions (if)
* [ ] Iteration (loop)

## Problems

### 01 minimum_value
    * [ ] define function with 2 variables
    * [ ] compare two values to see which is lesser
    * [ ] return the lesser of the two, or either if they are equal
        * [ ] if statements
            - if value1 <= value2
            - return value1
            - otherwise return value2

# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

### 04 max_of_three
    * [ ] define function with 3 variables
    * [ ] compare to see which is the greatest
    * [ ] return the greater of the three, or any one if they are equal
        * [ ] if statements
            - if value1 > value2 and value3 
                -return value1
            - if value2 > value1 and value3 
                -return value2
            - if value3 > value1 and value2
                -return value 3


### 06 can_skydive  
    * [ ] define function with 2 variables 
    * [ ] conditions: if person is >= 18 yo OR if they have signed consent form then they can skydive
        - if statements
            -if age >= 18 OR has_consent_form = True
                -return ("you can skydive")
            -else return ("you cannot skydive")

### 09 is_palindrome
    * [ ] define function with 1 variable
    * [ ] condition: if word is palindrome, it is the same reversed
        - to get a palindrome:
            -you have to first make the word into a list
            -then get the reverse of that list using reverse(list)
            -then join the reversed list back into a word using ''.join(reverse_word_list)
            -then compare if the new word == original word


### 010 is_divisible_by_3
    * [ ] define function with 1 variable
    * [ ] condition: if number is divisible by 3, return "fizz", otherwise return number
        - use % 3 == 0 to test if # divisible by 3
        - if statements
            - if number is divisible by 3
                - return "fizz"
            - else
                -return number

### 011 is_divisible_by_5
    * [ ] define function with 1 variable
    * [ ] condition: if number is divisible by 5, return "buzz", otherwise return number
        - use % 5 == 0 to test if # divisible by 5
            - if statements
                - if number is divisible by 5
                    - return "buzz"
                - else
                    -return number

### 012 fizzbuzz
    * [ ] define function with 1 variable
    * [ ] conditions: 
        1. if number is divisible by 3 AND 5, return "fizzbuzz"
        2. if number is only divisible by 3, return "fizz"
        3. if number is only divisible by 5, return "buzz"
    - use % 5 == 0 and % 3 == 0
        - if statements:
            - if number is divisible by 3
                - return "fizz"
            - if number is divisible by 5
                - return "buzz"
            - if number is divisible by 3 AND 5
                - return "fizzbuzz"

### 014 can_make_pasta
    * [ ] define function with 1 variable
    * [ ] conditions:
        - need a for loop because sorting through a list
        - if list contains flour, eggs, AND oil
            - return True
        - otherwise return False

### 016 is_inside_bounds
    * [ ] define function with 2 variables
    * [ ] conditions:
        - check if both x and y variables are between 0 and 10
        - if statements:
            - range(0,10)
            if x in range AND y in range:

### 019 is_inside_bounds2
    * [ ] define function with 6 variables
    * [ ] condition:
        - if (x >= rect_x) AND (y >= rect_y) AND (x <= rect_x + rect_width) AND (y <= rect_y + rect_height)
            - must condense - too long of if statement
            - combine into a range since rect_x + rect_width >= x >= rect_x
                - same for y
            - return True
        - otherwise False

### 020 has_quorum
    * [ ] define function with 2 variables (lists)
    * [ ] conditions:
        - will need if statement:
            - if len(attendees list) >= 1/2 len(members_list)

### 022 gear_for_day ***UNFINISHED*** NOT YET TESTED
    * [ ] define function with 2 variables
    * [ ] conditions:
        - returns a list of gear needed for 3 different days
        - if day == workday AND day != sunny
            - list must include umbrella and laptop
        - if day == workday
            - list must include laptop
        - day != worday
            - list must include surfboard

### 024  calculate_average
    * [ ] define function with 1 variable
    * [ ] reads a list of #s and returns average
    * [ ] conditions:
        - number_items = len(values)
        - if list = empty
            return None
        - set sum = 0
        - for value in values
            - sum = sum + value
        - return(sum/number_items)

### 025 calculate_sum
    * [ ] define function with 1 variable
    * [ ] accepts list of #s and returns sum
    * [ ] conditions:
        - if list = empty
            return None
        - set sum = 0
        - for value in values:
            - sum = sum + value
        - return sum

### 026 calculate_grade
    * [ ] define function with 1 variable
    * [ ] accepts list of scores between 0 and 100
    * [ ] find average and return respective score letter
    * [ ] conditions:
        1. average >= 90
            return A
        2. average >= 80
            return B
        3. average >= 70
            return C
        4. average >= 60
            return D
        5. else
            return F


### 027 max_in_list
    * [ ] 

### 028 remove_duplicate_letters
    * [ ]

### 030 find_second_largest
    if len(list) == 0 or len(list) == 1, return None
    *** Use sorted fx to sort list in numerical order ***
    - for loop:
        - create new sorted list (new_list = sorted(list))
    - return new_list at index 1 (second place)


### 031 sum_of_squares
    conditions:
        - for loop because we need to go over each number
            - first square each number
            - then add all squared numbers together



