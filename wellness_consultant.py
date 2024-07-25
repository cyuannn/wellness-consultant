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

    def detailed_workout_plan(self):
        if self.physical_goal == "build muscle":
            return ("**Strength Training Plan:**\n"
                    "1. Monday: Chest and Triceps - Bench Press, Incline Dumbbell Press, Tricep Dips\n"
                    "2. Tuesday: Back and Biceps - Deadlifts, Pull-Ups, Bicep Curls\n"
                    "3. Wednesday: Rest or Light Cardio\n"
                    "4. Thursday: Legs - Squats, Leg Press, Lunges\n"
                    "5. Friday: Shoulders - Overhead Press, Lateral Raises\n"
                    "6. Saturday: Core - Planks, Russian Twists\n"
                    "7. Sunday: Rest\n")
        elif self.physical_goal == "lose weight":
            return ("**Cardio and Strength Training Plan:**\n"
                    "1. Monday: Cardio - 30 minutes running or cycling\n"
                    "2. Tuesday: Strength Training - Full Body Workout\n"
                    "3. Wednesday: Cardio - 30 minutes swimming\n"
                    "4. Thursday: Strength Training - Upper Body Focus\n"
                    "5. Friday: Cardio - 30 minutes HIIT\n"
                    "6. Saturday: Strength Training - Lower Body Focus\n"
                    "7. Sunday: Rest or Light Activity\n")
        else:
            return ("**Mixed Workout Plan:**\n"
                    "1. Monday: Full Body Strength Training\n"
                    "2. Tuesday: Cardio - 30 minutes\n"
                    "3. Wednesday: Strength Training - Upper Body\n"
                    "4. Thursday: Cardio - 30 minutes\n"
                    "5. Friday: Strength Training - Lower Body\n"
                    "6. Saturday: Active Recovery - Yoga or Stretching\n"
                    "7. Sunday: Rest\n")

    def detailed_nutrition_plan(self):
        if self.physical_goal == "build muscle":
            return ("**Muscle Building Nutrition Plan:**\n"
                    "1. Breakfast: Scrambled eggs with spinach, whole-grain toast\n"
                    "2. Snack: Greek yogurt with honey and almonds\n"
                    "3. Lunch: Grilled chicken breast, quinoa, mixed vegetables\n"
                    "4. Snack: Protein shake with fruit\n"
                    "5. Dinner: Baked salmon, sweet potatoes, steamed broccoli\n"
                    "6. Post-Workout: Whey protein shake\n")
        elif self.physical_goal == "lose weight":
            return ("**Weight Loss Nutrition Plan:**\n"
                    "1. Breakfast: Oatmeal with berries and chia seeds\n"
                    "2. Snack: Apple slices with peanut butter\n"
                    "3. Lunch: Salad with mixed greens, grilled chicken, and vinaigrette\n"
                    "4. Snack: Carrot sticks with hummus\n"
                    "5. Dinner: Turkey breast, brown rice, and steamed vegetables\n"
                    "6. Hydration: Drink green tea or herbal tea\n")
        else:
            return ("**Maintenance Nutrition Plan:**\n"
                    "1. Breakfast: Smoothie with spinach, banana, and protein powder\n"
                    "2. Snack: Cottage cheese with pineapple\n"
                    "3. Lunch: Turkey sandwich with whole-grain bread and a side salad\n"
                    "4. Snack: Mixed nuts\n"
                    "5. Dinner: Lean beef stir-fry with vegetables and brown rice\n"
                    "6. Hydration: Drink plenty of water throughout the day\n")

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
        workout = self.detailed_workout_plan()
        nutrition = self.detailed_nutrition_plan()
        mental_tips = self.mental_wellness_tips()
        emotional_tips = self.emotional_wellness_tips()

        update_message = (f"Good morning! Here's your wellness plan for today:\n"
                          f"- Drink at least {water_intake:.2f} liters of water\n"
                          f"- Eat {protein_intake:.2f} grams of protein\n"
                          f"- Workout Plan:\n{workout}"
                          f"- Nutrition Plan:\n{nutrition}"
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

