document.addEventListener('DOMContentLoaded', function() {

const inputField = document.getElementById('coupon-input');
const couponBtn = document.getElementById('coupon-btn');
const orderPrice = document.getElementById('order-price');
const responseContainer = document.getElementById("response-container");
const getActiveCoupon = document.getElementById('active-coupon');
const priceElem = document.getElementById('price-elements');

    inputField.addEventListener('input', function() {
    if (inputField.value.trim() !== '') {
        couponBtn.removeAttribute('disabled');
    } else {
        couponBtn.setAttribute('disabled', '');
    }
    });

    couponBtn.addEventListener('click', ()=>{
        const inputValue = inputField.value.trim();
        
        fetch( '/coupon/apply/' ,{
            method:'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: inputValue })
        })
        .then(response => response.json())
        .then(data =>{
            if(data.status == 200){
                //border-color: rgba(57, 241, 33, 0.76);
                if(getActiveCoupon){
                    getActiveCoupon.style.display = 'none';
                }
                // data.old_price;
                // let oldPrice = `<svg class="bi bd-highlight my-1" width="1em" height="1em"><use xlink:href="#dollar"/></svg>
                // <p class="price bd-higdhlight text-decoration-line-through text-muted pe-2" id="order-price">${data.old_price}</p>`;

                // priceElem.insertAdjacentHTML('beforebegin', oldPrice);
                location.reload();
                // responseContainer.innerHTML = `<div class="success-frame">${data.message}</div>`;
                // inputField.style.borderColor = "#39f121c2";
                // orderPrice.innerHTML = data.new_price;
                // orderPrice.style.color = 'red';

            }else{
                responseContainer.innerHTML = `<div class="success-frame">${data.message}</div>`;
                inputField.style.borderColor = "#ff553f";
                console.log("iooio")
            }
        })
    });

});

// const couponBtn = document.getElementById('coupon-btn')
