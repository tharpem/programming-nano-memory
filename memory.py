import random
import os
import webbrowser


nature_cards = ["nature1", "nature1a", "nature2", "nature2a", "nature3", "nature3a", "nature4", "nature4a", "nature5", "nature5a", "nature6", "nature6a", "nature7", "nature7a", "nature8", "nature8a"]
car_cards = ["car1", "car1a", "car2", "car2a", "car3", "car3a", "car4", "car4a", "car5", "car5a", "car6", "car6a", "car7", "car7a", "car8", "car8a"]
music_cards = ["music1", "music1a", "music2", "music2a", "music3", "music3a", "music4", "music4a", "music5", "music5a", "music6", "music6a", "music7", "music7a", "music8", "music8a"]
card_set = []
original_card_list= ["card1",  "card2",  "card3",  "card4", "card5",  "card6", "card7",  "card8", "card9",  "card10",  "card11",  "card12","card13", "card14",  "card15",  "card16"]
card_dic = {}
new_grid_list = []

music_dic= {"music1": "ausbra.jpg", "music1a": "ausbra.jpg", "music2": "ausbra.jpg", "music2a": "ausbra.jpg",
"music3": "Antonio.jpg", "music3a": "Antonio.jpg", "music4": "Antonio.jpg", "music4a": "Antonio.jpg",
"music5": "Ananda.jpg", "music5a": "Ananda.jpg", "music6": "Ananda.jpg", "music6a": "Ananda.jpg",
"music7": "Ananda.jpg", "music7a": "Ananda.jpg", "music8": "Ananda.jpg", "music8a": "Ananda.jpg"}

#Selection of cards
def repeat_card_pick(nature_cards, car_cards, music_cards):
    global card_set
    print ("I did not understand your selection, please read carefully and try again.")
    pick_card_set(nature_cards, car_cards, music_cards)

def pick_card_set(nature_cards, car_cards, music_cards):
    global card_set, card_dic, testVar
    #card_pick = input('Which card set would you like to use?\n Select: \n "A"  for nature\n "B" for car or\n "C" for music\n')
    if "#card_pick" == "A" or "#card_pick" == "a" or "#card_pick" == "n" or "#card_pick" == "nature":
        card_set = nature_cards
        print ("You have selected the nature card set....Let's play!")
        return card_set
    elif "#card_pick" == "B" or "#card_pick" == "b" or "#card_pick" == "car" or "#card_pick" == "cars":
        card_set = car_cards
        print ("You have selected the car card set....Let's play!")
        return card_set
    #elif "#card_pick" == "C" or "#card_pick" == "c" or "#card_pick" == "music":
    elif testVar == "music_dic":
        card_dic = music_dic
        #print ("You have selected the music card set....Let's play!")
    return card_dic
    #else:
    #    repeat_card_pick(nature_cards, car_cards, music_cards)




#def grid_dic_fill():
#    global grid_dic, card_set, new_grid_dic
#    num_cols = 4
#    index = 0
#    row = -1

#    while row < 3:
#        col = 0
#        row += 1
#        for items in grid_dic[row]:
#            new_grid_dic[row][col]  = card_set[index]
#            col+=1
#            index+=1
#            print (new_grid_dic)
#        return new_grid_dic



main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Maji Memory Game</title>
    <script language="JavaScript" type="text/javascript" src="memory.js" charset="utf-8"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <script type="text/javascript">radioEvent(form) </script>

    <link rel="stylesheet" href="memory.css">
</head>
'''

main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<body>
<h1><div font=bold> MAJI'S MEMORY GAME</h1>
<h2>Select Your Game Theme</h2>

<form>
    <label>Nature Deck</label>
    <input type="radio" class="priority" name="priorityN" onclick="getResults();"  value="nature_cards" onclick="radioEvent(this.form);"/>
    <label>Car Deck</label>
    <input type="radio" class="priority" name="priorityN" onclick="getResults" value="car_cards"  onclick=radioEvent;/>
    <label>Music Deck</label>
    <input type="radio" class="priority" name="priorityN" value="music_cards" onclick=pick_card_set />
</form>
<script>pick_card_set(nature_cards, car_cards, music_cards)</script>
<script>shuffles </script>
<p id=game_start> </p>

<div id="gridContainer">
<script> cardsInGrid(shuffled_card_dic)</script>
<div class= "gridRow" id="gridRow1">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell"  id = "cell1">Cell 0</div>
    <div class = "secondCell" id = "cell2">Cell 1</div>
    <div class = "thirdCell"  id = "cell3">Cell 2</div>
    <div class = "fourthCell" id = "cell4">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
<div class = "clearLeft"></div>

<div class= "gridRow" id="gridRow2">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell"  id = "cell5">Cell 0</div>
    <div class = "secondCell" id = "cell6">Cell 1</div>
    <div class = "thirdCell"  id = "cell7">Cell 2</div>
    <div class = "fourthCell" id = "cell8>Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
<div class = "clearLeft"></div>

<div class= "gridRow" id="gridRow3">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell"  id = "cell9" >Cell 0</div>
    <div class = "secondCell" id = "cell10">Cell 1</div>
    <div class = "thirdCell"  id = "cell11">Cell 2</div>
    <div class = "fourthCell" id = "cell12">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
<div class = "clearLeft"></div>
<div class= "gridRow" id="gridRow4">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell"  id = "cell13">Cell 0</div>
    <div class = "secondCell" id = "cell14">Cell 1</div>
    <div class = "thirdCell"  id = "cell15">Cell 2</div>
    <div class = "fourthCell" id = "cell16">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
</div>

    <p>Here is where grid should be</p>
    <script> user = input("Welcome, what is your name? ")
    </script>
    <p id="tester"></p>
    <script>
        document.getElementById("tester").innerHTML = 4;
        </script>
    <p> Which card set would you like to use?\n Select: \n "A"  for nature\n
        "B" for car or\n "C" for music\n:</p>
        <p><input type="text" id="card_pick" /></p>
	  <p><input type="button" id="btnSubmit" value="Card_Selection" /></p>
     <script>

<script type="text/javascript">
  console.log(userPickingCard());
  </script>
    <!--<script scr="memory.js"> document.write(grid(4, 4, var new_grid_dic)) </script>


    <script var new_grid_dic; grid(4, 4, new_grid_dic)>
    </script>-->
  </div>
</html>
'''

def open_memory_page():
  # Create or overwrite the output file
  output_file = open('memory_test.html', 'w')
  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format()#there was a function

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()
  print ("closed file")

  # open the output file in the browser
 # url = os.path.abspath(output_file.name)
  url = os.path.abspath("memory_test.html")
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

def shuffles(card_dic):
    print (card_dic)
    card_list= music_dic.keys()
    for items in card_list:
        str(items)
    return card_list
    print (card_list)
    card_list = random.shuffle(card_list)
    print (card_list)
    shuffled_card_dic={}
    count=0
    index=card_list[count]
    for items in card_list:
        shuffled_card_dic[index]=card_dic[items]
        count +=1
    return shuffled_card_dic


open_memory_page()
print ("opened page")
#random.shuffle(card_set)
#grid_dic_fill()
#pick_card_set(nature_cards, car_cards, music_cards)
print ("picked card")




#shuffles(card_dic)
print ("shuffled card")
