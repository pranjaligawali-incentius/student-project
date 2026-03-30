<template>
  <div class="login-page">
    <div class="login-card">
    <h4>Login Here !</h4>
    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <q-input
        filled
        v-model="username"
        label="Username*"
        
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />

     
    <q-input
    filled
    v-model="password"
    :type="passwordFieldType"
    label="Password *"
    lazy-rules
    :rules="[
      val => (val !== null && val !== '') || 'Please type your password',
      val => (val && val.length >= 8) || 'Password must be at least 8 characters'
    ]"
 />

     

      <div>
        <q-btn label="login" type="submit" color="primary" />
        <q-btn
          label="Register"
          type="register"
          color="primary"
          flat
          class="q-ml-sm"
        />
      </div>
    </q-form>
  </div></div>
</template>

<script>
import { useQuasar } from 'quasar'
import { ref } from 'vue'

export default {
  setup() {
    const $q = useQuasar()

    const username  = ref(null)
    const password = ref(null)
    

    return {
      username,
      password
    
    }
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
