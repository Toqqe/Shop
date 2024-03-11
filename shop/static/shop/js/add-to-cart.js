

function addToCart(){
    let addToCartButtons = document.querySelectorAll("#add-to-cart");

    // Dodaj obsługę kliknięcia dla każdego przycisku
    addToCartButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Pobierz id produktu z atrybutu data-product-id
            const productId = this.getAttribute("data-product-id"); 
            const cartIcon = this.querySelector('.bi');
            cartIcon.classList.add('changing-icon');


            fetch(`/cart/add-to-cart/`, {
                method:'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ productId: productId })
            })
            .then(response => response.json())
            .then(data => {

                cartIcon.querySelector('use').setAttribute('xlink:href', '#check');

                // Usuń animację checkmark po chwili
                setTimeout(() => {
                    cartIcon.querySelector('use').setAttribute('xlink:href', '#basket');
                    cartIcon.classList.remove('changing-icon');
                }, 1500);

            })
        });
    });
};
addToCart();