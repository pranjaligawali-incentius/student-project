<template>
    <h5>Welcome TO The Student  Dashboard</h5>
   <Qform>
    <div class="q-pa-md">
    <div class="q-gutter-y-md column" style="max-width: 300px">
      <q-input filled v-model="name" label="Name " stack-label :dense="dense" />
      <q-input filled v-model="rollno" label="Roll no " stack-label :dense="dense" />
      <q-btn label="Submit" type="submit" color="primary"/>
      <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
      <q-item v-for="(item, index) in data" :key="item.id">
      <q-item-section>
        {{ index + 1 }}. {{ item.name }}
       </q-item-section>
      </q-item>
      </div>
  </div>
   </Qform> 
  

</template>
<script>
import { ref } from 'vue'
export default{
    setup(){
        return{
            /*text:ref(''),
            number:ref(''),*/
            dense:ref(false),
            student:ref({name:'',rollno:''}),
            data:ref([])
            
        }
        
        
    },methods:{
            submit(){
            this.data.push(this.student)
            this.student=""
        },
        reset(){
            this.student={
                name:'',
                rollno:''
            }
        }
        
    ,}

}


</script>
        