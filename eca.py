#created by Owais Quadri (100697281) on Nov 21, 2021
import shutil as ui
import time
money="${:,.2f}"
columns=ui.get_terminal_size()[0]
answers=()
def getAnswer(answers,q):
    ans=input(q).lower()
    if ans == 'y' or ans == 'n':
        return ans
    else:
        print('Invalid Entry: autofilled to \'n\'')
        return 'n'
    
#init centered title
program_title="Embedded Configuration Assistant"
i=int((columns-len(program_title))/2)-2
spacer=""
for i in range(i):
    spacer+="~"
#application title
print(spacer,program_title,spacer,"\n")
print("Exit at any time using Ctrl-C")
#use a try-catch in case the user wants to exit at any time using ctrl c
try:
    #init questions
    q0="Should the embedded system have Wi-Fi? (Y/n)"
    q1="Should the embedded system cost less than $125? (Y/n)"
    q2="Should the embedded system have 4GB or more RAM? (Y/n)"
    q3="Should the embedded system excel in machine learning? (Y/n)"
    q4="Should the embedded system run android? (Y/n)"
    #get answers from above questions and append to answer tuple
    #(tuples are faster than list/string storage and manipulation)
    answers+=(getAnswer(answers,q0),)
    answers+=(getAnswer(answers,q1),)
    answers+=(getAnswer(answers,q2),)
    answers+=(getAnswer(answers,q3),)
    answers+=(getAnswer(answers,q4),)
    #init names of embedded systems (ES)
    ES1="Raspberry Pi 4 Model B"#4core, gpu,1.5ghz,1GB+ ram,wifi,noML
    ES2="Raspberry Pi Zero"#1core,nogpu,1ghz,512mb ram,nowifi,noML
    ES3="Raspberry Pi Zero W"#1core,nogpu,1ghz,512mb ram,wifi,noML
    ES4="Nvidia Jetson TX2"#6core,gpu,2ghz,8GB RAM,wifi,ML
    ES5="Odroid XU4"#8core,gpu,2GHz,2GB ram,wifi,ML,android
    ES6="NVIDIA Jetson Nano"#4core,gpu,1.43ghz,4GB RAM,no wifi,ML
    ES7="Coral Dev Board"#4core,gpu,1.5ghz,1gb ram,wifi,ml
    ES8="UDOO Quad"#4 core,gpu,1ghz,1gb ram,wifi, noML
    ES9="Hikey 970 Development Board"#8core,gpu,2.08 ghz,6gb ram,wifi,ml,android
    ES10="Respeaker Core v2.0"#4core,gpu,1.5ghz,1gb ram,wifi,ML,android,sound apps
    #initialize ES score
    score={
        ES1:0,
        ES2:0,
        ES3:0,
        ES4:0,
        ES5:0,
        ES6:0,
        ES7:0,
        ES8:0,
        ES9:0,
        ES10:0,
    }
    #define prices for each board
    PRICE={
        ES1:47.45,
        ES2:5,
        ES3:10,
        ES4:399,
        ES5:130.25,
        ES6:89,
        ES7:169.99,
        ES8:135,
        ES9:299,
        ES10:99,
    }
    #process answers
    if answers[0] == 'y':
        #wifi
        add_devices=[ES1,ES3,ES4,ES5,ES7,ES8,ES9,ES10]
        for device in add_devices:
            score[device]+=5
    if answers[1] == 'y':
        #cost<125
        add_devices=[ES1,ES2,ES3,ES6,ES10]
        for device in add_devices:
            score[device]+=5
    if answers[2] == 'y':
        #4gb or more ram
        add_devices=[ES1,ES4,ES6,ES9]
        for device in add_devices:
            score[device]+=1
    if answers[3] == 'y':
        #machine learning
        add_devices=[ES4,ES5,ES6,ES7,ES9,ES10]
        for device in add_devices:
            score[device]+=2
    if answers[4] == 'y':
        #android
        add_devices=[ES5,ES9]
        for device in add_devices:
            score[device]+=2

    suggestions=[]
    max_score=max(score.values())
    for device,score in score.items():
        if score==max_score:
            suggestions.append(tuple((device,PRICE[device])))
    print("\nSuggested Device(s) (sorted by price):")
    suggestions.sort(key=lambda y: y[1])
    for device,price in suggestions:
        print("Device: ",device,", Starting Price:",money.format(price))
    input("\nPress the Enter key to exit")
except KeyboardInterrupt:
    print('\nexiting ...')
    time.sleep(2)