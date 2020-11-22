$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("invisible");

    $("#link_listar_veiculos").click(function(){
        
        $.ajax({
            url: 'http://localhost:5000/listar_veiculos',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_veiculos, // chama a função listar_plantas para processar o resultado
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_veiculos(veiculos) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as plantas retornadas em json
            for (var i in veiculos) {

              // montar uma linha da tabela de plantas
              lin = "<tr>" + 
              "<td>" + veiculos[i].marca + "</th>" + 
              "<td>" + veiculos[i].nomeDescricao + "</td>" + 
              "<td>" + veiculos[i].anoModelo + "</td>" + 
              "<td>" + veiculos[i].cor + "</td>" +
              "<td>" + veiculos[i].categoria + "</td>" +
              "<td>" + veiculos[i].placa + "</td>" +
              "<td>" + veiculos[i].renavam + "</td>" +
              "</tr>";

              // adicionar a linha da tabela em um acumulador
              linhas = linhas + lin;
            }
            // colocar as linhas na tabela
            $("#corpoTabelaVeiculos").html(linhas);

            // esconder todos os elementos da tela
            $("#conteudoInicial").addClass("visible");
            $("#tabelaVeiculos").addClass("visible");

            // exibir a tabela
           // $("conteudoInicial").removeClass("visible");
          //  $("#tabelaVeiculos").removeClass("visible");
        }

    });


     $("#link_apagar_tela").click(function(){
            $("#conteudoInicial").removeClass("true");
        });

});