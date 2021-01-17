$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("visible");

    $("#link_listar_veiculos").click(function(){
        
        $.ajax({
            url: 'http://localhost:5000/listar_veiculos',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_veiculos, // chama a função listar_veiculos para processar o resultado
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
           //$("conteudoInicial").removeClass("visible");
          //$("#tabelaVeiculos").removeClass("visible");
        }

    });


      
    $("#bt_novo_veiculo").click(function(){
          //obter dados da tela
         marca_veiculo     = $("#marca_veiculo").val();
         descricao_veiculo = $("#descricao_veiculo").val();
         anoModelo_veiculo = $("#anoModelo_veiculo").val();
         cor_veiculo       = $("#cor_veiculo").val();
         categoria_veiculo = $("#categoria_veiculo").val();
         placa_veiculo     = $("#placa_veiculo").val();
         renavam_veiculo   = $("#renavam_veiculo").val();
        
          //preparar os dados para envio (json)
          dados = JSON.stringify({marca: marca_veiculo, nomeDescricao: descricao_veiculo, anoModelo: anoModelo_veiculo, cor: cor_veiculo, placa: placa_veiculo, renavam: renavam_veiculo, categoria: categoria_veiculo});
          
          //mandar para o back-end
          
          $.ajax({
              url : 'http://localhost:5000/incluir_veiculo',
              type : 'POST',
              ContentType : 'application/json', //envio de dados json
              dataType : 'json',
              data: dados,
              success: incluirVeiculo,
              error: erroIncluirVeiculo
          });

          function incluirVeiculo(resposta) {
              if (resposta.resultado == "ok"){
              //exibe mensagem de sucesso
              alert('Veiculo incluido com sucesso!')
          
              //limpa valores do formulario
              $("#marca_veiculo").val("");
              $("#descricao_veiculo").val("");
              $("#anoModelo_veiculo").val("");
              $("#cor_veiculo").val("");
              $("#categoria_veiculo").val("");
              $("#placa_veiculo").val("");
              $("#renavam_veiculo").val("");
                }else{
                alert('Erro ao salvar Veículo!!!')
                 }
          }
        function erroIncluirVeiculo(resposta){
            alert("Problema com o back-end")

        }
    });
});