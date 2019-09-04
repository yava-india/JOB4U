/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "400px";
  document.body.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
  document.getElementById("myVideo").style.opacity = "0.4";
  document.getElementById("containerinVideo").style.opacity = "0.4";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.body.style.backgroundColor = "black" ;
  document.getElementById("myVideo").style.opacity = "1";
  document.getElementById("containerinVideo").style.opacity = "1";
}

$('body').on('click', function(){
  if( parseInt( $('#mySidenav').css('width') ) > 0 ){
    closeNav();
  }
});
