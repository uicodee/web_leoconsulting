//  ***** Scrolling event with Header *****
const fixedHeader = document.querySelector(".header__fixed");

document.addEventListener("scroll", function (e) {
  const heightY = scrollY;
  const navY = fixedHeader.offsetHeight;
  if (heightY > navY) {
    fixedHeader.classList.add("scroll");
  } else {
    fixedHeader.classList.remove("scroll");
  }
});

// ***** Opening and Clothing questions *****
const toggles = document.querySelectorAll(".quiz__toggle");
const activeQuiz = document.querySelector(".quiz__active");
const divContent = document.querySelectorAll(".quiz__content");
const icons = document.querySelectorAll(".icon");
const quizBox = document.querySelectorAll(".questions__box");
activeQuiz.style.height = activeQuiz.scrollHeight + "px";
for (let i = 0; i < toggles.length; i++) {
  toggles[i].addEventListener("click", function () {
    if (parseInt(divContent[i].style.height) != divContent[i].scrollHeight) {

      divContent[i].style.height = divContent[i].scrollHeight + "px";
      icons[i].classList.remove("fa-plus");
      icons[i].classList.add("fa-minus");
      quizBox[i].classList.add("plus");
    } else {
      divContent[i].style.height = "0px";
      icons[i].classList.add("fa-plus");
      icons[i].classList.remove("fa-minus");
      quizBox[i].classList.remove("plus");
    }

    for (let j = 0; j < divContent.length; j++) {
      if (j !== i) {
        divContent[j].style.height = "0px";
        icons[j].classList.add("fa-plus");
        icons[j].classList.remove("fa-minus");
        quizBox[j].classList.remove("plus");
      }
    }
  });
}

// ***end

const menuBtn = document.querySelector(".menu__btn");
const closeBtn = document.querySelector(".btn-close");
const nav = document.querySelector(".navigation");

menuBtn.addEventListener("click", function (e) {
  nav.classList.add("open");
});
closeBtn.addEventListener("click", function () {
  nav.classList.remove("open");
});
