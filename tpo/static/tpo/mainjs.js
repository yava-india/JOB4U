var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

// function checkNavbar(){
//   // alert("Your screen resolution is: " + screen.width + "x" + screen.height);
//   const sw = screen.width;
//   var x = document.getElementsByClassName("Navbar-items")
//   if(sw >= "670px"){
//     if (x.style.display === "none") {
//     x.style.display = "block";
//     }
//   }
//   else{
//     if (x.style.display === "block") {
//     x.style.display = "none";
//     }
//   }
// }


/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "100%";
  document.body.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
  // document.getElementById("myVideo").style.opacity = "0.4";
  document.getElementById("top-wrapper").style.opacity = "0.4";
  document.getElementById("upcoming-drives").style.opacity = "0.4";
  document.getElementById("our-recruiters").style.opacity = "0.4";
  document.getElementById("image-gallery").style.opacity = "0.4";
  document.getElementById("video-gallery").style.opacity = "0.4";
  document.getElementById("reach-us").style.opacity = "0.4";
  document.getElementById("footer").style.opacity = "0.4";
  document.getElementById("cuform").style.display = "none";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0px";
  document.body.style.backgroundColor = "black" ;
  // document.getElementById("myVideo").style.opacity = "1";
  document.getElementById("top-wrapper").style.opacity = "1";
  document.getElementById("upcoming-drives").style.opacity = "1";
  document.getElementById("our-recruiters").style.opacity = "1";
  document.getElementById("image-gallery").style.opacity = "1";
  document.getElementById("video-gallery").style.opacity = "1";
  document.getElementById("footer").style.opacity = "1";
  document.getElementById("reach-us").style.opacity = "1";
}

// function openForm() {
//   // document.getElementById("cuform").style.width = "40%";
//   document.getElementById("cuform").style.display = "block";
//   document.body.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
//   document.getElementById("top-wrapper").style.opacity = "0.4";
//   // document.getElementById("containerinVideo").style.opacity = "0.4";
//   document.getElementById("upcoming-drives").style.opacity = "0.4";
//   document.getElementById("our-recruiters").style.opacity = "0.4";
//   document.getElementById("image-gallery").style.opacity = "0.4";
//   document.getElementById("video-gallery").style.opacity = "0.4";
//   document.getElementById("reach-us").style.opacity = "0.4";
//   document.getElementById("footer").style.opacity = "0.4";
//   document.getElementById("mySidenav").style.width = "0px";
// }
//
// function closeForm() {
//   // document.getElementById("cuform").style.width = "0%";
//   document.getElementById("cuform").style.display = "none";
//   document.body.style.backgroundColor = "black" ;
//   document.getElementById("top-wrapper").style.opacity = "1";
//   // document.getElementById("containerinVideo").style.opacity = "1";
//   document.getElementById("upcoming-drives").style.opacity = "1";
//   document.getElementById("our-recruiters").style.opacity = "1";
//   document.getElementById("image-gallery").style.opacity = "1";
//   document.getElementById("video-gallery").style.opacity = "1";
//   document.getElementById("footer").style.opacity = "1";
//   document.getElementById("reach-us").style.opacity = "1";
// }
