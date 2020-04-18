<template>
  <div class="hello">
    <h1>Current positions</h1>
    <section v-if="errored">
      <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
    </section>
    <section v-else>
      <div v-if="loading">Loading...</div>
      <ul id="example-1">
        <li v-for="item in info" :key="item.id">
          {{ item.id }} {{ item.place }}
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SimpleTable',
  data () {
    return {
      info: null,
      loading: true,
      errored: false
    }
  },
  mounted()
  {
    axios .get('http://localhost:8000/api/position/?format=json')
          .then(response => (this.info = response.data))
          .catch(error => {
            console.log(error)
            this.errored = true
          })
         .finally(() => this.loading = false)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
