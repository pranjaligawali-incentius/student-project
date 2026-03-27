<template>
  <div class="q-pa-md">
    <q-table
      title="Student"
      :rows="rows"
      :columns="columns"
      row-key="name"
    />
  </div>
</template>

<script>
const columns = [
  {
    name: 'name',
    required: true,
    label: 'Student Name',
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'Roll No', align: 'center', label: 'Rollno', field: 'rollno', sortable: true },
  { name: 'Class', label: 'Class', field: 'grade' },
  { name:'school', label:'School', field:'school'},


]

const rows = [
  {
    name: 'Pranjali Gawali',
   rollno: 1,
    class: 'F.Y',
    grade:'A',
    school:'abc'
  
  },
   {
    name: 'shreya',
   rollno: 15,
    class: 'F.Y',
    grade:'A',
    school:'abc'
  
  }, {
    name: 'Shruti',
   rollno: 29,
    class: 'F.Y',
    grade:'D',
    school:'abc'
  
  },
   {
    name: 'Shrushti',
   rollno: 23,
    class: 'F.Y',
    grade:'C',
    school:'abc'
  
  },
   {
    name: 'Kavya',
   rollno: 3,
    class: 'F.Y',
    grade:'B',
    school:'abc'
  
  },
  {
    name: 'ashwini',
   rollno: 2,
    class: 'F.Y',
    grade:'A',
    school:'abc'
  
  },
   {
    name: 'siddhi',
   rollno: 3,
    class: 'F.Y',
    grade:'A',
    school:'abc'
  
  }, {
    name: 'shweta',
   rollno: 9,
    class: 'F.Y',
    grade:'D',
    school:'abc'
  
  },
   {
    name: 'riya',
   rollno: 23,
    class: 'F.Y',
    grade:'C',
    school:'abc'
  
  },
   {
    name: 'kiya',
   rollno: 3,
    class: 'F.Y',
    grade:'B',
    school:'abc'
  
  }
 
]

export default {
  setup () {
    return {
      columns,
      rows
    }
  }
}
</script>
