<template>
  <div class="register">
    <div class="register-card" style="max-width: 300px">
      <h4>SignUp</h4>
    <q-input square outlined v-model="user.username" label="Username" />

    <q-input square outlined v-model="user.email" label="User Email" />
    <q-input square outlined v-model="user.password" label="User password" />
    
    <q-btn label="Register" type="submit" @click=register() color="primary" />
   
      </div>
      </div>
    
      </template>
<script>
import { ref } from 'vue'
export default{
    setup(){
        return{
            user:ref({
                username:'',
                email:'',
                password:'',
                
            }),
        }
       

        },
         methods:{
            register(){
                let self=this;
                self.$axios.post('/register',this.user)
                .then(function(response){
                     if(response.data.ok){
                        self.username=response.data.name
                        self.email=response.data.email
                        self.password=response.data.password
                        self.user={username:'',email:'',password:''}
                     }
                     else{
                       
                       self.$q.notify(response.data.message);
                     }
                       
                     
                     
                })

            }

    }
}
</script>
<style>
/*.register {
  display: flex;
  justify-content: center; 
  align-items: center;     
  min-height: 100vh;       
  background-color: #f4f7f6; 
}


.register-card {
  width: 100%;
  max-width: 700px;
  padding: 5px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}*/
</style>