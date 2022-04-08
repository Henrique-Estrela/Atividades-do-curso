/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atvdd2;

/**
 *
 * @author ALUNO
 */
public class Velho extends Imovel{
   private double add;
            
    public Velho(String Local, double preco) {
        super(Local, preco);
    }

    public double getPreco(double add) {
        return preco - add;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    
    
}