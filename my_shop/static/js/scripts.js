
$(function() {
    $('input:radio[name="delivery"]').change(function() {
        if ($(this).val() === '1') {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});


$(document).on("click", ".add-to-cart", function (e) {

    e.preventDefault();

    var goodsInCartCount = $("#cart-count");
    var cartCount = parseInt(goodsInCartCount.text() || 0);

    var product_id = $(this).data("product-id");

    var add_to_cart_url = $(this).attr("href");

    $.ajax({
        type: "POST",
        url: add_to_cart_url,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        },
        success: function (data) {

            cartCount++;
            goodsInCartCount.text(cartCount);

            var cartItems = $("#cart-items");
            cartItems.html(data.cart_html);
        },

        error: function (data) {
            console.log("Ошибка при добавлении товара в корзину");
        },
    });
});


$(document).on("click", ".remove-from-cart", function (e) {
    e.preventDefault();

    var goodsInCartCount = $("#cart-count");
    var cartCount = parseInt(goodsInCartCount.text() || 0);

    var cart_id = $(this).data("cart-id");

    var remove_from_cart = $(this).attr("href");

    $.ajax({

        type: "POST",
        url: remove_from_cart,
        data: {
            cart_id: cart_id,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        },
        success: function (data) {

            cartCount -= data.quantity_deleted;
            goodsInCartCount.text(cartCount);

            var cartItems = $("#cart-items");
            cartItems.html(data.cart_html);

        },

        error: function (data) {
            console.log("Ошибка при добавлении товара в корзину");
        },
    });
});

//$(document).on('click', '.increment', function(e) {
//
//    e.preventDefault();
//
//    var cart_id = $(this).data("cart-id");
//    var goodsInCartCount = $("#cart-count");
//    var cartCount = parseInt(goodsInCartCount.text() || 0);
//    var quantityVal = $(this).closest("input[name='quantity']").val();
//    var qtyVal = quantityVal+1;
//    var update_cart = $(this).attr("href");
//
//    $.ajax({
//        url: update_cart,
//        type: 'POST',
//        data: {
//            cart_id: cart_id,
//            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
//            quantity: qtyVal,
//        },
//        success: function(data) {
//
//            quantityVal = qtyVal;
//            cartCount++;
//            goodsInCartCount.text(cartCount);
//
//            var cartItems = $("#cart-items");
//            cartItems.html(data.cart_html);
//        },
//
//        error: function (data) {
//            console.log("Ошибка при добавлении товара в корзину");
//        },
//    });
//});


//$(document).on('click', '.decrement', function(e) {
//  // Does some stuff and logs the event to the console
//    e.preventDefault();
//
//    var cart_id = $(this).data("cart-id");
//    var quantityVal = parseInt($(this).closest("input[name='quantity']").val() || 0);
//    var qtyVal = quantityVal-1;
//    var goodsInCartCount = $("#cart-count");
//    var cartCount = parseInt(goodsInCartCount.text() || 0);
//
//
//    var update_cart = $(this).attr("href");
//
//    $.ajax({
//        url: update_cart,
//        type: 'POST',
//        data: {
//            cart_id: cart_id,
//            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
//            quantity: qtyVal,
//        },
//        success: function(data) {
//            this.parentNode.querySelector("input[name='quantity']").stepDown();
//            cartCount--
//            goodsInCartCount.text(cartCount);
//
//            var cartItems = $("#cart-items");
//            cartItems.html(data.cart_html);
//        },
//
//        error: function (data) {
//            console.log("Ошибка при добавлении товара в корзину");
//        },
//    });
//});