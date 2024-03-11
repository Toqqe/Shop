function updateCart(e){

    const newValueOfQuantity = e.value;

    if(newValueOfQuantity > 10){
        e.value = 10;
        newValueOfQuantity = e.value;
    }

    const cartItemID = e.getAttribute("data-item-id");
    const priceElement = document.querySelector(`.price-item-${cartItemID}`);
    const totalCartPrice = document.querySelector('.price');
    //    path('update-cart/<int:id>/<int:value>/', views.update_cart, name="update-cart")
    
    fetch('/cart/update-cart/', {
        method:'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            cartItemID: cartItemID,
            newValueOfQuantity: newValueOfQuantity
        }),
    })
    .then(response => response.json())
    .then(data => {

        priceElement.textContent = data.new_item_price
        totalCartPrice.textContent = data.new_total_price
    })

}