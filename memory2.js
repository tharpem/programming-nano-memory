
this.dad = "grandpa";
music_dic= {"music1": "vogue.png", "music1a": "vogue.png", "music2": "beyonce.png", "music2a": "beyonce.png",
"music3": "siouxsie.png", "music3a": "siouxsie.png", "music4": "fifty.png", "music4a": "fifty.png",
"music5": "bobby_blue_bland.png", "music5a": "bobby_blue_bland.png", "music6": "taylor.png", "music6a": "taylor.png",
"music7": "jill.png", "music7a": "jill.png", "music8": "thicke.png", "music8a": "thicke.png"};
card_dic={}

window.clickGame = document.getElementById("music").onclick = clickGame(){
  global music_dic, car_dic, nature_dic, card_dic
  console.log("open game selector")
  card_dic = music_dic
  return card_dic};

var mysample = ""
var openGame =  function setval(varval)
  {

    mysample= varval;
  	alert(mysample);}
