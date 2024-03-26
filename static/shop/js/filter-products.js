
// let categoryButtons = document.querySelectorAll("#category-tag");
// const productClass = document.getElementById('products')

// categoryButtons.forEach(function(anchor) {
//     anchor.addEventListener('click', (event)=>{
//         event.preventDefault()
//         const choosedCategory = anchor.dataset.value;
//         let url = `/products/${choosedCategory}/`;
//         fetch(url)
//         .then(reponse => reponse.text())
//         .then(data =>{
//             productClass.innerHTML = data;
//             history.pushState(null, null, url);
//             addToCart();
//         })

//     });
// });