# Mesclador de PDF's em Python utilizando a biblioteca *PyPDF2*
Minha intenção com esse repositório é a prática contínua dos estudos em Python
A instalação da biblioteca pode ser acessada [aqui](https://pypi.org/project/PyPDF2).

## Como foi feito:
Através da biblioteca __*os*__ nativa do python é possível utilizar o método *listdir* para retornar o nome de todos os arquivos de uma pasta em forma de lista.

Com essa lista, basta percorrê-la e adicionar todos os arquivos com seus respectivos caminhos a uma instância de *PdfWriter* utilizando o método *append*.

Por final, basta utilizar o método *write* para definir o nome do novo arquivo e utilizar o método *close* para salvar o novo pdf
***