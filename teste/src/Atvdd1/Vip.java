/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Atvdd1;

/**
 *
 * @author ALUNO
 */
public class Vip extends Ingresso {
    public float ValorAdicional;
   
    public float getValorAdicional(){
    return this.ValorAdicional;
    }
    public void setValorAdicional(float valorAdicional){
        this.ValorAdicional = valorAdicional;
    }
    public float valorIngressoVip(float valoringresso){
         this.ValorIngresso = valoringresso;
        return this.ValorIngresso + (this.ValorAdicional* this.ValorIngresso);       
    }
}

    


