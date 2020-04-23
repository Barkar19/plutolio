<template>
    <div>
        <h1> Settings {{ value }}</h1>
        <v-container >
            <v-row align="center" justify="center">
                <v-col class="text-right" justify="end">
                    <h3>Night mode</h3>
                </v-col>
                <v-col>
                    <v-btn-toggle  v-model="value" mandatory>
                        <v-btn :value="false">
                            <v-icon>wb_sunny</v-icon>
                        </v-btn>
                        <v-btn :value="true">
                            <v-icon>nights_stay</v-icon>
                        </v-btn>
                    </v-btn-toggle>
                </v-col>
            </v-row>

        </v-container>
    </div>
</template>

<script>
export default {
    data () {
      return {
          value: true
        // toggle_exclusive: this.$vuetify.theme.dark,
      }
    },
    methods: {

    },
    watch: {
        value: function() {
            console.log("Changed!!!\n", this.value)
            this.$emit('nightModeChanged', this.value)
        }
    },
    computed: {
        // value: $vuetify.theme.dark
    },

}
</script>