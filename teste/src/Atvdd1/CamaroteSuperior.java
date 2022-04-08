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
public class CamaroteSuperior extends Vip{
    float TaxaAdicional;
    private float ValorAdicional;
    private float ValorIngresso;

   
    public void setTaxaAdicional(float valor){
        this.TaxaAdicional = valor;
    }
    public float getTaxaAdicional(){
        return this.TaxaAdicional;
    }  
    public float valorIngressoAdd(float valor){
        valor= this.ValorAdicional;
        float valorAdd =(this.TaxaAdicional*this.ValorIngresso)*2+this.ValorIngresso;
    return valorAdd;
    }
}   
