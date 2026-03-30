<template>
  <q-page class="flex flex-center bg-grey-1">
    <q-card style="width: 450px; padding: 20px; border-radius: 8px">
      <q-card-section>
        <div class="text-h6 text-primary">Edit Student Profile</div>
        <!--<div class="text-caption">Update information for ID: {{ studentId }}</div>-->
      </q-card-section>

      

      <q-card-section>
        <q-form @submit="saveChanges" class="q-gutter-md">
          <q-input filled v-model="student.name" label="Full Name" />
          <q-input filled v-model="student.age" label="Age" type="number" />
          <q-select filled v-model="student.gender" :options="['Male', 'Female']" label="Gender" />
          
        <!-- <q-input filled v-model="student.languages" label="Languages" hint="Comma separated" />-->
          
         <br>

      <lable>Languages you know:</lable><br>
      <q-checkbox dense v-model="student.languages" val="English" label="English" color="orange" />
      <q-checkbox dense v-model="student.languages" val="Japneese" label="Japneese" color="orange" />
      <q-checkbox dense v-model="student.languages" val="Spanish" label="Spanish" color="orange" />
      <q-checkbox dense v-model="student.languages" val="Other" label="Other" color="orange" />
  

  
  
    
        <q-toggle
        v-model="student.value"
        color="green"
        label="The information you have provided is totally correct ?",
         left-label
 />
        
          <div class="row justify-between q-mt-lg">
            <q-btn label="Cancel" color="grey" flat @click="$router.push('/assignment')" />
            <q-btn label="Save Updates" type="submit" color="blue" />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

export default {
  setup() {
    const route = useRoute()
    const router = useRouter()
    const studentId = route.params.id 

    const student = ref({
      name: '',
      age: '',
      gender: '',
      languages: [],
      value:false
    })

    
    axios.get(`http://localhost:5000/api/get_student/${studentId}`)
      .then(response => {

        
        student.value = response.data
      })
      

    const saveChanges = () => {
      axios.post(`http://localhost:5000/api/edit/${studentId}`, student.value)
        .then(response => {
          if (response.data.ok) {
            router.push('/assignment') 
          }
        })
        
    }

    return {
      student,
      studentId,
      saveChanges
    }
  },
}
</script>