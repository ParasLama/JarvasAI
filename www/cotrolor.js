//syntex jqdo
$(document).ready(function () {
    
 //Display speak message
 eel.expose(DisplayMessage)
 //function for displaymessae in frontend
 function DisplayMessage(message){
     $(".siri-message li:first").text(message);
     $(".siri-message ").textillate('start');
 }

//Displayying hood=mainpage again
eel.expose(ShowHood)
//function for displaymessae in frontend
function ShowHood(){
      
       $("#Oval").attr("hidden",false);
       $("#SiriWave").attr("hidden",true);

  }


});
 

