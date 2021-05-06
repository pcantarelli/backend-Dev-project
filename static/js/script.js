// Materealize JS 
var currYear = (new Date()).getFullYear();

$(document).ready(function () {
    $('.sidenav').sidenav();

    $('.datepicker').datepicker({
        format: "dd/mm/yyyy",
        defaultDate: new Date(currYear - 5, 1, 31),
        maxDate: new Date(currYear - 5, 12, 31),
        yearRange: [1928, currYear - 5],
        i18n: {
            done: "Select"
        }
    });

    $('.collapsible').collapsible();
});

//   Register Form Slider
$('.btn-create').on("click", () => {
    $('.slider-forms').addClass("slide-active");
    $('.form-register').removeClass("hidden-form");
    $('.form-login').addClass("hidden-form");
    $('.left-area').addClass("mobile-hidden");
    $('.right-area').removeClass("mobile-hidden");
});

$('.btn-account').on("click", () => {
    $('.slider-forms').removeClass("slide-active");
    $('.form-register').addClass("hidden-form");
    $('.form-login').removeClass("hidden-form");
    $('.right-area').addClass("mobile-hidden");
    $('.left-area').removeClass("mobile-hidden");
});
