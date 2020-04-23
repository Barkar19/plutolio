<template>
    <v-navigation-drawer
      v-model="drawer_value"
      app
      clipped
    >
      <v-list dense>
        <v-list-item link v-for="l in links" :key="l.route" router :to="l.route">
          <v-list-item-action>
            <v-icon>{{ l.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ l.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
    name: 'NavBar',
    props: ["drawer_value"],
    data() {
        return {
            links: [
                {icon: "account_balance_wallet", text: "Home", route:"/"},
                {icon: "insert_chart_outlined", text: "Reports", route:"/reports"},
                {icon: "transform", text: "Transactions", route:"/transactions"},
                {icon: "euro", text: "Currencies", route:"/currencies"},
                {icon: "settings", text: "Settings", route:"/settings"},
                
            ]
        }
    }
}
</script>