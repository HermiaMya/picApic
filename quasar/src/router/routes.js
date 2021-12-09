
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },

  {
    path:'/page1',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/page1', component: () => import('pages/page1.vue')}
    ]
  },

  {
    path:'/page2',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/page2', component: () => import('pages/page2.vue')}
    ]
  },

  {
    path:'/page3',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/page3', component: () => import('pages/page3.vue')}
    ]
  },

  {
    path:'/page4',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/page4', component: () => import('pages/picApic.vue')}
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
