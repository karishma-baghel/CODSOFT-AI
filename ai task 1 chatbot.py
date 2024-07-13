import re

Data={
    "hi": "Hello! What can I do for you?",
    "how are you":"I'm a bot, so I don't have feelings, but thanks for asking!",
    "what is your favourate color":"thanks for asking ,but i have not any personal choice",
    "what's your name": "I'm a chatbot created to assist you.",
    "What can you do?":" i can answer questions and provide information",
    "can you tell me capital of india":"yes!capital of india is 'New Delhi'[https://en.wikipedia.org/wiki/New_Delhi]",
    "what is your purpose": "My purpose is to assist users with information and tasks, while providing a fun and engaging experience.",
    "can you tell me a joke": "Here's a joke for you: Why was the math book sad? Because it had too many problems and for joke link[https://youtu.be/px4DnaCcTyg?si=km9K7FLXbR3MrfDI].",
    "what is the weather like today": "I'm not able to access real-time weather information, but I can suggest some ways for you to find out the current weather in your area.",
    "can you recommend a restaurant near me": "I'd be happy to help! Can you please provide me with your location so I can recommend some restaurants near you?",
    "i'm feeling sad": "Sorry to hear that you're feeling sad. Would you like to talk about what's on your mind or would you like me to try and cheer you up with a joke or a fun fact?",
    "can you summarize the latest news for me": "I'd be happy to summarize the latest news for you. Please let me know what topics you're interested in, such as politics[https://timesofindia.indiatimes.com/politics/news], sports[https://www.msn.com/en-in/sports?ocid=msedgntphdr&cvid=1084b358c8834c11b8326cc2f2939140], or entertainment[https://www.bing.com/news/search?q=entertainment+news&FORM=HDRSC7].",
    "can you help me with my math homework": "I'd be happy to help with your math homework. What type of math are you working on and what specific problem are you stuck on?,you did with this link[https://www.doubtnut.com/search]",
    "can you translate 'hello' into spanish": "The translation of 'hello' in Spanish is 'hola'.",
    "can you give me a recipe for chocolate cake": "Here's a simple recipe for chocolate cake: [https://youtu.be/J7bjH5IdMjc?si=ZMjSogOUuJ0U6QfP]. I hope you enjoy it!",
    "can you suggest a gift for my friend's birthday": "I'd be happy to help you find a gift for your friend's birthday. Can you please provide me with some more information about your friend, such as their interests and hobbies?",
    "can you have friends": " As,a chatbot,I don't have personal relationships or emotions, but I'm designed to be friendly and assistive! I'm here to help you with any questions or tasks, and I'm always happy to chat and learn more about you.",
    "default": "I'm sorry, I don't understand that. Can you please rephrase?"

}


 # Function to match user input with the rules
def get_response(user_input):
       
      
        
# Check for each rule keyword in user input

    for keyword, response in Data.items():
        if re.search(keyword, user_input):
            return response
    return Data["default"]
# Simulate a chat loop

print("Chatbot: Hello! I'm here to chat with you. Type 'bye' to end the conversation.")
while True:
    user_input=input("you: ")
    if(user_input=="bye"):
        print("have a nice day")
        break
    response = get_response(user_input)
    print("Chatbot: " + response)

  
