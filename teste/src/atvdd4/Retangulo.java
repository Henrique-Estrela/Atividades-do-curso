/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atvdd4;

/**
 *
 * @author ALUNO
 */
public class Retangulo implements Quadrilatero{
    private float base;
    private float altura;

    public Retangulo(float base, float altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public float CalcularArea() {
      return base * altura;  
    }

    @Override
    public float CalcularPerimetro() {
        return (base + altura) * 2;
    }
    
    
}
