Integrantes:
Heverton de Oliveira Lourenço, José Adrian Torres dos Santos e Pedro Augusto Santos da Silva

Conteúdos de consulta:
Adrian, Heverton e Pedro:

Material disponibilizado no classroom e replit para desenvolver a busca sequencial e busca binaria.
Documentação do timeit, para melhor compreensão do seu uso. Disponível em: https://docs.python.org/3/library/timeit.html

Dificuldades:

Heverton: 
Entender o uso do timeit, necessitei de alguns testes para entender o seu funcionamento e conseguir implementar no projeto.
Uma outra "dificuldade", foi tentar testar o desempenho com uma lista de 1 bilhão de elementos. O computador simplesmente travou e 
tive que forçar o desligamento. O projeto não pede, mas tive a curiosidade de testar. 

Percebi que dependendo do valor digitado pelo usuário era possivel ocorrer um erro pois o tamanho*1.25 (linha 31, função valores aleatorios) poderia ser um tipo float, então usei a função floor para arredondar o número.

Pensei que colocar o parâmetro "hibrida" como opcional na função de busca binária, era a melhor forma para evitar a chamada da busca sequencial dentro do próprio escopo da função. Retornando a lista fatiada de tamanho menor ou igual ao valor recebido pelo parâmetro "hibrida", dá ao programador maior liberdade para implementar outro tipo de busca. Algo que não seria possivel caso fosse feita a  chamada da função de busca sequencial e ela não existisse no código.

A implementação acima gerou outro problema, a função de busca binaria poderia retornar "True", antes de fatiar a lista. Gerando erro pois a busca sequencial receberia um boolean ao invés de uma lista em si. Então o uso da função "isinstance()" foi implementado, ela garante que só será feita a busca sequencial quando a lista fatiada for do tipo "list".
    

Pedro: a estrutura de busca binaria não é tão complexa mas me confundi um pouco com o funcionamneto da mesma no codigo , compreendi melhor usando debug.

Adrian:
