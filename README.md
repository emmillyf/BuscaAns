<!DOCTYPE html>
<html lang="pt-BR">
<body>

<h1>Teste de API - Análise de Operadoras de Saúde</h1>

<p>Este projeto consiste em uma aplicação que permite realizar buscas textuais em um conjunto de dados de operadoras de saúde e exibir os resultados em uma interface web interativa desenvolvida com Vue.js. O backend foi desenvolvido em Python, utilizando o Uvicorn como servidor ASGI e configurado com variáveis de ambiente.</p>

<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Frontend</strong>: Vue.js</li>
  <li><strong>Backend</strong>: Python com FastAPI (servidor ASGI) e Uvicorn</li>
  <li><strong>Banco de Dados</strong>: CSV (operadoras_ans.csv)</li>
  <li><strong>Postman</strong>: Para testar as APIs</li>
  <li><strong>Variáveis de Ambiente</strong>: Para configurações sensíveis (ex: banco de dados)</li>
</ul>

<h2>🚀 Como Rodar o Projeto Localmente</h2>

<h3>1. Pré-requisitos</h3>
<p>Antes de rodar o projeto, você precisará ter os seguintes componentes instalados:</p>
<ul>
  <li><strong>Python 3.11</strong> ou superior</li>
  <li><strong>Node.js e npm</strong> (para rodar o Vue.js)</li>
  <li><strong>Postman</strong> (opcional, mas recomendado para testar a API)</li>
  <li><strong>pip</strong> (gerenciador de pacotes do Python)</li>
</ul>

<h3>2. Clonar o Repositório</h3>
<p>Clone o repositório do projeto para o seu ambiente local:</p>
<pre><code>git clone https://github.com/emmillyf/BuscaAns.git
cd BuscaAns</code></pre>

<h3>3. Configuração do Backend</h3>

<h4>3.1. Criar e Ativar um Ambiente Virtual (opcional, mas recomendado)</h4>
<p>Crie e ative um ambiente virtual para isolar as dependências do projeto Python:</p>
<pre><code>python3 -m venv venv
# Para ativar o ambiente virtual:
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate</code></pre>

<h4>3.2. Instalar as Dependências do Backend</h4>
<p>Instale as dependências necessárias para o backend utilizando <strong>pip</strong>:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h4>3.3. Variáveis de Ambiente</h4>
<p>Crie um arquivo <code>.env</code> na raiz do projeto com a seguinte configuração de variáveis de ambiente:</p>
<pre><code># Preencha com suas informações

DB_USER=postgres
DB_PASSWORD=2203
DB_HOST=localhost
DB_PORT=5432
DB_NAME=despesas_op</code></pre>
<p>Essas variáveis serão utilizadas para conectar o servidor com o banco de dados. O arquivo <code>operadoras_ans.csv</code> deve estar localizado na raiz do projeto.</p>

<h4>3.4. Rodar o Servidor Backend</h4>
<p>Com as dependências instaladas e o ambiente configurado, você pode rodar o servidor FastAPI com o Uvicorn:</p>
<pre><code>cd app
uvicorn main:app --reload</code></pre>
<p>Isso vai iniciar o servidor backend na URL <code>http://127.0.0.1:8000</code>.</p>

<h3>4. Configuração do Frontend (Vue.js)</h3>

<h4>4.1. Instalar as Dependências do Frontend</h4>
<p>Para rodar a interface Vue.js, navegue até a pasta do frontend (geralmente a pasta <code>frontend</code>) e instale as dependências com npm:</p>
<pre><code>cd frontend
npm install</code></pre>

<h4>4.2. Rodar o Servidor Frontend</h4>
<p>Após a instalação das dependências, você pode rodar o servidor de desenvolvimento do Vue.js:</p>
<pre><code>npm run serve</code></pre>
<p>A aplicação estará disponível em <code>http://localhost:8080</code>.</p>

<h3>7. Roteamento e Funcionalidade da API</h3>
<p>O servidor Python oferece várias rotas para realizar buscas textuais nas operadoras de saúde e realizar outras operações:</p>

<ul>
  <li><strong>GET /operadoras/</strong>: Retorna a lista completa de operadoras de saúde cadastradas no banco de dados.</li>
  <li><strong>GET /operadoras/{id}</strong>: Retorna as informações de uma operadora específica a partir do <code>id</code> da operadora.</li>
  <li><strong>GET /operadoras/buscar/</strong>: Permite buscar operadoras de saúde a partir de um termo de pesquisa. A busca pode ser realizada considerando informações como nome, UF, CNPJ e modalidade da operadora. A busca é paginada.</li>
  <li><strong>GET /download-csv</strong>: Baixa um arquivo CSV contendo dados das operadoras de planos de saúde ativas da ANS.</li>
</ul>
<h2>⚠️ Observação sobre Docker</h2>
<p>Os arquivos de configuração do Docker estão incluídos no projeto para testes em containers. O uso do Docker é opcional, mas pode ser uma alternativa útil para rodar a aplicação em ambientes isolados. Para mais informações sobre como usar Docker, consulte os arquivos <code>Dockerfile</code> e <code>docker-compose.yml</code> na raiz do projeto.</p>

</body>
</html>
