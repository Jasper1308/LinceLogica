//Importando bibliotecas
#include <stdio.h>

//Definindo função principal
int main()
{
    //Definindo variáveis
    int a, b, c;
    
    //Entrada de dados
    printf("Digite o valor 1 ");
    scanf("%d",&a);
    printf("Digite o valor 2 ");
    scanf("%d",&b);
    
    //Condicional para definir maior número e fazer cálculo
    if(a>b){
        c=a/b;
    }else{
        c=b/a;
    }
    //Mostrando Resultado
    printf("%d",c);

    return 0;
}