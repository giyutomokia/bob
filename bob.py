# Install necessary libraries
# pip install chatterbot
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class LoanChatbot:
    def __init__(self):
        # Create a chatbot instance
        self.chatbot = ChatBot('LoanChatbot')

        # Create a new trainer for the chatbot
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)

        # Train the chatbot on English language corpus data
        self.trainer.train('chatterbot.corpus.english')

    def ask_demographic_details(self):
        print("Welcome to the  chatbot!")
        self.user_data = {}
        self.user_data['credit_history'] = input("Do you have a credit history with our bank? (yes/no): ").lower()
        self.user_data['property_value'] = float(input("Enter the value of your property in pounds: "))
        self.user_data['annual_income'] = float(input("Enter your annual income in dollars: "))

    def check_loan_eligibility(self):
        if self.user_data['credit_history'] == 'no' and self.user_data['property_value'] > 100000:
            return "Congratulations! You are eligible for a loan."
        elif self.user_data['credit_history'] == 'yes':
            return "Congratulations! You are eligible for a loan from our bank."
        elif self.user_data['credit_history'] == 'no' and self.user_data['property_value'] == 0 and self.user_data['annual_income'] > 100000:
            return "Congratulations! You are eligible for a loan based on your high annual income."
        else:
            return "Sorry, you are not eligible for a loan at the moment."

    def get_response(self):
        response = self.check_loan_eligibility()
        print("LoanChatbot:", response)

if __name__ == "__main__":
    # Initialize the LoanChatbot
    chatbot = LoanChatbot()

    # Interaction loop
    while True:
        chatbot.ask_demographic_details()
        chatbot.get_response()

        # Break the loop if the user wants to exit
        exit_choice = input("Do you want to exit? (yes/no): ").lower()
        if exit_choice == 'yes':
            break
