<template>
    <div id="listaOperadoras">
        <div id="operadoras-nome">
            <h3  :class="{'dark-title': isDarkMode, 'light-title': !isDarkMode}" class="identificador">Listagem com todas operadoras</h3>
            <table class="operadoras-table">
                <thead>
                    <tr>
                    <th>Registro ANS</th>
                    <th>CNPJ</th>
                    <th>Nome</th>
                    <th>Modalidade</th>
                    <th>UF</th>      
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="operadora in operadoras" :key="operadora.id">
                        <td>{{ operadora.registro_ans || 'N/A' }}</td>
                        <td>{{operadora.cnpj}} </td>
                        <td>{{operadora.nome_fantasia || 'N/A' }}</td>
                        <td>{{operadora.modalidade || 'N/A'}}</td>
                        <td>{{operadora.uf}} </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>   
   
</template>

<script>

import axios from 'axios';

export default{
    data(){
        return {
            operadoras: [],
            loading: false,
            error: null
        }
    },
    computed: {
      isDarkMode() {
        return document.body.classList.contains('dark');
      }
    },
    async mounted() {
        await this.fetchOperadoras();
    },
    methods: {
        async fetchOperadoras() {
            try {
                this.loading = true;
                const response = await axios.get('http://127.0.0.1:8000/operadoras');   
               
                this.operadoras = response.data || [];
                } catch (err) {
                    console.error('Erro na requisição:', err);
                    this.error = err.message || 'Erro desconhecido ao buscar operadoras';
                    this.operadoras = [];
                } finally {
                    this.loading = false;
                }
        },
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

#listaOperadoras {
  width: 70%;
  margin-left: 17rem;
  padding: 10px;
  box-sizing: border-box;
}

.identificador {
  font-size: 25px;
  font-weight: bold;
  color: black;
  margin-bottom: 40px;
  margin-top: 30px;
  justify-content: center;
  padding: 10px 27px;
  display: flex;
  align-items: center;
  text-align: center;
}

.table-container {
  width: 100%;
  overflow-x: auto;
}

.operadoras-table {
  width: 100%;
  min-width: 600px;
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

.operadoras-table tr:hover {
  background-color: #f5f5f5;
}

.light-title {
  color: black;
}

.dark-title {
  color: #f1f1f1;
}


.col-ans { width: 90px; }
.col-cnpj { width: 150px; }
.col-nome { width: 150px; }
.col-modalidade { width: 150px; }
.col-uf { width: 60px; }

@media (max-width: 768px) {
  .identificador {
    font-size: 20px;
    padding: 8px 15px;
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
    font-size: 18px;
    flex-direction: column;
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
}
</style>
