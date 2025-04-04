<template>
    <div id='container' :class="{ dark: isDark, collapsed: isCollapsed }">
      <div id='buscar'>
        <label for="searchInput">
          <h3  :class="{'dark-title': isDarkMode, 'light-title': !isDarkMode}" class="identificador">Filtrar Operadoras</h3>
          <input 
            id="searchInput"
            v-model="searchTerm"
            @keyup.enter="fetchOperadoras"
            placeholder="Nome, Modalidade, CNPJ, UF">
        </label>
        
        <button class="filtrar" @click="fetchOperadoras">FILTRAR</button>
        <button class="limpar" @click="clearSearch">LIMPAR</button>
      </div>

      <div v-if="loading" class="loading"></div>
      <div v-else-if="error" class="error">{{ error }}</div>

      <div v-else  id="listaOperadoras">
        <div  id="operadoras-nome">
          <table class="operadoras-table" v-if="operadoras.length">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Modalidade</th>
                <th>CNPJ</th>
                <th>UF</th>      
              </tr>
            </thead>
            <tbody>
              <tr v-for="op in operadoras" :key="op.registro_ans">
                <td>{{ op.nome_fantasia }}</td>
                <td>{{ op.modalidade }}</td>
                <td>{{ op.cnpj }}</td>
                <td>{{ op.uf }}</td>
              </tr>
            </tbody>
          </table>
          <div  v-else-if="hasSearched && !loading" class="sem-resultados">
            Nenhuma operadora encontrada. Tente ajustar seus filtros.
          </div>
        </div>
      </div>
  
      <div id="paginas" v-if="operadoras.length > 0">
        <button class="anterior" @click="prevPage" :disabled="currentPage === 1">Anterior</button>
        <button class="proximo" @click="nextPage" :disabled="operadoras.length < itemsPerPage">Próxima</button>
      </div>
    </div>
  </template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      operadoras: [],
      searchTerm: '',
      currentPage: 1,
      itemsPerPage: 20,
      loading: false,
      error: null,
      hasSearched: false
    };
  },
  computed: {
      isDarkMode() {
        return document.body.classList.contains('dark');
      }
  },
  methods: {
    async fetchOperadoras() {
    const termoLimpo = this.searchTerm.trim();

    if (!termoLimpo) {
    this.operadoras = [];
    this.hasSearched = true;
    return;
    }

    this.loading = true;
    this.error = null;
    this.hasSearched = true;

    try {
    const params = {
        termo: termoLimpo,
        pagina: this.currentPage,
        por_pagina: this.itemsPerPage
    };

    const response = await axios.get('http://127.0.0.1:8000/operadoras/buscar/', {
        params,
        paramsSerializer: {
        indexes: null
        }
    });

    this.operadoras = response.data || [];
    } catch (err) {
    console.error(err);
    this.error = 'Erro ao buscar operadoras.';
    } finally {
    this.loading = false;
    }
    },
      nextPage() {
        this.currentPage++;
        this.fetchOperadoras();

      },
      prevPage() {
        if (this.currentPage > 1) {
              this.currentPage--;
              this.fetchOperadoras();
          }
      },
      clearSearch() {
        this.searchTerm = '';
        this.currentPage = 1;
        this.operadoras = [];   
        this.hasSearched = false;
      }
  }
};
</script>

<style scoped>
* {
  font-family: "Montserrat", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#container {
  display: flex;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
  margin-left: 15rem;
  padding: 20px;
}

#buscar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 27px 22px;
  gap: 20px;
}

#buscar input {
  width: 700px;
  max-width: 100%;
  height: 46px;
  border: 0;
  border-bottom: 2px solid #ccc;
  border-radius: 1px;
  color: #4b4b4b;
  padding: 5px 10px;
  outline: none;
}

.identificador {
  font-size: 25px;
  font-weight: bold;
  color: black;
  margin-bottom: 20px;
  text-align: center;
}

.filtrar,
.limpar {
  width: 93px;
  height: 35px;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
}

.filtrar {
  background: #980020;
}

.limpar {
  background: #5f6061;
}

#listaOperadoras {
  width: 100%;
  border-collapse: collapse;
  display: flex;
  align-items: center;
  justify-content: center;
}

.table-container {
  width: 100%;
  overflow-x: auto;
}

.operadoras-table {
  min-width: 600px;
  width: 100%;
  max-width: 100%;
  margin: 0 auto;
  border-collapse: collapse;
  background: #f7eeed;
  font-size: 0.9em;
}

.operadoras-table th,
.operadoras-table td {
  padding: 8px 10px;
  text-align: left;
  border: 1px solid #ddd;
}

.operadoras-table th {
  background-color: #AD102F;
  border: 0;
  border-top: 2px solid #ccc;
  color: white;
  font-weight: bold;
}

#paginas {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 15px;
  flex-wrap: wrap;
  gap: 10px;
}

#paginas .anterior {
  margin-right: 9px;
}

#paginas button {
  width: 93px;
  height: 35px;
  border: none;
  border-radius: 5px;
  background: #980020;
  color: white;
  cursor: pointer;
}

.sem-resultados {
  padding: 20px;
  text-align: center;
  color: #666;
  font-style: italic;
}

.light-title {
  color: black;
}

.dark-title {
  color: #f1f1f1;
}

.col-ans { width: 90px; }
.col-cnpj { width: 150px; }
.col-nome { width: 90px; }
.col-modalidade { width: 120px; }
.col-uf { width: 50px; }

@media (max-width: 768px) {
  #buscar {
    flex-direction: column;
    align-items: center;
  }

  #buscar input {
    width: 100%;
    max-width: 90%;
  }

  .operadoras-table {
    font-size: 0.8em;
    min-width: 100%;
  }

  .operadoras-table th,
  .operadoras-table td {
    padding: 6px 8px;
  }

  .col-cnpj,
  .col-modalidade {
    display: none;
  }
}

@media (max-width: 480px) {
  .identificador {
    font-size: 20px;
  }

  .operadoras-table {
    font-size: 0.75em;
    min-width: 100%;
  }

  .col-nome {
    width: auto;
  }

  .col-ans,
  .col-uf {
    font-size: 0.75em;
  }

  .col-cnpj,
  .col-modalidade {
    display: none;
  }

  #paginas button {
    width: 100%;
    max-width: 200px;
  }
}
</style>