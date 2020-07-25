<template>
  <div>
    <br><br><br><br>
    <CreateGoal></CreateGoal>
    <CreateMotive></CreateMotive>
    <CreateGiveUp></CreateGiveUp>
  </div>
</template>

<script>
import CreateGoal from "../goal/goal_info/CreateGoal.vue";
import CreateGiveUp from "../goal/giveup/CreateGiveUp.vue";
import CreateMotive from "../goal/motive/CreateMotive.vue";

export default {
  //component code
  components: {
    CreateGoal,
    CreateGiveUp,
    CreateMotive,
  },
  data: function () {
    return {
      Goal: {
        goal_title: "",
        goal_description: "",
        criteria: ""
      }
    };
  },
};
</script>

<style>
</style>
