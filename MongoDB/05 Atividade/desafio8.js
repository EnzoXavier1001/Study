// Delete os lanches com menos de 50 curtidas
db.produtos.deleteMany(
  { 
    curtidas: { $lt: 50 },
  },
);

// Retorne o nome dos lanches que restaram no banco
db.produtos.find(
  {},
  { 
    _id: false,
    nome: true,
  },
);
