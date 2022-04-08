
package atvdd2;

/**
 *
 * @author ALUNO
 */
public class Novo extends Imovel{
    private double add;
            
    public Novo(String Local, double preco) {
        super(Local, preco);
    }


    public double getPreco(double add) {
        return preco + add;
        
    }

    
    public void setPreco(double preco) {
        this.preco = preco;
    }


    
}   