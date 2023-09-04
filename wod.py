from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import random
import json
class Exercise:
    '''Exercise class with name, category, description, and link to video
    '''
    def __init__(self, name, category, description, link):
        self.name = name
        self.category = category
        self.description = description
        self.link = link
        
    '''Getters and setters for name, type, description, and link'''
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        self._category = value
        
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def link(self):
        return self._link
    @link.setter
    def link(self, value):
        self._link = value     

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.category, self.description, self.link)
    
class Workout:
    '''Workout class with list of exercises and categories
    '''
    def __init__(self, file_name, categories = ["upper body", "lower body", "full body", "wod"]):
        self.categories = categories
        self.file_name = file_name
        self.exercises = []
        
    '''Load exercises from json file'''
    
    def load_exercises(self):
        exersises = []
        with open(self.file_name) as f:
            data = json.load(f)
            for exercise in data['exercises']:
                exersise = Exercise(exercise["exercise_name"], exercise["exercise_type"], exercise["exercise_description"], exercise["exercise_video"])
                exersises.append(exersise)
            return exersises
    '''Generate random workout'''
    def generate_random_workout(self, choicen_category, num_exercises = 4):
        if choicen_category.lower() not in self.categories:
            raise ValueError("Category {} is not found".format(choicen_category))
        chosen_exercises = [exercise for exercise in self.exercises if exercise.category.lower() == choicen_category.lower()]
        random.shuffle(chosen_exercises)
        selected_exercises = chosen_exercises[:num_exercises]
        return selected_exercises
    
    '''Display workout with description and video link'''
    def display_workout(self,chosen_category,num_rounds = 3, break_time = 2):
        random_workout = self.generate_random_workout(chosen_category)
        print("\nYour WORKOUT for today is {}.\n".format(chosen_category.upper()))
        print("Provide {} rounds of each exercise with {} minutes break between rounds.".format(num_rounds, break_time))
        print("For exercise where you have to use weight, take a weight that you can do 10 reps with per set.\n")
        cyan_color = '\033[36m'
        reset_color = '\033[0m'
        for index, exercise in enumerate(random_workout, start = 1):
            print(f"{cyan_color}{index}. {exercise.name}{reset_color}")
        print("\nDescriprion for each exercise: \n")
        yellow_color = '\033[33m'
        reset_color = '\033[0m'
        for index, exercise in enumerate(random_workout, start = 1):
            print("{}{}. {}{}".format(yellow_color, index, exercise.description, reset_color))
        print("\nCheck the links below if needed to perform the correct technique for each exercise: \n")
        for index, exercise in enumerate(random_workout, start = 1):
            print(f"{index}. {exercise.link}")
                
                
    '''Get wod from txt file'''
    def get_wod(self, chosen_category):
        if chosen_category.lower() not in self.categories:
            raise ValueError("Category {} is not found".format(chosen_category))
        with open("wods.txt", "r") as f:
            wod_data = f.read().split('|')
            random_wod = random.choice(wod_data)
            print('\033[34m' + random_wod.upper() + '\033[0m')
            
    '''save workout as image'''
    def save_workout(self,chosen_category, output_image_path='workout.png'):
        random_workout = self.generate_random_workout(chosen_category)
        image_width, image_hight = 600,800
        background_color = (64,64,64)
        image = Image.new('RGB', (image_width, image_hight), background_color)
        draw= ImageDraw.Draw(image)
        font= ImageFont.load_default()
        font_size = 15
        text_position = (30,30)
        text_color = (255,255,255)
        
        workout_info=  f"Your WORKOUT for today is {chosen_category.upper()}.\n\n"
        workout_info += "Provide 3 rounds of each exercise with 2 minutes break between rounds.\n"
        workout_info += "For exercise where you have to use weight, take a weight that you can do 10 reps with per set.\n\n"
        
        for index, exercise in enumerate(random_workout, start = 1):
            workout_info += f"{index}. {exercise.name}\n"
        workout_info += "\nDescriprion for each exercise: \n\n"
        #wrap long lones of descriptions to fit within the image boundaries
        max_line_length = 90
        for index, exercise in enumerate(random_workout, start = 1):
            wrapped_lines = textwrap.wrap(exercise.description, width=max_line_length)
            formated_description = "\n".join(wrapped_lines)
            workout_info += f"{index}. {formated_description}\n"
        workout_info += "\nCheck the links below if needed to perform the correct technique for each exercise: \n\n"
        for index, exercise in enumerate(random_workout, start = 1):
            workout_info += f"{index}. {exercise.link}\n"
        lines = workout_info.strip().split('\n')
        for line in lines:
            draw.text(text_position, line, font=font, fill=text_color)
            text_position = (text_position[0], text_position[1] + font_size)
        image.save(output_image_path)
    
       
        
        
    
        
    