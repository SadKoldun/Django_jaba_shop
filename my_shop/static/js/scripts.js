
$(function() {
    $('input:radio[name="delivery"]').change(function() {
        if ($(this).val() === '1') {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});