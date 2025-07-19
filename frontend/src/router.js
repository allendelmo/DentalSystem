import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import CreateTreatments from './pages/CreateTreatments.vue'
import CreatePatients from './pages/CreatePatients.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    // component: () => import('@/pages/CreatePatients.vue'),
    component: CreatePatients,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router