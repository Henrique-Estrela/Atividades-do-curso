/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atvdd2;
import atvdd2.Novo;
import atvdd2.Velho;

import java.util.Scanner;

/**
 *
 * @author ALUNO
 */
public class Imovel {
    protected String Local;
    protected double preco;

    public Imovel(String Local, double preco) {
        this.Local = Local;
        this.preco = preco;
    }

   public class Novo extends Imovel{
    private double valorAdicional;
    
    public Novo(double valorAdicional, String endereco, double preco) {
        super(endereco, preco);
    }

    public double getValorAdicional() {
        return preco + valorAdicional;
    }
   }
   
    public static void main(String[] args) {
        
    }
   
   
}