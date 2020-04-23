<template>
  <v-app id="inspire">

    <NavBar v-bind:drawer_value="drawer"/>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Plutolio</v-toolbar-title>
    </v-app-bar>

    <v-footer app>
      <span>&copy; 2020</span>
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

    created () {
      this.$vuetify.theme.dark = true
    },

    
  }
</script>