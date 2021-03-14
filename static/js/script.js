// Materealize JS 

$(document).ready(function () {
    $('.sidenav').sidenav();
});


//   Form Slider
$('.btn-register').on("click", () => {
    $('.slider-forms').addClass("slide-active");
    $('.form-register').removeClass("form-hidden");
    $('.form-login').addClass("form-hidden");
});


$('.btn-login').on("click", () => {
    $('.slider-forms').removeClass("slide-active");
    $('.form-register').addClass("form-hidden");
    $('.form-login').removeClass("form-hidden");
});