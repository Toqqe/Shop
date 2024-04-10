const swiper = new Swiper(".mySwiper", {
    speed: 400,
    loop: true,
    slidesPerView: 4,
    spaceBetween: 50,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
  });
