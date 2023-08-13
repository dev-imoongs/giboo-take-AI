//on class 이동시키는 js

const tabLinks = document.querySelectorAll('.link-tab');
tabLinks.forEach((link, index) => {
  link.addEventListener('click', function(event) {
    event.preventDefault(); // 기본 클릭 동작 방지

    tabLinks.forEach((tabLink, tabIndex) => {
      if (tabIndex === index) {
        tabLink.parentElement.classList.add('on');
      } else {
        tabLink.parentElement.classList.remove('on');
      }
    });
  });
});