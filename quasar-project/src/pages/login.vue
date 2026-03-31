<template>
  <div class="login-page">
    <div class="login-card">
    <h4>Login Here !</h4>
     
    <q-input square outlined v-model="user.username" label="Username" />

    <q-input square outlined v-model="user.password" label="User password" />
    
    <q-btn label="Login" type="submit" @click.prevent=login() color="primary" />
   
  </div></div>

</template>

<script>
import { SessionStorage, useQuasar } from 'quasar'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default {
  setup() {
    

    return {
      user:ref({ 
        username:'',
        password:''

      })
    }
  },
  methods:{
    login(){
      let self=this;
      self.$axios.post("/login",self.user)
      .then(function(response){
        if(response.data.ok){
          self.username=response.data.username
          self.email=response.data.email
          self.$q.notify(response.data.message)
        }else{
          self.$q.notify(response.data.message)
        }
        
      })
      
    },
    


  }
}
</script>
<style>

.login-page {
  display: flex;
  justify-content: center; 
  align-items: center;     
  min-height: 100vh;       
  background-color: #f4f7f6; 
}


.login-card {
  width: 100%;
  max-width: 400px;
  padding: 30px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}
</style>
