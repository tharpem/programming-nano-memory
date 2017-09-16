import random
import os
import webbrowser

nature_cards = ["nature1", "nature1a", "nature2", "nature2a", "nature3", "nature3a", "nature4", "nature4a", "nature5", "nature5a", "nature6", "nature6a", "nature7", "nature7a", "nature8", "nature8a"]
car_cards = ["car1", "car1a", "car2", "car2a", "car3", "car3a", "car4", "car4a", "car5", "car5a", "car6", "car6a", "car7", "car7a", "car8", "car8a"]
music_cards = ["music1", "music1a", "music2", "music2a", "music3", "music3a", "music4", "music4a", "music5", "music5a", "music6", "music6a", "music7", "music7a", "music8", "music8a"]
card_set = []
grid_dic= [["card1",  "card2",  "card3",  "card4"],
         ["card5",  "card6", "card7",  "card8"],
         [ "card9",  "card10",  "card11",  "card12"],
         ["card13", "card14",  "card15",  "card16"]]

new_grid_dic = [["","","",""], ["","","","",""], ["","", "", ""],["", "", "", ""]]

#Selection of cards
def repeat_card_pick(nature_cards, car_cards, music_cards):
    global card_set
    print ("I did not understand your selection, please read carefully and try again.")
    pick_card_set(nature_cards, car_cards, music_cards)

def pick_card_set(nature_cards, car_cards, music_cards):
    global card_set
    #card_pick = input('Which card set would you like to use?\n Select: \n "A"  for nature\n "B" for car or\n "C" for music\n')
    if "#card_pick" == "A" or "#card_pick" == "a" or "#card_pick" == "n" or "#card_pick" == "nature":
        card_set = nature_cards
        print ("You have selected the nature card set....Let's play!")
        return card_set
    elif "#card_pick" == "B" or "#card_pick" == "b" or "#card_pick" == "car" or "#card_pick" == "cars":
        card_set = car_cards
        print ("You have selected the car card set....Let's play!")
        return card_set
    elif "#card_pick" == "C" or "#card_pick" == "c" or "#card_pick" == "music":
        card_set = music_cards
        print ("You have selected the music card set....Let's play!")
        return card_set
    else:
        repeat_card_pick(nature_cards, car_cards, music_cards)





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
    <link rel="stylesheet" href="memory.css">
</head>
'''

main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<body>
<div font=bold> MAJI'S MEMORY GAME</div>
<div class= "gridRow" id="gridRow1">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell">Cell 0</div>
    <div class = "secondCell">Cell 1</div>
    <div class = "thirdCell">Cell 2</div>
    <div class = "fourthCell">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
<div class = "clearLeft"></div>

<div class= "gridRow" id="gridRow2">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell">Cell 0</div>
    <div class = "secondCell">Cell 1</div>
    <div class = "thirdCell">Cell 2</div>
    <div class = "fourthCell">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
<div class = "clearLeft"></div>

<div class= "gridRow" id="gridRow3">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell">Cell 0</div>
    <div class = "secondCell">Cell 1</div>
    <div class = "thirdCell">Cell 2</div>
    <div class = "fourthCell">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>
<div class = "clearLeft"></div>
<div class= "gridRow" id="gridRow4">
    <div class = "bufferLeftCell">empty</div>
    <div class = "firstCell">Cell 0</div>
    <div class = "secondCell">Cell 1</div>
    <div class = "thirdCell">Cell 2</div>
    <div class = "fourthCell">Cell 3</div>
    <div class = "bufferRightCell">empty</div>
</div>


    <p>Here is where grid should be</p>
    <script> ("node").child.Append(new_row_cells)
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

open_memory_page()
#grid_dic_fill()
#pick_card_set(nature_cards, car_cards, music_cards)
#random.shuffle(card_set)
print (new_grid_dic)
