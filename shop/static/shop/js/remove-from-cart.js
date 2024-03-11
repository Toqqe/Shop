// Dodaj obsługę kliknięcia dla każdego przycisku

function removeFromCart(e){

    const productId = e.getAttribute("data-item-id"); 
    const priceElement = document.querySelector('.price')


    if(e.dataset.value == 1){
        fetch('/cart/remove-from-cart/', {
            method:'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ productId: productId }) 
        })
        .then(response => response.json())
        .then(data => {
            if(data.status == 200){
                let row = document.querySelector(`tr[data-item-id='${productId}']`);
                row.remove();
                priceElement.textContent = data.new_total_price;

                if(data.new_total_price_disc){
                    const priceElement = document.getElementById('order-price-disc')
                    priceElement.textContent = data.new_total_price_disc
                }
            }
        })
    
    }else if(e.dataset.value == 2){
        fetch(`/cart/reset-cart/`, {
            method:'POST',
            headers: {
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => response.json())
        .then(data => {

            let rows = document.querySelectorAll(`tr[data-item-id]`);
            rows.forEach((row)=>{
                row.remove();
            })
            priceElement.textContent = 0;

        })

    }

};






















            // // Pobierz id produktu z atrybutu data-product-id
            // const productId = this.getAttribute("data-product-id"); 
            // const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').getAttribute('value');

            // const cartIcon = this.querySelector('.bi');
            // cartIcon.classList.add('changing-icon');


            // fetch(`/cart/add-to-cart/${productId}/`, {
            //     method:'POST',
            //     headers: {
            //         'X-CSRFToken': csrfToken
            //     }
            // })
            // .then(response => response.json())
            // .then(data => {

            //     cartIcon.querySelector('use').setAttribute('xlink:href', '#check');

            //     // Usuń animację checkmark po chwili
            //     setTimeout(() => {
            //         cartIcon.querySelector('use').setAttribute('xlink:href', '#basket');
            //         cartIcon.classList.remove('changing-icon');
            //     }, 1500);

            // })