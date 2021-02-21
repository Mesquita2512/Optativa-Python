$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("visible");


    //listando os veiculos
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
                lin = '<tr id="linha_'+veiculos[i].id + '">' + 
                        '<td>' + veiculos[i].marca + '</th>' + 
                        '<td>' + veiculos[i].nomeDescricao + '</td>' + 
                        '<td>' + veiculos[i].anoModelo + '</td>' + 
                        '<td>' + veiculos[i].cor + '</td>' +
                        '<td>' + veiculos[i].categoria + '</td>' +
                        '<td>' + veiculos[i].placa + '</td>' +
                        '<td>' + veiculos[i].renavam + '</td>' +
                        '<td>' + veiculos[i].empresa.nome + '</td>' +
                        '<td><a href=# id="excluir_' + veiculos[i].id + '" '+
                        'class="excluir_veiculo"><img src="images/excluir.png" ' +
                        'alt="Excluir Veiculo" title="Excluir Veiculo"></a>' +
                        '</td>' +
                        '</tr>';

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


    //adicionando um veiculo
    $("#bt_novo_veiculo").click(function(){
          //obter dados da tela
         marca_veiculo     = $("#marca_veiculo").val();
         descricao_veiculo = $("#descricao_veiculo").val();
         anoModelo_veiculo = $("#anoModelo_veiculo").val();
         cor_veiculo       = $("#cor_veiculo").val();
         categoria_veiculo = $("#categoria_veiculo").val();
         placa_veiculo     = $("#placa_veiculo").val();
         renavam_veiculo   = $("#renavam_veiculo").val();
         id_empresa        = $("#id_empresa").val();
        
          //preparar os dados para envio (json)
          dados = JSON.stringify({marca: marca_veiculo, nomeDescricao: descricao_veiculo, anoModelo: anoModelo_veiculo, cor: cor_veiculo, placa: placa_veiculo, renavam: renavam_veiculo, categoria: categoria_veiculo, idEmpresa: id_empresa});
          
          //mandar para o back-end
          
          $.ajax({
              url : 'http://localhost:5000/incluir_veiculo',
              type : 'POST',
              contentType : 'application/json', //envio de dados json
              dataType : 'json',
              data: dados,
              success: incluirVeiculo,
              error: erroIncluirVeiculo,
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
            if(resposta.resultado == "erro"){
                alert("Problema com o back-end")
            }
            

        }
    });

    //Excluindo um Veiculo pelo identificador
    //codigo para o icone de excluir Veiculo (classe css)
    $(Document).on("click", ".excluir_veiculo", function() {
        //obter o id do veiculo clicado
        var componente_clicado = $(this).attr('id'); //exemplo: excluir_15
        //obter o id do veiculo no id do componente clicado
        var nome_icone = "excluir_";
        var id_veiculo = componente_clicado.substring(nome_icone.length); //ex:15
        //solicitar a exclusao do Veiculo para o back end
        $.ajax({
            url: 'http://localhost:5000/excluir_veiculo/'+id_veiculo,
            type: 'DELETE', // metodo de requisição
            dataType: 'json', //tipo de dado
            success: veiculoExcluido,
            error: erroExcluir
        });
    function veiculoExcluido(retorno){
        if(retorno.resultado == "ok"){//a operação deu certo
            //remove da tela a linha cujo veiculo foi excluido
            $("#linha_" + id_veiculo).fadeOut(1000, function(){
                alert('Veiculo Excluído com sucesso!!!!');
            });
        } else{
            //informa mensagem de erro
            alert(retorno.resultado + ":" + retorno.detalhes);
              }
        
    }
    function erroExcluir(retorno){
        alert('Erro ao excluir Veiculo, verifique o back end!!!')
    }
    });
});