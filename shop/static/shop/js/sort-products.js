
let selectElement = document.getElementById("form-select");
const category = JSON.parse(document.getElementById('curr-category').textContent);
const productClass = document.getElementById('products')

selectElement.addEventListener("change", ()=> {

    let selectedValue = selectElement.value;

    let url;
    if(category != ""){
        url = `/products/filter=${category}/?ordby=${selectedValue}`
    }
    else{
        url = `/products/?ordby=${selectedValue}`
    }

    fetch(url)
    .then( response => response.text())
    .then(data => {
        productClass.innerHTML = data;
        addToCart();
    })
});