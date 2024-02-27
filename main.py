import datetime
import pickle
import os


class FlashBackMemory:
    def __init__(self):
        self.users_data = {}

    def load_data(self):
        if os.path.exists('flashback_memory_data.pkl'):
            with open('flashback_memory_data.pkl', 'rb') as file:
                self.users_data = pickle.load(file)

    def save_data(self):
        with open('flashback_memory_data.pkl', 'wb') as file:
            pickle.dump(self.users_data, file)

    def user_check_in(self, user_id):
        today = datetime.date.today()

        if user_id not in self.users_data:
            self.users_data[user_id] = {'streak': 0, 'daily_check_ins': {}}

        if today not in self.users_data[user_id]['daily_check_ins']:
            self.users_data[user_id]['daily_check_ins'][today] = {'topics': []}
            self.users_data[user_id]['streak'] += 1
        else:
            print("You have already checked in today. Try again tomorrow.")
            return

        print(f"\nDaily Check-in - Streak: {self.users_data[user_id]['streak']}")
        topic = input("What did you learn today? Enter the topic: ")
        self.users_data[user_id]['daily_check_ins'][today]['topics'].append(topic)
        self.save_data()
        information= input("What did you learn about this topic?")

        print("Check-in successful!")

    def show_weekly_rewards(self, user_id):
        streak = self.users_data[user_id]['streak']
        if streak >= 7:
            print("Congratulations! You've completed a week with consistent daily check-ins.")
            print("You've earned a special reward!")

    def main_menu(self):
        user_id = input("Enter your user ID: ")
        self.load_data()

        while True:
            print("\nFlashBack Memory - Main Menu")
            print("1. Daily Check-In")
            print("2. Show Weekly Rewards")
            print("3. Exit")

            choice = input("Select an option (1/2/3): ")

            if choice == '1':
                self.user_check_in(user_id)
            elif choice == '2':
                self.show_weekly_rewards(user_id)
            elif choice == '3':
                self.save_data()
                print("Exiting FlashBack Memory. See you later!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    flashback_memory = FlashBackMemory()
    flashback_memory.main_menu()
