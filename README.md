# Pretrained NPL model based chatbot using Python

## Packages used
- Speech Recognition
- PyTorch
- Pyttsx3
- Transformers

## Project requirements
- Python 3.7-3.9 (Pytorch limitation)

## Installation Process


First clone this git repository or download zip
```html
  git clone https://github.com/shz-code/chatbot.git
```
Create a new virtual environment(Use Conda/ Virtual Environment) [Learn More.](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20created,the%20virtual%20environment%20are%20available.)

**If virtual environment is not installed on your machine install it using below command.*
```py
  pip install virtualenv
```
Activate **virtualenv**
```py
   virtualenv env
  .\env\Scripts\activate  
```
Run pip to install all the dependencies
```py
  pip install -r requirements.txt
```
Start main.py

```py
  py main.py
```

## Features
- Users can chat or speak with the bot.
- The bot can generate answers based on pre-defined conditions or it will generate answer from *NLP* model.
- **microsoft/DialoGPT-medium** used as pre-trained model. Change the model name and *task* (in this project *conversational*) to add other pre-trained models. Visit [Hugging Face](https://huggingface.co/models) to know more.



## Acknowledgements

 - Main article [Complete Guide to build your AI Chatbot with NLP in Python.](https://www.analyticsvidhya.com/blog/2021/10/complete-guide-to-build-your-ai-chatbot-with-nlp-in-python/)

