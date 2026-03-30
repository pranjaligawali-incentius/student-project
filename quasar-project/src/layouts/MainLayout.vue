<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>

        
        
         <q-btn color="white" text-color="black" label="Logout" />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

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
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const menuList = [
  {
    icon:'person',
    label:'Student',
    separator: true,
    path:'/student'
  },
  {
    icon: 'classroom',
    label: 'Classroom',
    separator: true,
    path:'/classroom'
  },{
    icon:'table',
    label:'Table',
    separator:true,
    path:'/table'
  },
  {
    icon:'assignment',
    label:'Assignment',
    separator:true,
    path:'/assignment'
  }
 



]

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup () {
    return {
      drawer: ref(false),
      menuList,
      leftDrawerOpen: ref(false),
    }
  },
  methods: {
     toggleLeftDrawer () {
        this.leftDrawerOpen = !this.leftDrawerOpen
      }
  },
})
</script>
