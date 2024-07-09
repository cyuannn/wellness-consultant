import datetime
import time

class WellnessConsultant:
    def __init__(self, weight, age, height, physical_goal, mental_goal, emotional_goal):
        self.weight = weight
        self.age = age
        self.height = height
        self.physical_goal = physical_goal
        self.mental_goal = mental_goal
        self.emotional_goal = emotional_goal

    def calculate_water_intake(self):
        # General guideline: 35 ml of water per kg of body weight
        return self.weight * 35 / 1000  # returns liters

    def calculate_protein_intake(self):
        if self.physical_goal == "build muscle":
            return self.weight * 1.6  # 1.6 grams of protein per kg
        elif self.physical_goal == "lose weight":
            return self.weight * 1.2  # 1.2 grams of protein per kg
        else:
            return self.weight * 1.0  # 1 gram of protein per kg for maintenance

    def workout_plan(self):
        if self.physical_goal == "build muscle":
            return "Strength training 4-5 times a week"
        elif self.physical_goal == "lose weight":
            return "Cardio 3-4 times a week and strength training 2-3 times a week"
        else:
            return "Mixed workout 3-4 times a week"

    def mental_wellness_tips(self):
        if self.mental_goal == "reduce stress":
            return "Practice meditation or yoga daily"
        elif self.mental_goal == "increase focus":
            return "Do brain exercises like puzzles and reading"
        else:
            return "Maintain a balanced work-life schedule"

    def emotional_wellness_tips(self):
        if self.emotional_goal == "enhance mood":
            return "Engage in activities you enjoy and socialize"
        elif self.emotional_goal == "reduce anxiety":
            return "Practice deep breathing and mindfulness"
        else:
            return "Keep a gratitude journal"

    def daily_update(self):
        water_intake = self.calculate_water_intake()
        protein_intake = self.calculate_protein_intake()
        workout = self.workout_plan()
        mental_tips = self.mental_wellness_tips()
        emotional_tips = self.emotional_wellness_tips()

        update_message = (f"Good morning! Here's your wellness plan for today:\n"
                          f"- Drink at least {water_intake:.2f} liters of water\n"
                          f"- Eat {protein_intake:.2f} grams of protein\n"
                          f"- Workout: {workout}\n"
                          f"- Mental wellness tip: {mental_tips}\n"
                          f"- Emotional wellness tip: {emotional_tips}\n")
        return update_message

    def send_notification(self, message):
        print(message)  # In real use, this would send a notification via some method (email, app, etc.)

def get_user_input():
    weight = float(input("Enter your weight (in kg): "))
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (in cm): "))
    physical_goal = input("Enter your physical goal (lose weight, build muscle, maintain): ").lower()
    mental_goal = input("Enter your mental goal (reduce stress, increase focus, maintain balance): ").lower()
    emotional_goal = input("Enter your emotional goal (enhance mood, reduce anxiety, maintain balance): ").lower()
    
    return weight, age, height, physical_goal, mental_goal, emotional_goal

def main():
    weight, age, height, physical_goal, mental_goal, emotional_goal = get_user_input()
    consultant = WellnessConsultant(weight, age, height, physical_goal, mental_goal, emotional_goal)

    while True:
        daily_message = consultant.daily_update()
        consultant.send_notification(daily_message)
        time.sleep(86400)  # Waits for 24 hours before sending the next update

if __name__ == "__main__":
    main()
