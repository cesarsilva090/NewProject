/* cadastro_alunos.c */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Aluno {
    char nome[50];
    int idade;
};

void cadastrar() {
    FILE *fp = fopen("alunos.txt", "a");
    struct Aluno a;

    printf("Nome do aluno: ");
    scanf(" %[^"]", a.nome);
    printf("Idade do aluno: ");
    scanf("%d", &a.idade);

    fprintf(fp, "%s %d\n", a.nome, a.idade);
    fclose(fp);
    printf("Aluno cadastrado com sucesso!\n");
}

void listar() {
    FILE *fp = fopen("alunos.txt", "r");
    char linha[100];
    printf("\nLista de alunos:\n");
    while (fgets(linha, sizeof(linha), fp)) {
        printf("%s", linha);
    }
    fclose(fp);
}

int main() {
    int opcao;
    do {
        printf("\n1. Cadastrar Aluno\n2. Listar Alunos\n3. Sair\nEscolha: ");
        scanf("%d", &opcao);
        switch (opcao) {
            case 1: cadastrar(); break;
            case 2: listar(); break;
            case 3: printf("Saindo...\n"); break;
            default: printf("Opção inválida!\n");
        }
    } while (opcao != 3);
    return 0;
}
