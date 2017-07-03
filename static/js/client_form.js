window.onload = function () {
}

function saveWithAJAX(formId){
    form = $("#clientForm");
    console.log("***********");
    console.log($(form).serialize());
    console.log($(form));
    $.ajax({
        type: $(form).attr('method'),
        data: $(form).serialize(),
        url: clientCreatModalURL,
        context: form,
        success: function(data, status) {
            alert(data);
        },
        error:function(errr){
            alert("error");
        }
    });
}