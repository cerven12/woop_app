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
          <transition-group mode="out-in">
            <AfterTask
              key="3"
              :TaskInfo="task_info"
              @startEdit="startEdit"
              v-show="!isTaskEditMode"
            ></AfterTask>
            <BeforeTask
              key="1"
              :TaskInfo="task_info"
              :OriginalTaskInfo="OriginalTaskInfo"
              @close="endEdit"
              v-show="isTaskEditMode"
            >
            </BeforeTask>
          </transition-group>

          <br />

          <!-- expectation -->
          <AfterExpectation
            :Expectations="task_info.expectations"
          ></AfterExpectation>

          <!-- Discover -->
          <Discover :Discovers="task_info.discovers"></Discover>

          <!-- AfterGiveUp -->
          <transition-group mode="out-in">
            <AfterGiveUp
              key="3"
              :Hurdles="task_info.hurdles"
              @startGiveUpEdit="startGiveUpEdit"
              v-show="!isGiveUpEditMode"
            ></AfterGiveUp>
            <BeforeGiveUp
              key="1"
              :Hurdles="task_info.hurdles"
              :OriginalHurdles="OriginalTaskInfo.hurdles"
              :taskId="task_info.task_id"
              @close="endGiveUpEdit"
              v-show="isGiveUpEditMode"
            ></BeforeGiveUp>
          </transition-group>

          <!-- Motivasion -->
          <transition-group mode="out-in">
            <AfterMotivation
              key="3"
              :Reasons="task_info.reasons"
              :Feedbacks="task_info.feedbacks"
              @startMotiveEdit="startMotiveEdit"
              v-show="!isMotiveEditMode"
            ></AfterMotivation>
            <BeforeMotivation
              key="1"
              :Reasons="task_info.reasons"
              :Feedbacks="task_info.feedbacks"
              :OriginalReasons="OriginalTaskInfo.reasons"
              :OriginalFeedbacks="OriginalTaskInfo.feedbacks"
              :taskId="task_info.task_id"
              @close="endMotiveEdit"
              v-show="isMotiveEditMode"
            ></BeforeMotivation>
          </transition-group>
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
import BeforeTask from "./task_info/BeforeTask";
import Discover from "./discover/Discover";
import AfterGiveUp from "../task/giveup/AfterGiveUp";
import BeforeGiveUp from "../task/giveup/BeforeGiveUp";
import AfterMotivation from "../task/motivation/Motivation";
import BeforeMotivation from "../task/motivation/BeforeMotivation";

export default {
  components: {
    AfterExpectation,
    AfterTask,
    BeforeTask,

    SoloStep,
    Discover,
    AfterGiveUp,
    BeforeGiveUp,

    AfterMotivation,
    BeforeMotivation
  },
  data: () => ({
    isDisplay: false,
    task_info: {}, // from Kanban.vue.
    OriginalTaskInfo: {}, // from Kanban.vue. Deep Copy

    // Component Switch
    isTaskEditMode: false,
    isGiveUpEditMode: false,
    isMotiveEditMode: false
  }),
  methods: {
    open() {
      this.isDisplay = true;
    },
    close() {
      this.isDisplay = false;
    },

    startEdit: function () {
      this.isTaskEditMode = true;
    },
    endEdit: function () {
      this.isTaskEditMode = false;
    },
    startMotiveEdit: function () {
      this.isMotiveEditMode = true;
    },
    endMotiveEdit: function () {
      this.isMotiveEditMode = false;
    },
    startGiveUpEdit: function () {
      this.isGiveUpEditMode = true;
    },
    endGiveUpEdit: function () {
      this.isGiveUpEditMode = false;
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

/*  Transition */
.v-enter {
  transform: translate(-100px, 0);
  opacity: 0;
}
.v-enter-to {
  opacity: 1;
}
.v-enter-active {
  transition: all 1s 0s ease;
}
.v-leave {
  transform: translate(0, 0);
  opacity: 1;
  position: absolute;
}
.v-leave-to {
  transform: translate(-100px, 0);
  opacity: 0;
  position: absolute;
}
.v-leave-active {
  transition: all 0.5s 0s ease;
  position: absolute;
}
</style>
