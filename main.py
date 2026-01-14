# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import json
import random
import os

def load_questions(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def run_exam():
    questions_file = 'questions.json'
    if not os.path.exists(questions_file):
        print(f"Error: {questions_file} not found.")
        return

    all_questions = load_questions(questions_file)
    total_available = len(all_questions)

    print("=" * 50)
    print("  PALO ALTO NETWORKS NGFW EXAM SIMULATION")
    print("=" * 50)
    print(f"Total questions in database: {total_available}")
    print("\nSelect Exam Mode:")
    print("1. Group 1 (Questions 1-60)")
    print("2. Group 2 (Questions 61-120)")
    print("3. Group 3 (Questions 121-180)")
    print("4. Group 4 (Questions 181-240)")
    print("5. Group 5 (Questions 241-300)")
    print("6. Random 60 Questions")
    print("7. All Questions (Marathon Mode)")
    
    choice = input("\nEnter your choice (1-7): ").strip()
    
    if choice == '1':
        questions = all_questions[0:60]
    elif choice == '2':
        questions = all_questions[60:120]
    elif choice == '3':
        questions = all_questions[120:180]
    elif choice == '4':
        questions = all_questions[180:240]
    elif choice == '5':
        questions = all_questions[240:300]
    elif choice == '6':
        questions = random.sample(all_questions, min(60, total_available))
    elif choice == '7':
        questions = all_questions
        random.shuffle(questions)
    else:
        print("Invalid choice. Defaulting to Random 60.")
        questions = random.sample(all_questions, min(60, total_available))

    score = 0
    total = len(questions)
    wrong_answers = []

    if total == 0:
        print("No questions found for the selected mode.")
        return

    print("\n" + "=" * 50)
    print(f"Starting Exam with {total} questions.")
    print("Type your answer (a, b, c, or d) and press Enter.")
    print("=" * 50)

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total}: [{q['domain']}]")
        print(q['question'])
        for key, value in q['options'].items():
            print(f"  {key}) {value}")
        
        user_answer = input("\nYour answer: ").strip().lower()
        
        if user_answer == q['answer'].lower():
            print("CORRECT! ✅")
            score += 1
        else:
            print(f"INCORRECT ❌. The correct answer was: {q['answer']}")
            wrong_answers.append({
                'question': q['question'],
                'user_answer': user_answer,
                'correct_answer': q['answer'],
                'explanation': q['explanation'],
                'options': q['options']
            })
        
        print(f"Explanation: {q['explanation']}")
        print("-" * 30)

    print("\n" + "=" * 50)
    print(f"EXAM FINISHED!")
    print(f"Your Score: {score}/{total} ({ (score/total)*100:.2f}%)")
    
    if (score/total) >= 0.7:
        print("Result: PASS! 🎓")
    else:
        print("Result: FAIL. Keep studying! 📚")
    
    if wrong_answers:
        print("\n" + "=" * 50)
        print("REVIEW WRONG ANSWERS")
        print("=" * 50)
        for i, wa in enumerate(wrong_answers, 1):
            print(f"\n{i}. {wa['question']}")
            print(f"   Your answer: {wa['user_answer']} ({wa['options'].get(wa['user_answer'], 'Invalid')})")
            print(f"   Correct answer: {wa['correct_answer']} ({wa['options'].get(wa['correct_answer'])})")
            print(f"   Explanation: {wa['explanation']}")
    
    print("=" * 50)

if __name__ == '__main__':
    run_exam()
