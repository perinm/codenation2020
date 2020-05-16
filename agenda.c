#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CARAC 100
#define MAX_CONT 50
#define MAX_NUM 9

void limpaFluxo() {
	int ch;
	do {
		ch = fgetc(stdin);
	}
	while (ch != EOF && ch != '\n');
}

void addNOME(char nome[MAX_CONT][MAX_CARAC], int n)
{
	printf("Por favor, digite o nome do contato: \n");
	fgets(nome[n], MAX_CARAC, stdin);
	nome[n][strcspn(nome[n], "\n")] = '\0';
}

void addEMAIL(char email[MAX_CONT][MAX_CONT], int n)
{
	printf("Por favor, digite o email do contato: \n");
	fgets(email[n], MAX_CARAC, stdin);
	email[n][strcspn(email[n], "\n")] = '\0';
}

void addTEL(char tel[MAX_CONT][MAX_NUM], int n)
{
	printf("Por favor, digite o telefone do contato: \n");
	fgets(tel[n], MAX_CARAC, stdin);
	tel[n][strcspn(tel[n], "\n")] = '\0';
}

void adicionar(char nome[MAX_CONT][MAX_CARAC], char email[MAX_CONT][MAX_CONT],
							 char tel[MAX_CONT][MAX_NUM], int *contador)
{
	if(*contador == 49){
		printf("Quantidade máxima de 50 registros atingidos!\n");
		printf("\nRemova ao menos 1 registro para continuar\n");
		return;
	}
	addNOME(nome,*contador);
	addEMAIL(email,*contador);
	addTEL(tel,*contador);

	*contador += 1;

	printf("\nRegistro adicionado com sucesso!\n");
}

void mostrar(char nome[MAX_CONT][MAX_CARAC], char email[MAX_CONT][MAX_CONT],
							 char tel[MAX_CONT][MAX_NUM], int *contador)
{
	for(int i = 0; i < *contador; i++){
		printf("%d, %s, %s, %s;\n",i+1,nome[i],email[i],tel[i]);
	}
}

void alterar(char nome[MAX_CONT][MAX_CARAC], char email[MAX_CONT][MAX_CONT],
							 char tel[MAX_CONT][MAX_NUM], int *contador)
{
	mostrar(nome,email,tel,contador);
	puts("Escolha o numero de registro que gostaria de alterar ou uma letra para sair.");
	int n;
	puts("");
	scanf("%d", &n);
	limpaFluxo();
	n--;
	addNOME(nome,n);
	addEMAIL(email,n);
	addTEL(tel,n);
	printf("\nRegistro alterado com sucesso!\n");
}

void remover(char nome[MAX_CONT][MAX_CARAC], char email[MAX_CONT][MAX_CONT],
							 char tel[MAX_CONT][MAX_NUM], int *contador)
{
	*contador -= 1;
	printf("\nÚltimo registro removido com sucesso!\n");
}

void limpar(char nome[MAX_CONT][MAX_CARAC], char email[MAX_CONT][MAX_CONT],
							 char tel[MAX_CONT][MAX_NUM], int *contador)
{
	*contador = 0;
	printf("Agenda limpada com sucesso!\n");
}

void test(char nome[MAX_CONT][MAX_CARAC], char email[MAX_CONT][MAX_CONT],
							 char tel[MAX_CONT][MAX_NUM], int *contador, void f())
{
	if(*contador==0){
		puts("Não há nenhum registro na agenda.");
	} else {
		f(nome,email,tel,contador);
	}
}

int main(void) {
  int ctrl = 0;
	int contador = 0;
	char ch;


	char nome[MAX_CONT][MAX_CARAC]={};
	char tel[MAX_CONT][MAX_NUM]={};
	char email[MAX_CONT][MAX_CONT]={};

	while (ctrl == 0){
		printf("Digite a opção desejada:\n");
		printf("1 - Adicionar um novo numero\n");
		printf("2 - Mostrar agenda\n");
		printf("3 - Alterar um registro\n");
		printf("4 - Remover ultimo contato adicionado\n");
		printf("5 - Limpar agenda\n");
		printf("0 - Sair\n\n");

		scanf("%c",&ch);
		limpaFluxo();

		switch(ch){
			case '1':
				system("clear");
				adicionar(nome,email,tel,&contador);
				break;
			case '2':
				system("clear");
				test(nome,email,tel,&contador,mostrar);
				break;
			case '3':
				system("clear");
				test(nome,email,tel,&contador,alterar);
				break;
			case '4':
				system("clear");
				test(nome,email,tel,&contador,remover);
				break;
			case '5':
				system("clear");
				test(nome,email,tel,&contador,limpar);
				break;
			case '0':
				system("clear");
				printf("Você confirmou a saída do programa, tchau!\n");
				printf("\nE tenha um ótimo dia, professor Baroni!\n");
				ctrl++;
				break;
			default:
				printf("\nOpcao invalida! Tente novamente.\n");
		}
		printf("\nPressione ENTER para prosseguir\n\n");
		getchar();
		system("clear");
	}

  return 0;
}