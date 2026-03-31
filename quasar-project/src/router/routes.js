const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path:'/student' , component:() => import('pages/Student.vue')      },
     // { path:'/classroom' , component:() => import('pages/Classroom.vue')     },
      { path:'/table' , component:() => import('pages/table.vue')     },
      {path:'/assignment', component:()=>import('pages/Assignment.vue')},
    { path: 'edit/:id', component: () => import('pages/Editpage.vue') }
    ]
  },
  {
    path:'/',
    component:()=>import('layouts/authentication.vue'),
    children:[
    {path:'/login',component:()=>import('pages/login.vue')},
    {path:'/signup',component:()=>import('pages/signup.vue')}
    ]
  }
,
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
