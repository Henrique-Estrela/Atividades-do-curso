
// Limpa Campos do Formulário
function limpa_formulario()
{
    var forms = document.querySelector('#painel_form_consulta');
    var campos = forms.querySelectorAll('[name]');
    
    for (var i = 0; i < campos.length; i++) 
    {
        var campo = campos[i];
        if(campo instanceof HTMLInputElement)
        {
            if(campo.type == 'text')
            {                                                                                                                                           
                if(campo.length > 1) 
                {
                    for(var j = 0; j < campo.length; j++)
                        campo[j].value = "";
                }
            }
        } 
        else if(campo instanceof HTMLSelectElement)
        {
            campo.selectedIndex = 0;
        }
    }
}


function remove_linhas(t)
{
    while(t.rows.length > 1)
    {
        t.deleteRow(1);
    }    
}


/* Retorna a faixa de cep  */
function pesquisar_faixa_cep(dados,chave)
{ 
    /* Faixas de CEP */ 
   var tipo = "";
   var faixa_cep = ""; 
   if ( dados[chave].faixasCep[0] )
   {
        var faixa_cep_inicial = "";
        var faixa_cep_final = ""; 
        var tamanho = dados[chave].faixasCep.length;
        var cont = 0;
        for (var i = 0; i < tamanho; i++)
        {
            cont = cont + 1;     
            tipo = dados[chave].faixasCep[i].tipo;
            //faixa_cep_inicial = dados[chave].faixasCep[i].cepInicial.substring(0, 5) + "-" +  dados[chave].faixasCep[i].cepInicial.substring(5, 8); 
            //faixa_cep_final   = dados[chave].faixasCep[i].cepFinal.substring(0, 5) + "-" +  dados[chave].faixasCep[i].cepFinal.substring(5, 8); 
            faixa_cep_inicial = dados[chave].faixasCep[i].cepInicial
            faixa_cep_final   = dados[chave].faixasCep[i].cepFinal
            if (faixa_cep_inicial.length > 1 && faixa_cep_final.length > 1 )
            {    
                if (cont < 2)
                {    
                    faixa_cep = faixa_cep_inicial + "  a  " +  faixa_cep_final; 
                }
                else
                {    
                    faixa_cep = faixa_cep + ",   " + faixa_cep_inicial + "  a " +  faixa_cep_final; 
                }    
            } 
        } 
    }
    return faixa_cep;
}



/* Retorna a faixa da caixa postal  */
function pesquisar_faixa_caixa_postal(dados,chave)
{ 
    /* Faixas de Caixa Postal */
    var faixa_cxp = "";        
    if ( dados[chave].faixasCaixaPostal[0] )
    {    
        var faixa_cxp_inicial = "";
        var faixa_cxp_final = "";
        var tamanho = dados[chave].faixasCaixaPostal.length;
        var cont = 0;
        for (var i = 0; i < tamanho; i++)
        {
            cont = cont + 1;                
            faixa_cxp_inicial = dados[chave].faixasCaixaPostal[i].caixaInicial; 
            faixa_cxp_final   = dados[chave].faixasCaixaPostal[i].caixaFinal;
            if ( faixa_cxp_inicial.length > 0 && faixa_cxp_final.length > 0 )
            {    
                if (cont < 2)
                {    
                    faixa_cxp = faixa_cxp_inicial + "  a  " +  faixa_cxp_final; 
                }
                else
                {    
                    faixa_cxp = faixa_cxp + ",   " + faixa_cxp_inicial + "  a " +  faixa_cxp_final; 
                }    
            } 
        }        
    }
    return faixa_cxp;
}



function faixa_cep_tipo(dados,chave)
{ 
   /* Faixas de CEP */ 
   var tipo = "";
   if ( dados[chave].faixasCep[0] )
   {
        var tamanho = dados[chave].faixasCep.length;
        var cont = 0;
        for (var i = 0; i < tamanho; i++)
        {
            cont = cont + 1;     
            tipo = dados[chave].faixasCep[i].tipo;
        } 
    }
    return tipo;
}
