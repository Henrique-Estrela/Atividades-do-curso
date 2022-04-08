/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atvdd3;
import atvdd2.Imovel;
import atvdd2.Novo;
import atvdd2.Velho;
import java.util.Scanner;
/**
 *
 * @author ALUNO
 */
public class Main2 {


    public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    Imovel imovel = new Imovel("Salvador", 1000);
    Novo novo = new Novo("Salvador", 1000);
    Velho velho = new Velho("Feira", 1000);
        System.out.println("Digite 1 para Imovel NOVO e 2 para Imovel VELHO");
        int op;
        op = entrada.nextInt();
        switch(op){
            case 1:
                novo.getPreco(0.5f);
                novo.getPreco(125000f);
                novo.setPreco(0);
                break;
            case 2:
                velho.getPreco(0.5f);
                velho.getPreco(125000f);
                velho.setPreco(5);
                break;
                
            
            default:
                System.out.println("opção errada!");
        }
    }
   
}

