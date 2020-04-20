document.addEventListener("DOMContentLoaded", function(){ 


  var hamburger = document.getElementById('hamburger');


  hamburger.onclick = function(event) {
    var menu = document.getElementsByClassName('navbar-nav')[0];
    if (menu.style.display == 'flex') 
      {menu.style.display = 'none';}
      else {menu.style.display = 'flex';}
  }
});
