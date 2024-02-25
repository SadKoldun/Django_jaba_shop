
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

        },

        error: function (data) {
            console.log("Ошибка при добавлении товара в корзину");
        },
    });
});
