O RTL tem como objetivo ver o comportamento => vendo se é ou não renderizado na tela

**Instalando o RTL**: `npm install --save-dev @testing-library/react`

**Documentação**: [Link](https://testing-library.com/docs/)

### Exemplo de Sintax:
```
import React from 'react';
import { render } from '@testing-library/react'; 
import App from './App';

it('renders learn react link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```
