var new_grid_dic = {'a1': 'music3a', 'b1': 'music7', 'c1': 'music8', 'd1': 'music6', 'a2': 'music4', 'b2': 'music8a', 'c2': 'music2a', 'd2': 'music2', 'a3': 'music4a',
'b3': 'music5', 'c3': 'music7a', 'd3': 'music1a', 'a4': 'music3', 'b4': 'music6a', 'c4': 'music5a', 'd4': 'music1'};


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

// function grid(colnum, rownum, new_grid_dic) {
  //   var grid_array = [];
    // for (num = 0, num < colnum - 1, num++){
//     grid_array[num] = new_grid_dic[num],
  //   console.log(grid_array),
  //   return grid_array;
  function grid(colnum=4, rownum=4) {
    //default set for 4 rows and 4 columns/ 16 cells;
    global new_grid_dic;
    var newGrid = $('<div id="grid" class="gridContainer" ></div>');
    for (var row = 0; row < new_grid_dic.length; row++) {
    for (var column = 0; column < new_grid_dic[row].length; column++) {
    //  $("<div class='cell' "+row+","+col+"'>0</div>").appendTo(newGrid)
      //         document.getElementById(newGrid).appendChild("<div class='cell' ");  }
$( ".grid" ).append( '<div id="cell" ></div>' );}}

var new_row_cells = document.createElement( "div" ),
var node = document.getElementById("#gridContainer");

//function selectCardTheme() {
//    var txt;
//    var card_pick = prompt(" Which card set would you like to use?\n Select: \n "A"  for nature\n
//          "B" for car or\n "C" for music\n:");
//    if (card_pick == null || card_pick == "") {
//        repeat_card_pick(nature_cards, car_cards, music_cards);
//    } else {
//        pick_card_set(nature_cards, car_cards, music_cards);
//    }
//   document.getElementById("demo").innerHTML = txt;
//}

<script type='text/javascript'>
function promptbox() {
    var name = prompt("What you Want", ""); 
    if (name != null) {
        document.getElementById("demo2").innerHTML =
        "Hi. " + name;
    )}
}
</script>
window.testVar = ""
window.getResults = function getResults() {
    var radios = document.getElementsByName("priorityN");
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            testVar = "nature_cards"
            document.getElementById("myLink").innerHTML = '<a href=\"' + 'www.example.com?pri=' + testVar + '\" onclick=\"$(this).modal({width:880, height:460}).open(); return false;\" >' + 'My Modal Link' + "</a>";

        }else if  (radios[i+1].checked) {
        testVar = "car_cards"
        document.getElementById("myLink").innerHTML = '<a href=\"' + 'www.example.com?pri=' + testVar + '\" onclick=\"$(this).modal({width:880, height:460}).open(); return false;\" >' + 'My Modal Link' + "</a>";

        }   else if  (radios[i+1+1].checked) {
          testVar = "music_cards"
          document.getElementById("myLink").innerHTML = '<a href=\"' + 'www.example.com?pri=' + testVar + '\" onclick=\"$(this).modal({width:880, height:460}).open(); return false;\" >' + 'My Modal Link' + "</a>";
          }
        return testVar}

window.pick_card_set = function pick_card_set(){
    global card_set, card_dic, testVar, nature_cards, car_cards, music_cards
        //    #card_pick = input('Which card set would you like to use?\n Select: \n "A"  for nature\n "B" for car or\n "C" for music\n')
    console.log("opened pick card set function")
    if testVar == "nature_dic" {
      card_set = nature_cards;
    }  elseif testVar ==  "car_dic" {
      card_set = car_cards;
    }elif testVar == "music_dic":
      card_dic = music_dic;
    } radioEvent(this.form)
     console.log("launching this form")
    return card_dic}

window.radioEvent = function radioEvent(this.form){
     for (var i = 0; i < form.radioButton.length; i++)
     {
        if (form.radioButton[i].checked)
        {
            alert("You chose " + form.radioButton[i].value + ".")
        }
     }
     }

window. getResults = function getResults(){
  pick_card_set(nature_cards, car_cards, music_cards);
  radioEvent(form)
}

window.shuffles = function shuffles(card_dic) {
  card_list= card_dic.keys()
  for items in card_list {
    str(items);}
  card_list = random.shuffle(card_list);
  shuffled_card_dic={};
  count=0;
  index=card_list[count];}
  for items in card_list{
        shuffled_card_dic[index]=card_dic[items];
            count +=1;}
  document.getElementById("#game_start").innerHTML = "Game will now begin!";
    return shuffled_card_dic}




window.onload=function()
{
    var el=document.getElementById('button');
    el.onclick=function(){
        var my_text=prompt('Which card set would you like to use?\n Select: \n "A"  for nature\n"B" for car or\n "C" for music\n:');
        if(my_text == "" or my_text == null) alert("Please read again and select your option"); // for example I've made an alert
    }
}

window.onload=function selectCardTheme(){
    print("opened selectCardTheme")
    var x;
    var card_pick=prompt('Which card set would you like to use?\n Select: \n "A"  for nature\n"B" for car or\n "C" for music\n:');
    if (card_pick!=null and card_pick!=){
       x="Hello " + name + "! How are you today?";
      alert(x);
   }
}


window.fill_grid = function fill_grid(card_set) {
  var grid_cells: ["cell1", "cell2", "cell3", "cell4", "cell5", "cell6", "cell7", "cell8",
              "cell9", "cell10", "cell11", "cell12", "cell13", "cell14", "cell15", "cell16"]
  var grid_dic = {}
  index = 0
  grid_index=grid_cells[index]
  domloc=$(".gridContainer").find("#"+grid_index)
  for items in card_set {
    grid_dic[grid_index]= domloc.card_set[index]
    index +=1
    grid_index +=1
  return grid_dic
  }
}
)
music_dic= {"music1": 'ausbra.jpg', "music1a": 'ausbra.jpg', "music2": 'ausbra.jpg', "music2a": 'ausbra.jpg',
"music3": 'Antonio.jpg', "music3a": 'Antonio.jpg', "music4": 'Antonio.jpg', "music4a": 'Antonio.jpg',
"music5": 'Ananda.jpg', "music5a": 'Ananda.jpg', "music6": 'Ananda.jpg', "music6a": 'Ananda.jpg',
"music7": 'Ananda.jpg', "music7a": 'Ananda.jpg', "music8": 'Ananda.jpg', "music8a": 'Ananda.jpg'}


window.cardsInGrid = Function cardsInGrid (shuffled_card_dic) {}
    count = 0
    for items in shuffled_card_dic:
        $("#cell"+STR(count)).append("<img src="+ STR(items)/>)
        count +=1



    //  new_grid_dic[row][column];
    // return new_grid_dic
//    }
  //}
//function grid(row=4, col=4) {
  //system.out.print("grid function initiated")
  //for (int[] row : array)
  //{
    // for (int col : row)
     //{
      //    System.out.print(col + " ");
     //}
     //System.out.println();
  //}
//}

grid(4, 4, new_grid_dic);

function userPickingCard() {
  global card_set, nature_cards, car_cards, music_cards
  return "userPicking function"
}
pick_card_set(nature_cards, car_cards, music_cards)
random.shuffle(card_set)

function print(){
  console.log("me")
}
//  var grid_array = [],

//  num=0;
//  for (num, num < colnum - 1, num++){
//  grid_array[num] = new_grid_dic[num];
//  return grid_array;
//})
