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
public class CamaroteInferior extends Vip {
      String LocalIngresso;

     
    public String getLocalIngresso(){
      return this.LocalIngresso;
    }
    public void setLocalIngresso(String local){
        this.LocalIngresso = local;
    }
   
    public String acessaLocalizacao(){
        return this.LocalIngresso;
    }
    public void imprimeLocalizacao(String local){
        local = this.LocalIngresso;
        System.out.println("Local:"+ local);
    }
}
