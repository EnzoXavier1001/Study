// Crie uma query que faça em todos os documentos a ordenação dos valores 
// do array valoresNutricionais pelo campo percentual de forma decrescente
db.produtos.updateMany(
  {},
  {
    $push: {
      valoresNutricionais: {
        $each: [],
        $sort: { percentual: -1 },
      },
    },
  },
);

// Crie uma query que retorne o nome e valoresNutricionais de todos os documentos
db.produtos.find(
  {},
  {
    nome: true,
    valoresNutricionais: true,
    _id: false,
  },
);
