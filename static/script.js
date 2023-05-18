const moter1=document.getElementById("moter1");
const moter2=document.getElementById("moter2");



moter1.oninput = function() {

   var url = new URL('http://127.0.0.1:5000/moter1?angle1='+this.value);
   window.location.replace(url);
var c = url.searchParams.get("angle");
moter1.value=c

  }

  moter2.oninput = function() {
    var url1 = new URL('http://127.0.0.1:5000/moter2?angle2='+this.value);
   window.location.replace(url1);
var c = url1.searchParams.get("angle");
moter2.value=c
 
  }


  var url = new URL(window.location.href);
var c = url.searchParams.get("angle1");
moter1.value=c

var url2 = new URL(window.location.href);
var c = url2.searchParams.get("angle2");
moter2.value=c