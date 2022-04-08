/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atvdd3;
import Atvdd1.CamaroteInferior;
import Atvdd1.CamaroteSuperior;
import Atvdd1.Ingresso;
import Atvdd1.Normal;
import Atvdd1.Vip;

/**
 *
 * @author ALUNO
 */
public class Main1 {
    
    public static void main(String[] args) {
        Ingresso ingresso = new Ingresso();
        Normal normal = new Normal();
        CamaroteInferior camaroteinferior = new CamaroteInferior();
        CamaroteSuperior camarotesuperior = new CamaroteSuperior();
        Vip vip = new Vip();
        ingresso.setValorIngresso(71);
        vip.setValorAdicional(0.7f);
        camaroteinferior.setLocalIngresso("terreo");
        camarotesuperior.setTaxaAdicional(0.5f);
        normal.setValorIngresso(70);
        normal.imprimeingressoNormal(normal.getValorIngresso());
        System.out.println("Ingresso Vip:"+vip.valorIngressoVip(ingresso.getValorIngresso()));
        System.out.println("Ingresso Vip Camarote Inferior:"+vip.valorIngressoVip(ingresso.getValorIngresso()));
        camaroteinferior.imprimeLocalizacao(camaroteinferior.getLocalIngresso());
        camarotesuperior.setValorAdicional(35);
        camarotesuperior.setValorIngresso(70);
        System.out.println("Ingresso Vip Camarote Superior:"+ camarotesuperior.valorIngressoAdd(vip.getValorAdicional()));
    }
    
}
