// App
import React from 'react';
import { Router } from 'react-router-dom';
import { createMemoryHistory } from 'history';
import { render } from '@testing-library/react';

const renderWithRouter = (component) => {
  const history = createMemoryHistory();
  return ({
    ...render(<Router history={history}>{component}</Router>), history,
  });
};
export default renderWithRouter;

// src/App.test.js:
import React from 'react';
import { screen } from '@testing-library/react';
import renderWithRouter from './renderWithRouter'; // <== Importamos o renderWithRouter
import App from './App';

it('Testando se renderiza o componente App(HOME => "/")', () => {
  renderWithRouter(<App />);

  const homeTitle = screen.getByRole('heading', {
    name: 'Você está na página Início',
  });
  expect(homeTitle).toBeInTheDocument();
});
