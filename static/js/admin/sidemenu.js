$(".triangle-button").each((i, e) => {

    let index = i;
    let $dom = $(e);
    let $menus = $($(".menus")[index]);
    let checkSlide;

    $dom.on("click", function(e) {
       e.preventDefault();
       console.log($menus);

       if(checkSlide){
          $dom.removeClass("triangle-acitve");
          $menus.slideUp();
          checkSlide = false;
       } else{
          $dom.addClass("triangle-acitve");
          $menus.slideDown();
          checkSlide = true;
       }
    });
 });