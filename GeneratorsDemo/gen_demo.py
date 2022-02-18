# gen_demo.py

# generator function example 
def compute():
    for i in range(10):
        yield i 

# list example
def square_nums(nums):
    result = []
    for num in nums: 
        result.append(num*num)
    return result 

# generator example
def square_nums_generator(nums):
    for num in nums: 
        yield num*num 


if __name__ == "__main__":
    
    # sample list of integer numbers 
    numbers_list = [1, 2, 3, 4, 5]

    squares_list = square_nums(numbers_list)

    print(f"Squares List: \n{squares_list}")

    squares = square_nums_generator(numbers_list)

    print("Squares from Generator:")
    for square in squares:
        print(square)
    