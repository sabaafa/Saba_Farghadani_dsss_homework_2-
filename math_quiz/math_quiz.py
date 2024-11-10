import random

def get_random_number(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.
    
    Args:
        min_value (int): The minimum value (inclusive).
        max_value (int): The maximum value (inclusive).
        
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Select a random mathematical operator from the set: +, -, *.
    
    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(number1, number2, operator):
    """
    Create a math problem and calculate its correct answer.
    
    Args:
        number1 (int): The first number.
        number2 (int): The second number.
        operator (str): The mathematical operator.
        
    Returns:
        tuple: A tuple containing the problem as a string and the answer as an int.
    """
    problem_statement = f"{number1} {operator} {number2}"
    
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    else:  # operator == '*'
        correct_answer = number1 * number2
        
    return problem_statement, correct_answer

def math_quiz_game():
    """
    Run a simple math quiz game where the user answers random math problems.
    """
    score = 0  # Initialize score counter
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("Solve the math problems presented and try to get as many correct as possible.")

    for _ in range(total_questions):
        num1 = get_random_number(1, 10)
        num2 = get_random_number(1, 5)
        operator = get_random_operator()

        problem, answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Skip to the next question if input is invalid

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
