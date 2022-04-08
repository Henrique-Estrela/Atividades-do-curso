package Atvdd1;

/**
 *
 * @author ALUNO
 */
public class Ingresso {
   public float ValorIngresso;
   
   public float getValorIngresso(){
   return this.ValorIngresso;
   }
   public void setValorIngresso(float valorIngresso){
   this.ValorIngresso = valorIngresso;
   }
    public void imprimeValor(float valor){
    valor = this.ValorIngresso;
       System.out.printf("Valor do Igresso:"+ valor);
    }
    
    
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

    
    

