<template>
  <div class="home">
    <NewGoal></NewGoal>
  </div>
</template>

<script>
// @ is an alias to /src
import NewGoal from '@/components/NewGoal.vue'

export default {
  name: 'Home',
  components: {
    NewGoal
  }
}
</script>
