import chatterbot
import chatterbot.trainers


def setup_chatbot():
    # Create a chatbot instance
    chatbot = chatterbot.ChatBot('HelpfulBot',
                                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                                 database_uri='sqlite:///chatterbot.sqlite3'
                                 )

    # Set up the trainer
    trainer = chatterbot.trainers.ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot using the English corpus
    trainer.train('chatterbot.corpus.english')

    return chatbot


def chat():
    print("Hello! I am HelpfulBot. Type something to start a conversation or type 'exit' to leave.")
    chatbot = setup_chatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == '__main__':
    chat()
