# Virtusa Jatayu - AI Conversational Bot - Health Talkie - AiQuantix
Hey Virtusa Jatayu experts, 
Here we are with a super supportive AI Conversational Bot named "Health Talkie" to extend our 24/7 Services with inbuilt VR.

Hope you will enjoy our product !

Steps to run the program:
1. Train the model:  rasa train
2. rasa run -m models --enable-api --cors "*"
3. Run the action server: rasa run actions --cors "*"


Major Files and their descriptions:
1. index.html - The executable file
2. CSS and JS folder - for frontend of the chatbot and webpage
3. Data folder - For nlu, stories and rules, taht contains the intents
4. Action.py - Python programming for rasa server action
5. Models - The trained models
6. chats.csv - The storage of conversations
7. domain.yml - To indicate the response of chatbot - utter messages
