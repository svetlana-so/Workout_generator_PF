import unittest
from wod import Exercise, Workout  
'''Check if the attributes are set correctly'''
class TestExercise(unittest.TestCase):
    def test_exercise_creation(self):
        exercise = Exercise("Push-up", "Upper Body", "Description of push-up", "https://example.com/push-up")
        self.assertEqual(exercise.name, "Push-up")
        self.assertEqual(exercise.category, "Upper Body")
        self.assertEqual(exercise.description, "Description of push-up")
        self.assertEqual(exercise.link, "https://example.com/push-up")
'''Set up a workout instance'''
class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.workout = Workout("test_data.json")
        self.workout.exercises = [
            Exercise("Push-up", "Upper Body", "Description of push-up", "https://example.com/push-up"),
            Exercise("Squat", "Lower Body", "Description of squat", "https://example.com/squat"),
        ]
    '''check if loading exercises works correctly'''
    def test_load_exercises(self):
        exercises = self.workout.load_exercises()
        self.assertEqual(len(exercises), 2)
        self.assertEqual(exercises[0].name, "Push-up")
        self.assertEqual(exercises[1].name, "Squat")
    '''check if a random workout is generated correctly'''
    def test_generate_random_workout(self):
        random_workout = self.workout.generate_random_workout("Upper Body", num_exercises=1)
        self.assertEqual(len(random_workout), 1)
        self.assertEqual(random_workout[0].category, "Upper Body")

if __name__ == '__main__':
    unittest.main()