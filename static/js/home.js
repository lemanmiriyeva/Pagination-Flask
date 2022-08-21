
var prev = document.querySelector('.prev');
var next = document.querySelector('.next');
var page = document.querySelectorAll('.pageNumber');
var letter = document.querySelectorAll('.letter');

prev.addEventListener('click', () => {
  for (let i = 0; i < page.length; i++) {
    if (page[i].className == 'pageNumber active') {
      if (i != 0) {
        page[i].classList.remove('active');
        page[i - 1].classList.add('active');
      }
      if (letter[i].className == 'letter active') {
        if (i != 0) {
          letter[i].classList.remove('active');
          letter[i - 1].classList.add('active');
          break;
        }

      }
    }
  }
});
next.addEventListener('click', () => {
  for (let i = 0; i < page.length; i++) {
    if (page[i].className == 'pageNumber active') {
      if (i != 4) {
        page[i].classList.remove('active');
        page[i + 1].classList.add('active');
      }

    }
    if (letter[i].className == 'letter active') {
      if (i != 4) {
        letter[i].classList.remove('active');
        letter[i + 1].classList.add('active');
        break;
      }

    }
  }
})
for(let i=0;i<page.length;i++){
  page[i].addEventListener('click',()=>{
    page.forEach(element=>{
      if(element.className=="pageNumber active"){
        element.classList.remove('active')
      }
    })
    letter.forEach(element=>{
      if(element.className="letter active"){
        element.classList.remove('active')
      }
    })
      page[i].classList.add('active');
      letter[i].classList.add('active');
    
    
  })
}