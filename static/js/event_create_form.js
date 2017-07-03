$( document ).ready(function() {
    $("#delivery_cost").val("0");
    $("#tax_percentage").val("0");
    $("#subtotal").val("0");
    $("#forward_payment").val("0");
    $("#total").val("0");

    $(".calculateTotal").blur(function(){
        calculateTotal();
    });

    calculateTotal();
    //Modal [future feature]
    //document.getElementById("btnClientModal").onclick = function(){createClientModal();};
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
/*MODAL [FUTURE FEATURE]
function createClientModal(){
    $.ajax({
      method: "GET",
      url: clientCreatModalURL+"/1"
    }).done(function( msg ) {
        $('#clientModalBody').html(msg);
        $('#myModal').modal('show');
    });
}
*/