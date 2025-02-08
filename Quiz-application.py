# QUESTIONS = [
#     ("When was the first known use of the word 'quiz'", "1781"),
#     ("Which built-in function can get information from the user", "input"),
#     ("Which keyword do you use to loop over a given list of elements", "for")
# ]

# SCORE = 0

# for question,answer in QUESTIONS:
#     user_input = input(f'{question}? ,  ')
#     if user_input == answer:
#         SCORE+=1
#         print("Correct")
#     else :
#         print("Not correct")
        
# print("Total scores- ",SCORE)

QUESTIONS = {
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
}


for question, alternative in QUESTIONS.items():
    
    print(f"{question}?" )
    correct_answer = alternative[0]
    
    sorted_alternative = sorted(alternative)
    
    for idx, answer in enumerate(sorted_alternative, start=1):
        print(f"{idx}) {answer} ")
        
    user_input = int(input("Choice? - "))
    
    answer = sorted_alternative[user_input-1]
    
    if answer == correct_answer:
        print("⭐ Correct ⭐")

    else: 
        print(f"The answer is {correct_answer}, not {answer}")
        
    