class ChatBot:
    def __init__(self):
        self.responses = {}

    def teach(self, question, response):
        self.responses[question] = response

    def respond_to(self, input_message):
        for question, response in self.responses.items():
            if question in input_message:
                return response
        return "Não entendi o que você quer dizer. Você gostaria de ensinar-me uma resposta para esta pergunta?"

    def chat(self):
        while True:
            user_input = input("Você: ")
            if user_input == "exit":
                break
            response = self.respond_to(user_input)
            if "Você gostaria de ensinar-me uma resposta para esta pergunta?" in response:
                question = user_input
                new_response = input("Digite a resposta que eu devo aprender: ")
                self.teach(question, new_response)
                print("Aprendi uma nova resposta!")
            else:
                print("ChatBot: ", response)

chatbot = ChatBot()
chatbot.teach("Olá", "Olá! Em que posso ajudá-lo hoje?")
chatbot.teach("Como você está?", "Estou bem, obrigado por perguntar. E você?")
chatbot.teach("Adeus", "Até mais tarde! Tenha um bom dia.")

chatbot.chat()
