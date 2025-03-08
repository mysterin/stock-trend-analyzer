import { createRouter, createWebHistory } from 'vue-router'
import AppLayout from '../components/AppLayout.vue'

const routes = [
  {
    path: '/',
    component: AppLayout,
    redirect: 'dashboard',
    children: [
      {
        path: 'dashboard',
        meta: { title: '首页' },
        component: () => import('@/views/AppDashboard')
      },
      {
        path: 'astock',
        redirect: '/astock/spot',
        meta: { title: 'A股相关' },
        children: [
          {
            path: 'spot',
            meta: { title: 'A 股实时数据' },
            component: () => import('@/views/StockZhASpot')
          },
          {
            path: 'hist',
            meta: { title: 'A 股历史数据' },
            component: () => import('@/views/StockZhAHist')
          }
        ]
      }
    ]
  },
  // 捕获所有未匹配路径的路由
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router