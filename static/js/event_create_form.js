$( document ).ready(function() {
    console.log( "ready!" );
    $("#delivery_cost").val("0");
    $("#tax_percentage").val("0");
    $("#subtotal").val("0");
    $("#forward_payment").val("0");
    $("#total").val("0");

    $(".calculateTotal").blur(function(){
        calculateTotal();
    });

    calculateTotal();
});

function calculateTotal(){
    var unit_price = $("#id_unit_price").val();
    var quantity = $("#id_quantity").val();
    var delivery = $("#id_delivery_cost").val();
    var subtotal;
    var itemPrice = 0;
    if(!isNaN(unit_price) && !isNaN(quantity)){
        itemPrice = unit_price * quantity;
    }
    if(isNaN(delivery)){
        delivery = 0;
    }
    subtotal = parseFloat(itemPrice)+parseFloat(delivery);
    $("#subtotal").val(subtotal);
    console.log(subtotal);
    /* END OF SUBTOTAL CALULATION*/

    var tax_percentage = $("#id_tax_percentage").val();
    var forward_payment =$("#id_forward_payment").val();
    var total = parseFloat(subtotal);
    if(!isNaN(tax_percentage)){
        total = parseFloat(subtotal)+((parseFloat(subtotal)*parseInt(tax_percentage))/100);
        $("#taxes").val((parseFloat(subtotal)*parseInt(tax_percentage))/100);
    }
    if(!isNaN(forward_payment)){
        total = parseFloat(total) - parseFloat(forward_payment);
    }
    $("#total").val(total);
}
	