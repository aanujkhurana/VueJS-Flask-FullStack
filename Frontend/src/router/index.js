import { createRouter, createWebHistory } from 'vue-router'
import Shark from '../views/Shark.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'shark',
      component: Shark
    },
  ]
})

export default router
