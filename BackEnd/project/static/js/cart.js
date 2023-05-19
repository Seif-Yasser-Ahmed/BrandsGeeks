// Get the 'Remove' buttons
const removeBtns = document.querySelectorAll('.remove-product');


removeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const product = btn.parentElement.parentElement;
        product.remove();
        updateCartTotal();
        updateCartQuantity();
    });
});


const quantityInputs = document.querySelectorAll('.product-quantity input');


quantityInputs.forEach(input => {
    input.addEventListener('change', () => {
        updateCartTotal();
        updateCartQuantity();
    });
});


function updateCartTotal() {
    const prices = document.querySelectorAll('.product-price');
    let totalPrice = 0;
    prices.forEach(price => {
        const product = price.parentElement.parentElement;
        const quantity = product.querySelector('.product-quantity input').value;
        const priceValue = parseFloat(price.textContent.replace('EGP ', ''));
        totalPrice += priceValue * quantity;
    });
    const totalEl = document.querySelector('.cart-total p:nth-child(1) span:nth-child(2)');
    totalEl.textContent = totalPrice;
}


function updateCartQuantity() {
    const quantities = document.querySelectorAll('.product-quantity input');
    let totalQuantity = 0;
    quantities.forEach(quantity => {
        totalQuantity += parseInt(quantity.value);
    });
    const quantityEl = document.querySelector('.cart-total p:nth-child(2) span:nth-child(2)');
    quantityEl.textContent = totalQuantity;
}
