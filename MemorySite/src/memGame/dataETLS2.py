# coding: utf-8

# import necessary packages
import random as rd
import pandas as pd


# set Globals
allShapes = ['triangle','square','circle']
allColors = ['yellow','red','blue','green']


#set shape and color chooser.
def selector(options):
    return options[rd.randint(0,len(options)-1)]


def unicodeEncoder(listedData):
    z = pd.DataFrame(listedData)
    z['color'] =z['color'].astype(unicode)
    z['design'] =z['design'].astype(unicode)
    z['level'] =z['level'].astype(int)
    z['position'] =z['position'].astype(int)
    return z.T.to_dict().values()


#use selector to append data onto master.
def dataAppender(dataMaster):
    try: 
        currLevel = max(pd.DataFrame(dataMaster)['level'])+1
    except:
        currLevel = 1
    
    for x in range(currLevel/5+1+(rd.randint(0,1))):
        currShape = selector(allShapes)
        currColor = selector(allColors)
        currentEntry = {'level':currLevel, 'position': (x+1), 
                        'design':currShape , 'color':currColor}
        dataMaster.append(currentEntry)

    return dataMaster


#current level and shape determiner
def levelShape(dataMaster):
    masterFrame = pd.DataFrame(dataMaster)
    currentLevelRaw = masterFrame['level'].max()
    currentShapeRaw = masterFrame.loc[masterFrame['level'] == currentLevelRaw]
    currentLevel = str(currentLevelRaw)
    currentShapes = currentShapeRaw.T.to_dict().values()
    return currentLevel, currentShapes

#question choice driver
def questionChoice(rawData):
    currDataLayer = pd.DataFrame(rawData)
    choice = rd.randint(1,12)
    
    if   (choice==1):question, correctAnswer = question_1a(currDataLayer)
    elif (choice==2):question, correctAnswer = question_1b(currDataLayer)
    elif (choice==3):question, correctAnswer = question_1c(currDataLayer)
    elif (choice==4):question, correctAnswer = question_2a(currDataLayer)
    elif (choice==5):question, correctAnswer = question_2b(currDataLayer)
    elif (choice==6):question, correctAnswer = question_2c(currDataLayer)
    elif (choice==7):question, correctAnswer = question_3a(currDataLayer)
    elif (choice==8):question, correctAnswer = question_3b(currDataLayer)
    elif (choice==9):question, correctAnswer = question_3c(currDataLayer)
    elif (choice==10):question, correctAnswer = question_4a(currDataLayer)
    elif (choice==11):question, correctAnswer = question_4b(currDataLayer)
    elif (choice==12):question, correctAnswer = question_4c(currDataLayer)
    else: print 'questionChoice error'
        
    return question, correctAnswer


#set of 12 different questions
def question_1a(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['color','design']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    shapeSelected = convertRaw.iloc[rowChoice,1]
    colorSelected =  convertRaw.iloc[rowChoice,0]
    number = int(convertRaw.iloc[rowChoice,2]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ colorSelected + ' ' +shapeSelected + "s is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer

def question_1b(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['color']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    colorSelected =  convertRaw.iloc[rowChoice,0]
    number = int(convertRaw.iloc[rowChoice,1]) + rd.choice([1*booler,-1*booler]) 

    question =  "The total number of "+ colorSelected + " shapes is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer


def question_1c(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['design']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    shapeSelected =  convertRaw.iloc[rowChoice,0]
    number = int(convertRaw.iloc[rowChoice,1]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ shapeSelected + "s is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer




def question_2a(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['color','design','level']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    levelSelected = convertRaw['level'][rowChoice]
    shapeSelected = convertRaw['design'][rowChoice]
    colorSelected =  convertRaw['color'][rowChoice]
    number = int(convertRaw[0][rowChoice]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ colorSelected + ' ' +shapeSelected + "s on level "+ str(levelSelected)+ " is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer

def question_2b(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['color','level']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    levelSelected = convertRaw['level'][rowChoice]
    colorSelected =  convertRaw['color'][rowChoice]
    number = int(convertRaw[0][rowChoice]) + rd.choice([1*booler,-1*booler]) 

    question =  "The total number of "+ colorSelected + " shapes on level "+ str(levelSelected)+ " is " + str(number) + '.'
    correctAnswer =  ['True','False'][booler]
    return question, correctAnswer

def question_2c(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['design','level']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    levelSelected = convertRaw['level'][rowChoice]
    shapeSelected = convertRaw['design'][rowChoice]
    number = int(convertRaw[0][rowChoice]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ shapeSelected + "s on level "+ str(levelSelected)+ " is " + str(number) + '.'
    correctAnswer =  ['True','False'][booler]
    return question, correctAnswer


def question_3a(dataMasterFrame):
    convertRaw =  dataMasterFrame

    booler = rd.randint(0,1)
    booler2 = rd.choice(['design','color'])
    rowChoice = rd.randint(0,len(convertRaw)-1)

    positionSelected = convertRaw['position'][rowChoice]
    levelSelected = convertRaw['level'][rowChoice]
    shapeSelected = convertRaw['design'][rowChoice]
    colorSelected =  convertRaw['color'][rowChoice]


    if booler2 == 'design':
        shapeSelected = allShapes[allShapes.index(convertRaw['design'][rowChoice])+rd.choice([-2*booler,-1*booler])]
    else:
        colorSelected =  allColors[allColors.index(convertRaw['color'][rowChoice])+rd.choice([-2*booler,-1*booler])]

    
    question = "The shape in the number "+ str(positionSelected) + " position on level "+ str(levelSelected) +" is a " + colorSelected + ' ' +shapeSelected + '.'
    correctAnswer =  ['True','False'][booler]
    
    return question, correctAnswer


def question_3b(dataMasterFrame):
    convertRaw =  dataMasterFrame

    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    positionSelected = convertRaw['position'][rowChoice]
    levelSelected = convertRaw['level'][rowChoice]
    colorSelected =  allColors[allColors.index(convertRaw['color'][rowChoice])+rd.choice([-2*booler,-1*booler])]

    question = "The shape in the number "+ str(positionSelected) + " position on level "+ str(levelSelected) +" is " + colorSelected + '.'
    correctAnswer = ['True','False'][booler]

    return question, correctAnswer


def question_3c(dataMasterFrame):
    convertRaw =  dataMasterFrame

    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    positionSelected = convertRaw['position'][rowChoice]
    levelSelected = convertRaw['level'][rowChoice]
    shapeSelected = allShapes[allShapes.index(convertRaw['design'][rowChoice])+rd.choice([-2*booler,-1*booler])]

    question = "The shape in the number "+ str(positionSelected) + " position on level "+ str(levelSelected) +" is a " + shapeSelected + '.'
    correctAnswer = ['True','False'][booler]
    
    return question, correctAnswer




def question_4a(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['color','design','position']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    positionSelected = convertRaw['position'][rowChoice]
    shapeSelected = convertRaw['design'][rowChoice]
    colorSelected =  convertRaw['color'][rowChoice]
    number = int(convertRaw[0][rowChoice]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ colorSelected + ' ' +shapeSelected + "s in the number "+ str(positionSelected)+ " position is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer


def question_4b(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['color','position']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    positionSelected = convertRaw['position'][rowChoice]
    colorSelected =  convertRaw['color'][rowChoice]
    number = int(convertRaw[0][rowChoice]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ colorSelected + " shapes in the number "+ str(positionSelected)+ " position is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer

def question_4c(dataMasterFrame):
    convertRaw =  dataMasterFrame.groupby(['design','position']).size().reset_index()
    booler = rd.randint(0,1)
    rowChoice = rd.randint(0,len(convertRaw)-1)

    positionSelected = convertRaw['position'][rowChoice]
    shapeSelected = convertRaw['design'][rowChoice]

    number = int(convertRaw[0][rowChoice]) + rd.choice([1*booler,-1*booler]) 

    question = "The total number of "+ shapeSelected + "s in the number "+ str(positionSelected)+ " position is " + str(number) + '.'
    correctAnswer = ['True','False'][booler]
    return question, correctAnswer

