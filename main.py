#!/usr/bin/env python3
import openai
import os
from getpass import getpass

score = 0


subj = input('''

SUBJECT

Type the subject under here,
e.g.,
History
English
Math
Biology
Chemistry
Reading

>>''')

openai.organization = "org-NFYrq8pSxUlmdAcuuKh8diXY"
openai.api_key = getpass("Enter the OpenAI Key here. Members of Shrewsbury International School get this for free.")
openai.Model.list()

def printe(text): return text

def GPT_Completion(texts):## Call the API key under your account (in a secure way)
#openai.api_key = "your API key"
	response = openai.Completion.create(engine="text-davinci-002",
	prompt =  texts,
	temperature = 0.8,
	top_p = 1,
	max_tokens = 64,
	frequency_penalty = 0,
	presence_penalty = 0)
	return printe(response.choices[0].text)

lvl = int(input("What level would you consider yourself in? 1 (super easy) to 12 (SUPER DUPER hard) >>"))
while True:
	question = GPT_Completion(f"""
Please give a random question for a person in grade {lvl}? Make sure the subject is {subj}, and make sure there's only one answer.

""")
	
	remarks = ''
	if 'math' in subj.lower():
		remarks = 'Make sure the answer is in number form if it doesn\'t specify that it shouldn\'t be.'
	answer = GPT_Completion(f'''

Please can you answer this question? {remarks}

{question}


''')
	print(f"Score: {score}")
	scoreminus = lvl ** 2
	if 'math' in subj.lower():
		answer=answer.replace(' ','').lower()
		try:
			float(answer)
		except:
			print("You can get this one wrong btw!")
			scoreminus = 0
	answer= answer.replace(chr(10),'')
	print(question)
	if input("Answer >>") == answer:
		print("Correct!")
		score += lvl ** 2
	else:
		print("Wrong!")
		score -= scoreminus
