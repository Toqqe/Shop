const delCoupon = document.getElementById('remove-coupon');

delCoupon.addEventListener('click', ()=>{
    const frame = document.getElementById('response-container');
    let discountBlock = document.getElementById('discount-elements');
    let priceBlock = document.getElementById('price-block');

    fetch( '/coupon/remove/' ,{
        method:'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data =>{
        if(data.status == 200){
            location.reload();
            //border-color: rgba(57, 241, 33, 0.76);
            // delCoupon.style.display = 'none';
            // discountBlock.style.setProperty('display', 'none', 'important');

            // priceBlock.innerHTML += `
            // <div class="d-flex" id="price-elements">
            //     <svg class="bi bd-highlight my-1" width="1em" height="1em"><use xlink:href="#dollar"/></svg>
            //     <p class="bd-highlight" id="order-price">${data.old_price}</p>
            // </div>
            // `;
        }else{
            frame.innerHTML = `<div class="success-frame">Error</div>`;
        }
    })

});