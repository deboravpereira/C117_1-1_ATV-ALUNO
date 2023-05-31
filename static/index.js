//Crie a variável de data
var date = new Date()
let display_date= "Data: " + date.toLocaleDateString('pt-BR', {weekday: 'short', year: 'numeric', month: 'short', day: 'numeric'})

//Carregue o DOM HTML
$(document).ready(function(){
    $("#display_date").html(display_date)
})

//Defina a variável para armazenar a emoção prevista


//seletor jQuery e ação de clique
$(function () {
    $("#predict_button").click(function () {
        var input_data = {
            "text": $("#text").val()
        }
        //chamada AJAX
        $.ajax({
            type: '',
            url: "",
            data: ,
            dataType: "",
            contentType: '',
            success: ,
            //Função de erro
            error: 
        });
    });
})

