// HTML Web Storage provê dois objetos para armazenamento de dados no cliente: cheve-valor
// 	- sessionStorage: Salva os dados no navegador, ou seja assim que fechar o navegador os dados serão deletados.
// 	- localStorage: Salva os dados sem data de expiração . Os dados não serão removidos quando o browser for fechado.
// Os mesmos comandos servem tanto pra localStorage quanto pra sessionStorage.

// Salvando:
localStorage.setItem("name", "Vincenzo [DEV]");
sessionStorage.setItem("name", "Vincenzo [DEV]");

// Acessando valor:
localStorage.getItem("name");
sessionStorage.getItem("name");

// Removendo valor:
localStorage.removeItem("name");
sessionStorage.removeItem("name");

// Limpando:
localStorage.clear();
sessionStorage.clear();

// Mudando o valor:
localStorage.nome_da_chave = "novo valor";
sessionStorage.nome_da_chave = "novo valor";
