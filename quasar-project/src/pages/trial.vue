<template >
    <div class="row">
    <div class="q-gutter-md" style="max-width: 300px">
   <h4>Student Registration Form</h4>
    <q-input dense filled v-model="student.name" label="Student Full Name" stack-label :dense="dense" />
 
    
     <div >
       <q-select dense v-model="student.age" :options="options" label="Student Age" />
     
    <div class="q-pa-md q-gutter-sm" >
    <div class="q-gutter-sm">
       
      <lable>Gender:</lable><q-radio dense v-model="student.gender" val="Male" label="Male" />
      <q-radio dense v-model="student.gender" val="Female" label="Female" />
      </div>
    </div>
     <div class="q-gutter-sm">
      <lable>Languages you know:</lable><br>
      <q-checkbox dense v-model="student.lang1" label="English" color="orange" />
      <q-checkbox dense v-model="student.lang2" label="Japneese" color="orange" />
      <q-checkbox dense v-model="student.lang3" label="Spanish" color="orange" />
      <q-checkbox dense v-model="student.lang4" label="Other" color="orange" />
    
 
    </div>
    <div class="q-pa-md q-gutter-lg">
    <div>
  <q-item v-for="(item, index) in FormData" :key="item.id"></q-item>
    <q-toggle
        v-model="student.value"
        color="green"
        label="The information you have provided is totally correct ?",
         left-label
      />
       
  </div>
      </div>
  <div class="q-pa-md q-gutter-sm">
     
    <q-btn v-if="curridx===null" color="blue" label="ADD" @click.prevent="Submit()"/>
    
     
    <br>
   
  </div> 

</div></div></div>

<div class="q-pa-md">
    <q-table
      flat bordered
      title="Student Data"
      :rows="FormData"
      :columns="columns"
      row-key="name"
    >
      <template v-slot:body="props">
        <q-tr :props="props" >
          <q-td key="name" :props="props">
            {{ props.row.name }}
          </q-td>
          <q-td key="age" :props="props">
            <q-badge color="green">
              {{ props.row.age }}
            </q-badge>
          </q-td>
          <q-td key="gender" :props="props">
            <q-badge color="purple">
              {{ props.row.gender }}
            </q-badge>
          </q-td>
          <q-td key="lang1" :props="props">
            <q-badge color="orange">
              {{ props.row.lang1 ?'English':''}}, {{ props.row.lang2 ? 'Japneese':'' }}, {{ props.row.lang3  ? 'Spanish':''}}  ,{{ props.row.lang4 ? 'Other':'' }}
            </q-badge>
          </q-td>
          
          <q-td key="value" :props="props">
            <q-badge color="orange">
              {{ props.row.value }}
              
            </q-badge>
          </q-td>
          <q-td key="action" :props="props">
            <q-badge color="white">
                <q-btn  color="blue" label="Edit" @click.prevent="EditStudent(props.rowIndex)" prompt="true"/>
                  <q-btn color="red" label="Delete" @click="demo=true" />
            </q-badge>
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
  <q-dialog v-model="prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Edit Form</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input filled v-model="Editstud.name" label="Full Name" stack-label :dense="dense" autofocus @keyup.enter="prompt = false" />
          <q-select filled v-model="Editstud.age" :options="options" label="Age" stack-label :dense="dense" autofocus @keyup.enter="prompt = false"  />
           <lable>Gender:</lable>
        <q-radio filled v-model="Editstud.gender"  val="Male" label="Male" stack-label :dense="dense" autofocus @keyup.enter="prompt = false" />
         <q-radio filled v-model="Editstud.gender"  val="Female" label="Female" stack-label :dense="dense" autofocus @keyup.enter="prompt = false" />
       
      
      <lable>Languages you know:</lable><br>
      <q-checkbox v-model="Editstud.lang1" label="English" color="orange" />
      <q-checkbox v-model="Editstud.lang2" label="Japneese" color="orange" />
      <q-checkbox v-model="Editstud.lang3" label="Spanish" color="orange" />
      <q-checkbox v-model="Editstud.lang4" label="Other" color="orange" />
  
       <q-toggle
        v-model="Editstud.value"
        color="green"
        label="The information you have provided is totally correct ?",
         left-label
         stack-label :dense="dense" autofocus @keyup.enter="prompt = false"

      />
        </q-card-section>
        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn @click="EditItem()" flat label="Edit " v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog v-model="demo" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Are you sure you want to delete </div>
        </q-card-section>

        

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="No" v-close-popup />
          <q-btn @click="deleteStud(index)" flat label="Yes" v-close-popup  />
        </q-card-actions>
      </q-card>
    </q-dialog>
 
</template>
<script>
import { ref } from 'vue'
export default {
  setup () {
    
    return {
      student:ref({ 
        name: '',
        gender:'',
        age:null,
        model: null,
        value: false,
        lang1: false,
        lang2: false,
        lang3: false,
        lang4: false,
        
      }
    
    ),
    options: ref(['12', '13', '14', '15', '16']),
    curridx:null,
    columns : ref( [
      {
    name: 'name',
    required: true,
    field:'name',
    label: 'Student Name',
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'age', label: 'Age', field: 'age', sortable: true },
  { name: 'gender', field:'gender', label: 'Gender'},
  { name: 'lang1',field:'lang1', label: 'Language'  },
 
  { name: 'value', field:'value' ,label: 'Correct Info' },
  { name: 'action', field:'action' ,label: 'Action' }

  
]) ,
 FormData:ref([]),


 Editstud:ref({ 
        name: '',
        gender:'',
        age:null,
        model: null,
        
        
        value: false,
        lang1: false,
        lang2:false,
        lang3:false,
        lang4:false,
        
      }
    
    ),

      prompt: ref(false),
      demo:ref(false),
     
}
    },
    methods:{
      
        Submit(){
          if(this.curridx===null){
             this.FormData.push({...this.student})
              this.student={
            name:'',
            age:'',
            gender:'',
            lang1:'',
            value:false
          }
           } 
        } ,
        EditStudent(index){
        
        this.prompt=true

          this.Editstud={...this.FormData[index]}
          
          this.curridx=index
        },
        EditItem(){
          this.FormData[this.curridx]={...this.Editstud}
          this.curridx=null
          this.student={
            name:'',
            age:'',
            gender:'',
            lang1:'',
            value:false
          }
        },
        deleteStud(index){
           this.FormData.splice(index,1)
        }     
  }
}
//
</script>
<style scoped>

.row {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: 12vh;
  background-color: #f4f7f6; 
  padding: 40px 20px;
  margin: 0 auto;
}


.q-gutter-md {
  background: #ffffff !important; 
  padding: 30px !important;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08); 
  max-width: 500px !important;
  width: 100%;
  margin: 0 auto ;
  text-align: left ; 
}


h4 {
  color: black; 
  font-weight: 700;
  margin-top: 0;
  margin-bottom: 25px;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
}


lable {
  font-weight: 600;
  color: #555;
  display: inline-block;
  margin-top: 10px;
  margin-bottom: 5px;
}

.q-pa-md {
  max-width: 1000px;
  margin: 20px auto;
  background: white;
  border-radius: 8px;
}


.q-gutter-sm {
  padding-top: 2px;
  padding-bottom: 2px;
  
}

.q-pt-none{
  max-width: 1000px;
  margin: 20px auto;
  background: white;
  border-radius: 8px;

}
.q-btn {
  border-radius: 6px;
    font-weight: bold;
    display: block;
  margin: 0 auto;
 
}
.q-table {
  border-radius: 20px;
  

}


</style>
