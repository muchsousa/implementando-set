# Implementação do tipo de dado abstrato Set

## Complexidade de Algoritmos e Avaliação de Desempenho - Unilasalle 2023/02

### Objetivo
Compreender as escolhas de estruturas de dados e algoritmos utilizadas na implementação de soluções.

### Tarefas
O tipo de dado abstrato Set (conjunto) suporta as operações de inserção, remoção e consulta de elementos, além das operações de união, interseção e diferença entre conjuntos.

Nesse trabalho o aluno deve implementar as operações do tipo de dados abstratos Set, utilizando alguma estrutura de dados que permita a sua implementação de forma eficiente.

Deve constar no repositório de código um arquivo README contendo a justificativa para a escolha da estrutura de dados, e a complexidade de tempo e espaço esperada para cada uma das operações.

## Implementação

Implementado uma estrutura de dados do tipo "set", onde guarda valores únicos. Uilizando dicionários em python.

A implementação feita conta com a seguinte API:

### ``class Set``

#### ``#constructor()``

#### ``#contains(value: string | number): boolean``

Verifica se o valor informado faz parte dos valores armazenados pelo set.
Retorna True quando o valor existir e False quando valor não existir.

#### ``#insert(value: string | number): boolean``

Insere o valor no set.
Retorna True quando o valor for inserido e False quando já existir no set.

#### ``#remove(value: string | number): boolean``

Remove o valor recebido do set.
Retornando True quando o valor for removido com sucesso, e False quando o valor não existir no set.

#### ``#list_elements(): array``

Retorna como array os valores armazenados.

#### ``#union(other_set: Set): Set``

Realiza a união dos valores do set atual com os valores do set recebido por parametro, retornando um novo set.

#### ``#intersection(other_set: Set): Set``

Realiza a intersecção dos valores do set atual com os valores do set recebido por parametro, retornando um novo set.

#### ``#difference(other_set: Set): Set``

Realiza a diferença dos valores do set atual com os valores do set recebido por parametro, retornando um novo set.


### Referências

- https://www.geeksforgeeks.org/introduction-to-set-data-structure-and-algorithm-tutorials/
