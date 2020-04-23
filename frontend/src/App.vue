<template>
  <v-app id="inspire">

    <NavBar v-bind:drawer_value="drawer"/>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Plutolio </v-toolbar-title>
    </v-app-bar>
    <v-content class="mx-4">
    <router-view @nightModeChanged="changeNightMode($event)"></router-view>
    </v-content>

    <v-footer app>
      <span>&copy; 2020 <h1> </h1></span>
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar.vue'

  export default {
    props: {
      source: String,
    },
    components: {
      NavBar
    },
    data: () => ({
      drawer: null,
    }),

    methods: {
      changeNightMode(mode) {
        // console.log("Need to chnge!", mode)
        this.$vuetify.theme.dark = mode
      }
    },

    created () {
      this.changeNightMode(true)
    },


  }
</script>