import { createRouter, createWebHistory } from 'vue-router'
import ListaOperadoras from '@/views/ListaOperadoras.vue'
import Home from '@/views/HomeView.vue'

const routes = [
  { path: '/', redirect: '/home' }, 
  { path: '/home', name: 'Home', component: Home },
  { path: '/operadoras', name: 'ListaOperadoras', component: ListaOperadoras },
  { path: '/operadoras/buscar/', name: 'BuscarOperadora', component: Home }, 
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
