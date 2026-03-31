import { defineStore, acceptHMRUpdate } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    session:{
        username:'',
        email:'',
        isLogin:false
    }
  }),

  getters: {
   
  },

  actions: {
    setLoginSession(data) {
      this.session.username=data.username
      this.session.email=data.email
      this.session.isLogin=true 
    },
    destroyLoginSession(data){
        this.session.username=''
        this.session.email=''
        this.session.isLogin=false
    }
  }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCounterStore, import.meta.hot))
}
