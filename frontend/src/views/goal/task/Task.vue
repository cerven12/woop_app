<template>
  <div>
    <v-dialog
      class="dialog-shape"
      v-model="isDisplay"
      width="1400"
      :fullscreen="$vuetify.breakpoint.xs"
    >
      <div class="background">
        <v-container>
          <br />

          <AfterTask>
            <template #task_title>
              {{ task_info.task_title }}
            </template>
            <template #task_description>
              {{ task_info.task_description }}
            </template>
            <template #criteria>
              {{ task_info.criteria }}
            </template>
          </AfterTask>
          <AfterTask :></AfterTask>
<br>

          <!-- expectation -->
          <AfterExpectation
            :Expectations="task_info.expectations"
          ></AfterExpectation>



          <!-- Discover -->
          <Discover :Discovers="task_info.discovers"></Discover>

          <!-- AfterGiveUp -->
          <AfterGiveUp :Hurdles="task_info.hurdles"></AfterGiveUp>

          <!-- Motivasion -->
          <AfterMotivation
            :Reasons="task_info.reasons"
            :Feedbacks="task_info.feedbacks"
          ></AfterMotivation>

       </v-container>
        <!-- </v-card> -->
      </div>
    </v-dialog>
  </div>
</template>

<script>
import SoloStep from "../../../components/SoloStep";
import AfterExpectation from "./expectation/AfterExpectation";
import AfterTask from "./task_info/AfterTask";
import Discover from "./discover/Discover";
import AfterGiveUp from "../task/giveup/AfterGiveUp";
import AfterMotivation from "../task/motivation/Motivation";

export default {
  components: {
    AfterExpectation,
    AfterTask,
    SoloStep,
    Discover,
    AfterGiveUp,
    AfterMotivation
  },
  data: () => ({
    isDisplay: false,
    task_info: "" // from Kanban.vue.
  }),
  methods: {
    open() {
      this.isDisplay = true;
    },
    close() {
      this.isDisplay = false;
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #088dda;
}

.category-title {
  font-family: Roboto;
  font-size: 24px;
  /* text-align: center; */
  line-height: 30px;
  color: #4d4d4d;
  padding-bottom: 15px;
}

.sub-title {
  font-family: Roboto;
  font-size: 18px;
  /* text-align: center; */
  line-height: 30px;
  color: #666666;
  padding-bottom: 15px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #2e2e2e;
  margin-block-end: 0em;
}

.back {
  background: #f0f0f0f5;
}

.goal-title {
  font-style: normal;
  font-weight: normal;
  color: #4465c0;
  /* Match position to SoloStep */
  padding: 10px 0px;
}

.background {
  background: #f0f0f0f7;
  border-radius: 20px;
}
</style>
