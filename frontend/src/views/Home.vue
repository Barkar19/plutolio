<template>
    <div>
        <h1> Home </h1>
        <v-container>
            <SimpleTable/>
        </v-container>
    </div>
</template>

<script>
import SimpleTable from '../components/SimpleTable';
export default {
    components: {
        SimpleTable
    }
}
</script>