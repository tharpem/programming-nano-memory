import random
import os
import webbrowser


main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Maji Memory Game</title>
    <link rel="stylesheet" href="memory2.css">
    <script src="memory2.js" type="text/javascript"></script>
<window.openGame= openGame();>

</head>
'''

main_page_content = '''
<body>
<h1> MAJI'S MEMORY GAME</h1>
<script>console.log(this.mysample)</script>
<div class = "threeCellRow" id="deck_selector_row">
    <div class = "bufferfarLeftCell"></div>
    <div class = "farLeftCell">  <img src="Ananda.jpg" id= "nature_image_selector" alt="Nature Deck" height="200" ;></div>
    <div class = "middleCell"><script>clickGame</script><img src="Antonio.jpg"  id= "car_image_selector" alt="Car Deck" height="200" ></div>
    <div class = "farRightCell"><img src="music_card_back.png"  id= "music" alt="Nature Deck" height="200" ;><p onclick="this.openGame">Desperate</p></div>
    <div class = "bufferfarRightCell"></div>
</div>

'''
def open_memory_page():
  # Create or overwrite the output file
  output_file = open('memory2.html', 'w')
  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format()#there was a function

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()
  print ("closed file")

  # open the output file in the browser
 # url = os.path.abspath(output_file.name)
  url = os.path.abspath("memory2.html")
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

open_memory_page()
