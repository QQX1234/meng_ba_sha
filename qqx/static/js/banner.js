$(function () {
             $.getJSON('/api/v1/banner/', function (response) {
                 console.log(response)
                 if (response.status == 200){
                     var list = response.list

                     var $wrapper = $('.swiper-wrapper')
                     for (var i=0; i<list.length; i++){
                         var $slider = $('<div></div>').addClass('swiper-slide').appendTo($wrapper)
                         $('<img />').addClass('swiper-lazy').attr('data-src', list[i].img).appendTo($slider)
                         $('<div></div>').addClass('swiper-lazy-preloader swiper-lazy-preloader-white').appendTo($slider)
                     }


                     // 初始化轮播图
                     var swiper = new Swiper('.swiper-container', {
                        nextButton: '.swiper-button-next',
                        prevButton: '.swiper-button-prev',
                        pagination: '.swiper-pagination',
                        paginationClickable: true,
                        // Disable preloading of all images
                        preloadImages: false,
                        // Enable lazy loading
                        lazyLoading: true,
                         autoplay: 2000
                    });
                 }
             })
         })
