AOS.init();

//var elNavbar = document.querySelector(".navbar");
//var elAddArticleBtn = document.querySelector(".add_article_btn");
//
//	// bu esa scroll bo'ganda brauzerni qiynamaslik uchun kod
//var debounce = function (func, wait, immediate) {
//  var timeout;
//  return function() {
//    var context = this, args = arguments;
//    var later = function() {
//      timeout = null;
//      if (!immediate) func.apply(context, args);
//    };
//    var callNow = immediate && !timeout;
//    clearTimeout(timeout);
//    timeout = setTimeout(later, wait);
//    if (callNow) func.apply(context, args);
//  };
//};
//
//// Bu scroll tepadan 200 px tushganda ishlashi uchun kod
//var onWindowScroll = function(){
//  if (window.scrollY > 200) {
//	  elNavbar.classList.add("navbar-fixed")
//	  document.body.style.marginTop = elNavbar.offsetHeight + "px"
//  }else{
//		document.body.style.marginTop = "0"
//		elNavbar.classList.remove("navbar-fixed")
//	}
//}
//
//document.addEventListener("scroll", debounce(onWindowScroll, 100))
//

//Bu alert chiqishi uchun
elAddArticleBtn.addEventListener("click", function () {
    alert("Maqolangiz admin tomonidan ko'rib chiqiladi va tez fursat ichida taomnomalar qatoriga qo'shiladi")
})