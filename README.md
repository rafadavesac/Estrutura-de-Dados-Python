# Sistema de Gerenciamento de Estoque e Vendas (Terminal)

**Disciplina:** Estrutura de Dados com Python  
**Título do Trabalho:** Mini Sistema de Estoque com Persistência e Estruturas de Dados Clássicas  
**Integrantes:** Cristina Bisol Orso e Rafaela Laimer Davesac

---

## 📝 Descrição do Sistema
Este sistema foi desenvolvido para gerenciar o fluxo de mercadorias e vendas de um pequeno estabelecimento. Executado inteiramente via terminal, o software permite o cadastro de clientes e produtos, a realização de vendas com baixa automática de estoque, consulta de patrimônio e um histórico de operações com a funcionalidade de desfazer.

O foco principal do projeto é a aplicação prática de conceitos de Programação Orientada a Objetos e o uso de Estruturas de Dados, garantindo que os dados sejam preservados entre diferentes execuções por meio de um sistema de persistência automática.

---

## 🏗️ Estruturas de Dados Utilizadas

Para atender aos requisitos da disciplina, não foram utilizadas listas nativas do Python para o armazenamento principal. Em vez disso, implementamos:

1.  **Lista Simplesmente Encadeada (LSE):** Utilizada para gerenciar os cadastros de `Clientes` e `Produtos`. Cada elemento é um `Nodo` que aponta para o próximo, permitindo inserção dinâmica e percorrimento eficiente para listagens e buscas.
2.  **Fila (Queue):** Utilizada para o registro de `Vendas`. Segue a lógica FIFO (First-In, First-Out), garantindo que a ordem cronológica das vendas seja respeitada.
3.  **Pilha (Stack):** Utilizada para o sistema de Histórico e Desfazer. Segue a lógica LIFO (Last-In, First-Out). Cada operação relevante (cadastro ou venda) é empilhada; ao selecionar "Desfazer", o sistema remove o topo da pilha e reverte a ação (devolvendo estoque ou removendo registros).

---

## 💾 Persistência Automática em Arquivos

O sistema conta com um mecanismo de "Banco de Dados" baseado em arquivos de texto plano (`.txt`):

* **Salvamento Automático:** Toda alteração em memória (novo cadastro, nova venda ou operação desfeita) dispara automaticamente uma rotina de escrita que sobrescreve os arquivos com os dados atualizados.
* **Carregamento Inicial:** Ao iniciar, o sistema varre a pasta `/dados`. Caso os arquivos existam, os objetos são reconstruídos em memória, mantendo inclusive os vínculos entre Vendas, Clientes e Produtos por meio de seus IDs.
* **Resiliência:** O sistema utiliza caminhos absolutos baseados na localização do script, garantindo que a pasta de dados seja criada e lida corretamente independentemente de onde o terminal seja executado.

---

## 🛠️ Instruções de Execução

### Pré-requisitos
* Python 3.x instalado.
* Terminal ou Prompt de Comando.

### Como rodar
1. Clone o repositório:
   ```bash
   git clone [LINK_DO_SEU_REPOSITORIO]