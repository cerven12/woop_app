<template>
  <v-app>
    <div id="background">
      <AfterGoal></AfterGoal>
      <AfterMotive></AfterMotive>
      <BeforeGoal></BeforeGoal>
      <BeforeMotive></BeforeMotive>
      <BeforeGiveUp></BeforeGiveUp>
      <BeforeSchedule></BeforeSchedule>
    </div>
  </v-app>
</template>

<script>
// Goal
import BeforeGoal from "./goal_info/BeforeGoal";
import AfterGoal from "./goal_info/AfterGoal";

// Motive
import BeforeMotive from "./motive/BeforeMotive";
import AfterMotive from "./motive/AfterMotive";

// GiveUp
import BeforeGiveUp from "./giveup/BeforeGiveUp";
import AfterGIveUp from "./giveup/AfterGiveUp";

// Schedule
import BeforeSchedule from "./schedule/BeforeSchedule";
import AfterSchedule from "./schedule/AfterSchedule";

export default {
  components: {
    BeforeGoal,
    AfterGoal,
    BeforeMotive,
    AfterMotive,
    BeforeGiveUp,
    AfterGIveUp,
    BeforeSchedule,
    AfterSchedule,
  },
};
</script>

<style scoped>
body {
  background: #f4f4f4;
}
</style>
