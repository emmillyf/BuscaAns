<template>
<div id="app">
    <HomePage />

</div>

</template>

<script>

import HomePage from './views/HomeView.vue'

export default {
  name: 'App',
    components: {
      HomePage
  }, 
}
</script>

<style>

* {
  margin: 0;
  padding: 0;
  box-sizing:border-box;

}

/* .app{
  width: 100%;
  min-height: 100%;
  background: #f3f3f3;
  color: #152828;
} */

/* .dark{
  background: #152828;
  color: #F3F3F3;
} */

</style>