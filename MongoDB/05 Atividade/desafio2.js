// Ordene a coleção produtos pela quantidade de lanches vendidos em ordem
// crescente, mostrando apenas o nome e a quantidade de lanches vendidos
db.produtos.find(
  {},
  { 
    nome: true,
    _id: false,
    vendidos: true,
  },
)
.sort({ vendidos: 1 });
