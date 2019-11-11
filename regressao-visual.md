# Regressão Visual comparando diferenças em imagens (screenshots).

Chamaremos o screenshot original de *baseline* a o screenshot a ser comparado de *test* (*baseline* e *test* devem possuir as mesmas dimensões).

Inicialmente, precisamos definir o numero de linhas e colunas do grid, o qual dividirá a imagem em regiões que serão comparadas entre si. Nas situações de teste utilizei os valores de 60 linhas X 80 colunas e 100 linhas x 150 Colunas, onde o primeiro obteve melhores resultados.

Com o numero de linhas e colunas do grid, obtém-se as dimensões de cada célula/região a ser comparada a partir da divisão altura/linhas e largura/colunas. No caso de teste, os valores foram de 17x12 pixels em cada região.

Em seguida, iremos percorrer cada imagem e calcular o coeficiente de brilho de cada região. O coeficiente de brilho pode ser calculado de algumas formas, a utilizada nos testes foi calcular somatório da média aritmética simples entre os valores **RGBA** de cada pixel da célula e dividir por um fator de sensibilidade. Exemplo abaixo:

```
coeficiente_de_brilho = 0
fator_sensibilidade = 10
para cada x no intervalo [0, largura_da_celula] {
    para cada y no intervalo [0, altura_da_celula] {
        pixel = IMAGEM.getPixel(x, y);
        coeficiente_de_brilho += ((pixel.r + pixel.g + pixel.b + pixel.a) / 4);
    }
}
return coeficiente_de_brilho / fator_sensibilidade;
```

Esse cálculo é feito para cada região de ambas as imagens e comparadas 1 a 1. As regiões que apresentarem coeficientes de brilhos diferentes, são consideradas com mudanças.

Os resultados encontrados em testes foram satisfatórios. Porém, ainda é necessário verificar alguma alternativa para realizar os testes de regressão visual a partir de comparação entre a estrutura DOM e CSS de cada página.

