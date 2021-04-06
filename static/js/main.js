// eslint 플러그인 -> javascript standard 적용

/* Please ❤ this if you like it! */


/*(function($) { "use strict";
	const navbarNav = document.querySelector('.navbar-nav.nav-item pl-4 pl-md-0');
	const navbarNav = $('.navbar-nav');
	
	window.addEventListener('onload', () => {
		alert('hello');
	});

	$(window).onload(()=>{
		
	})

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {    
			var scroll = $(window).scrollTop();
		
			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});		
		
	//Animation
	
	$(document).ready(function() {
		$('body.hero-anime').removeClass('hero-anime');
	});

	//Menu On Hover
		
	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});	

	
  })(jQuery); */ 

  /* 햄버거 버튼 눌렸을 때 햄버거 - x 바꿔주기 */
  $(document).ready(function(){
	$('.con').click(function(e){
		e.preventDefault();
		$(this).toggleClass('con-no');
	});
});