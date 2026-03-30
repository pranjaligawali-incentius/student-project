<template>
  <q-layout view="lHh Lpr lFf">
   
   
      <q-list>
        
        <!--<q-scroll-area class="fit">-->
          <q-list>
            
            
            <template v-for="(menuItem, index) in menuList" :key="index">
            
              <q-item clickable :active="menuItem.label === ''" v-ripple>
                <q-item-section avatar>
                  <q-icon :name="menuItem.icon" />
                </q-item-section>
                <q-item-section  @click="this.$router.push(menuItem.path)">
                  {{ menuItem.label }}
                </q-item-section>
              </q-item>
              <q-separator :key="'sep' + index"  v-if="menuItem.separator" />
            </template>

          </q-list>
        <!--</q-scroll-area>-->
      </q-list>
    

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
//import EssentialLink from 'components/EssentialLink.vue'

const menuList = [
  
  {
    //icon:'login',
   // label:'Login',
   separator:true,
    path:'/login'
  }

]

export default defineComponent({
  name: 'authentication',

  
  setup () {
    return {
      
      menuList,
      
    }
  },
 
})
</script>
