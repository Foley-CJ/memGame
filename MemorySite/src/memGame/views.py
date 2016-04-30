from django.shortcuts import render
from memGame.dataETLS2 import *
import json 


def shapeDisplay(request):
	#current setup works!

	#pull in the current Data
	dataMaster = request.session["dataMaster"]

	#update the data
	updatedDataMaster = dataAppender(dataMaster)

	#extract the current level and current shape 
	currLevel, currShapes = levelShape(updatedDataMaster)

	#push data to json for template
	jsonLevel = json.dumps(currLevel)
	jsonShapes = json.dumps(currShapes)

	#convert full dataset into unicdoe for request session
	updatedDataMaster = unicodeEncoder(updatedDataMaster)

	#store the data in the session
	request.session["dataMaster"] = updatedDataMaster

	return render(request, "../game/new_display_3.html",{'level':jsonLevel, 'shapes':jsonShapes})





def question(request):
	currDataMaster = request.session["dataMaster"]

	question, correctAnswer = questionChoice(currDataMaster)

	if (correctAnswer == 'True'):
		theTrueUrl = '/memorize'
		theFalseUrl = '/gameOver'
	else:
		theTrueUrl = '/gameOver'
		theFalseUrl = '/memorize'

	return render(request, "../game/question2.html", {'question':question, 'answer':correctAnswer, 'trueUrl':theTrueUrl, 'falseUrl':theFalseUrl})



def gameOver(request):
	#pull in the current Data
	dataMaster = request.session["dataMaster"]

	#extract the current level and current shape 
	currLevel, currShapes = levelShape(dataMaster)

	print currLevel
	
	try:
	 	currBest = request.session["maxLevel"]
	except:
		currBest = 0

	#update Best Score
	newBest = max(int(currLevel), int(currBest))
	request.session["maxLevel"] = newBest

	#clear the baseData
	dataMaster = []
	request.session["dataMaster"] = dataMaster

	return render(request, "../game/endGame.html", {'level': currLevel, 'best':newBest})
