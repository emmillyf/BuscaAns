<template>
   <div id='container'>
        <div id='buscar'>
            <label for="searchInput">
                <h3 class="identificador">Filtrar Operadoras</h3>
             <input :value="text" @input="event => text = event.target.value" placeholder="Cidade, UF, Modalidade ou Nome">
            </label>
            <button class="filtrar" @click="$emit('increaseBy', 1)">FILTRAR</button>
            <button class="limpar" @click="$emit('increaseBy', 1)">LIMPAR</button>
        </div>
    </div>

</template>

<script>

</script>

<style scoped>


*{
    font-family: "Montserrat", sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

#container {
  display: flex;
  justify-content: center; 
  align-items: center; 
  height: 400px; 
  /* background: yellow; */

}

#buscar{
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding: 27px 22px;
    height: 50px;
    /* background: red; */
}

#buscar input{
    width: 700px;
    height: 46px;
    border: 0;
    border-bottom: 2px solid #ccc;
    border-radius: 1px;
    color: #4b4b4b;
    border-color: none;
    position: relative;
    padding: 5px 10px;
    outline: none;
}

.identificador {
    font-size: 25px;
    font-weight: bold;
    color: black; /* Altere para a cor desejada */
    margin-bottom: 20px;
}

.filtrar{
    width: 93px;
    height: 35px;
    border: none;
    border-radius: 3px;
    background: #980020;
    color: white;
    border-color: none;
    outline: none;
    margin-left: 20px;
}

.limpar{
    width: 93px;
    height: 35px;
    border: none;
    border-radius: 3px;
    background: #5f6061;
    color: white;
    border-color: none;
    outline: none;
    margin-left: 20px;
}

</style>