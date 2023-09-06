from wod import Workout
import time
import requests
import random
import os

'''Main function that displays main menu and asks user for input'''''
def main():
    
    workout = Workout("info.json")
    workout.exercises = workout.load_exercises()
    clear()
    main_menu()
    while True:
        chosen_category = input("\033[36mWhich type of the workout would you like to get?\033[0m ")
        clear()
        if chosen_category.lower() in ["upper body", "lower body", "full body"]:
            workout.display_workout(chosen_category)
            image_answer = input("\nWould you like to save your workout as an image? (yes/no) ")
            if image_answer.lower() == "yes":
                workout.save_workout(chosen_category)
                clear()
                print("🌟Your workout has been saved as an image!🌟")
            else:
                print("Ok, no problem!")  
            break
        elif chosen_category.lower() == "wod":
            wod_description = workout.get_wod(chosen_category)
            print('\033[34m' + wod_description+ '\033[0m')
            save_wod_answer = input("\nWould you like to save your WOD as an image? (yes/no) ")
            if save_wod_answer.lower() == "yes":
                workout.save_wod(wod_description, output_image_path='wod.png')
                clear()
                print("🌟Your WOD has been saved as an image!🌟")
            else:
                print("Ok, no problem!")  
            break
        else:
            print("This category is not found. Please choose between UPPER BODY, LOWER BODY, FULL BODY, or WOD!")        
    
                 
    user_answer = input("\nWhen you are done with your workout provide some stretching exercises. Would you like to get the example of the streching exercises? (yes/no) ")
    clear()
    if user_answer.lower() == "yes":
        get_streching_exercises()
        print("\n\033[33mHave a nice day and enjoy our workout!\033[0m\n")
    else:
        print("\n\033[33mHave a nice day and enjoy our workout!\033[0m\n")
        
    
'''Function that gets streching exercises from api'''  
def get_streching_exercises():
    type = 'stretching'
    api_url = 'https://api.api-ninjas.com/v1/exercises?type={}'.format(type)
    response = requests.get(api_url, headers={'X-Api-Key': 'Tnfq58nczmtcqvtPKgkdsQ==o9PUVZvWmRWWljjS'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        exercise_names = [exercise['name'] for exercise in data]
        exercises_description = [exercise['instructions'] for exercise in data]
        random_exercise = random.sample(range(len(exercise_names)), 4)
        for i, index in enumerate(random_exercise,start=1):
            print(f"\033[36m{i}. {exercise_names[index]}\033[0m")
        print("\nDescriptions:\n")    
        for i, index in enumerate(random_exercise,start=1):
            print(f"{i}. {exercises_description[index]}")    
    else:
        print("Error:", response.status_code, response.text)   
        
'''Function that displays main menu'''       
def main_menu():
    typing("\033[36mHello fitness enthusiast! Welcome to the Workout Generator! 🏋️‍♂️  💪 ")
    typing("Whether you are a beginner or a seasoned fitness enthusiast, we have a workout for you!\033[0m\n")
    typing("MAIN MENU: \n") 
    typing("1. UPPER BODY")
    typing("2. LOWER BODY")
    typing("3. FULL BODY")
    typing("4. WOD(your weekly challenge)\n")
    
'''Function that clears the screen'''   

def clear():
   os.system('cls' if os.name == 'nt' else 'clear')
   
'''Function that types text with delay'''   
def typing(text, delay = 0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()            
if __name__ == '__main__':
    main()    
    