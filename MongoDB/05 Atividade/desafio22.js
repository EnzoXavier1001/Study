// Crie uma query que inclua um campo vendasPorDia em todos os 
// sanduíches. O valor deste campo deverá ser um array com sete posições
db.produtos.updateMany(
  {}, 
  { 
    $set: { vendasPorDia: [0, 0, 0, 0, 0, 0, 0] },
  },
);

// Crie uma query que incremente as vendas de Big Mac às quartas-feiras em 60
db.produtos.updateOne(
  { nome: "Big Mac" },
  { 
    $inc: { "vendasPorDia.3": 60 },
  },
);

// Crie uma query que incremente as vendas de todos os sanduíches de 
// carne do tipo bovino aos sábados em 120
db.produtos.updateMany(
  { tags: "bovino" },
  { 
    $inc: { "vendasPorDia.6": 120 },
  },
);

// Crie uma query que retorne o nome e vendasPorDia de todos os documentos
db.produtos.find(
  {},
  { 
    nome: true,
    vendasPorDia: true,
    _id: false,
  },
);
