<template>
  <v-app>
     <div id="background">
     {{ All }}
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>
      <AfterGoal :Goal="Goal" :Steps="Steps"></AfterGoal>
      <Kanban :Boards="Boards"></Kanban>
      <Note :Notes="Notes"></Note>
      <AfterGIveUp :Worries="Worries"></AfterGIveUp>
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>
      <AfterMotive
        :Motives="Motives"
        :SelfTranscendence="SelfTranscendence"
        :FutureSelves="FutureSelves"
      ></AfterMotive>
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>
      <BeforeGoal></BeforeGoal>
      <BeforeMotive></BeforeMotive>
      <BeforeGiveUp></BeforeGiveUp>
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

// Note
import Note from "./note/Note.vue";
import Kanban from "./task/Kanban.vue";

import api from "@/services/api";

export default {
  components: {
    BeforeGoal,
    AfterGoal,
    BeforeMotive,
    AfterMotive,
    BeforeGiveUp,
    AfterGIveUp,
    Note,
    Kanban,
  },
  data: function() {
    return {
      All: {},
      Goal: {},
      Motives: {},
      SelfTranscendence: {},
      FutureSelves: {},
      Worries: {},
      Notes: {},
      Boards: {},
      Steps: {},
    };
  },
  mounted: function() {
    let vm = this;
    api
      .get("goals/55a04a5e-8cdb-4317-b6ea-4bfb46142740/")
      .then(function(response) {
        vm.All = response;
        // Goal_Info
        vm.$set(vm.Goal, "goal_title", response.data.goal_title);
        vm.$set(vm.Goal, "goal_description", response.data.goal_description);
        vm.$set(vm.Goal, "criteria", response.data.criteria);
        vm.$set(vm.Goal, "created_at", response.data.created_at);

        // Motive
        vm.$set(vm.Motives, "motives", response.data.motives);

        // Self Transcendence Goal
        vm.$set(
          vm.SelfTranscendence,
          "self_transcendence_goals",
          response.data.self_transcendence_goals
        );

        //  Future Selves
        vm.$set(vm.FutureSelves, "future_selves", response.data.future_selves);

        //  Worry, Idea
        vm.$set(vm.Worries, "worries", response.data.worries);

        //  Notes
        vm.$set(vm.Notes, "notes", response.data.notes);

        // Kanban
        vm.$set(vm.Boards, "boards", response.data.boards);

        // Steps ( Since the nested APIs do not allow to sort Step by order_by, we will again axios. get. )
        api.get(`goals/${response.data.goal_id}/steps/`).then(function(response){
        vm.$set(vm.Steps, "steps", response.data)})
      });
  },
};
</script>

<style scoped>
body {
  background: #f4f4f4;
}
</style>
