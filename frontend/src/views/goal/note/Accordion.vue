<template>
  <div>
    <h1>ACC</h1>
    <accordion>Accordion body</accordion>
    <accordion theme="purple">
      <div slot="header">TIPS</div>
      Purple accordion
    </accordion>
  </div>
</template>

<script>
import accordion from "./Acc.vue";

export default {
  components: {
    accordion,
  },
  props: ["theme"],
  data: function() {
    return {};
  },
};
</script>
