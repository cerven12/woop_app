<template>
  <v-app>
    <div id="background">
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>
      <AfterGoal></AfterGoal>
      <Kanban></Kanban>
      <Note></Note>

      <AfterMotive></AfterMotive>
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>

      <AfterGIveUp></AfterGIveUp>
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>

      <AfterSchedule></AfterSchedule>
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>

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

// Note
import Note from "./note/Note.vue";
import Kanban from "./task/Kanban.vue";

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
    Note,
    Kanban,
  },
};
</script>

<style scoped>
body {
  background: #f4f4f4;
}
</style>
