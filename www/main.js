$(document).ready(function () {
     $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
     })
     
     //siri configuration
     const siriContainer = document.getElementById("siri-container");
     
     //clear any existing children in the #siri-container to privent duplicate
     while(siriContainer.firstChild){
        siriContainer.removeChild(siriContainer.firstChild);

     }


     var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style:"ios9",
        amplitude:'4',
        speed:'0.20',
        autotart:true,
      });
     
      //siri-message
      $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync:true,
        },
        out:{
            effect:"fdeOutUp",
            sync:true,
        },
     })

     // event handeller -MickBtn click event
     $("#MicBtn").off("click").on("click",function() { 
        console.log("MickBtn click");
        //now we have  @eel.express so we can call it fromhere
        eel.playAssistantSound()
         //syntax jqueryattributset
         //step1; here we have Oval hidden = ture so we got oval page
        $("#Oval").attr("hidden", true);
        //step2;  and the siriwave is false that mean no open seripage
        $("#SiriWave").attr("hidden", false);
        eel.all_command()()   //calling t command
        

     });//step3; after clicking the MicBtn then the oval=fals and siriswave= ture 
      
 
});