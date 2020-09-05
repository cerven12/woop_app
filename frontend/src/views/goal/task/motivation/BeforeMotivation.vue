<template>
  <div>
    <div id="css-grid">
      <!----------------------------------------------------------------------->
      <!--                       Left Side "form"                         -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="form-area">
        <div id="line">
          <!-- Label -->
          <v-row>
            <v-col cols="10">
              <h2 class="message-title">
                To Keep Your Motivation Flying High.
              </h2>
            </v-col>
            <v-col>
              <v-btn
                fab
                small
                depressed
                color="#b3b3b3"
                @click="editReason(), editFeedback()"
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--                       reason                                       -->
          <!----------------------------------------------------------------------->
          <v-form v-model="valid">
            <h2 class="category-title">Reasons</h2>
            <transition-group name="form" tag="div">
              <div
                v-for="(reasons, reason_index) in ReasonsData"
                :key="reason_index"
              >
                <!-- If it's two or more forms, show ✘, and label and hint is hide. -->
                <template v-if="reason_index >= 1">
                  <v-row>
                    <v-col cols="11">
                      <v-textarea
                        color="#3994bf"
                        v-model="reasons.reason"
                        rows="1"
                        auto-grow
                      ></v-textarea>
                    </v-col>
                    <v-col cols="1">
                      <!-- Form Delete Buttom -->
                      <v-btn
                        @click="
                          deleteReasonForm(reasons.reason_id, reason_index)
                        "
                        text
                        depressed
                        height="55"
                        color="error"
                        >✘</v-btn
                      ></v-col
                    >
                  </v-row>
                </template>

                <!-- If it's first form, show label, hint.  -->
                <template v-else>
                  <v-row>
                    <v-col cols="12">
                      <v-textarea
                        v-model="reasons.reason"
                        label="reason"
                        hint="Why want to achieve it ?"
                        rows="1"
                        auto-grow
                      ></v-textarea>
                    </v-col>
                  </v-row>
                </template>
              </div>
            </transition-group>

            <!-- Form Increase buttom -->
            <v-row justify="end">
              <v-col cols="1">
                <v-btn depressed small @click="addReasonForm">
                  ＋
                </v-btn>
              </v-col>
            </v-row>
          </v-form>

          <!----------------------------------------------------------------------->
          <!--                       reason                                       -->
          <!----------------------------------------------------------------------->
          <v-form v-model="valid">
            <h2 class="category-title">Feedbacks</h2>
            <transition-group name="form" tag="div">
              <div
                v-for="(feedbacks, feedback_index) in FeedbacksData"
                :key="feedback_index"
              >
                <!-- If it's two or more forms, show ✘, and label and hint is hide. -->
                <template v-if="feedback_index >= 1">
                  <v-row>
                    <v-col cols="11">
                      <v-textarea
                        color="#3994bf"
                        v-model="feedbacks.feedback"
                        rows="1"
                        auto-grow
                      ></v-textarea>
                    </v-col>
                    <v-col cols="1">
                      <!-- Form Delete Buttom -->
                      <v-btn
                        @click="
                          deleteFeedbackForm(
                            feedbacks.feedback_id,
                            feedback_index
                          )
                        "
                        text
                        depressed
                        height="55"
                        color="error"
                        >✘</v-btn
                      ></v-col
                    >
                  </v-row>
                </template>

                <!-- If it's first form, show label, hint.  -->
                <template v-else>
                  <v-row>
                    <v-col cols="12">
                      <v-textarea
                        v-model="feedbacks.feedback"
                        label="reason"
                        hint="Why want to achieve it ?"
                        rows="1"
                        auto-grow
                      ></v-textarea>
                    </v-col>
                  </v-row>
                </template>
              </div>
            </transition-group>

            <!-- Form Increase buttom -->
            <v-row justify="end">
              <v-col cols="1">
                <v-btn depressed small @click="addFeedbackForm">
                  ＋
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </div>
      </v-container>
    </div>

  </div>
</template>
<script>
import api from "@/services/api.js";

export default {
  name: "Task",
  props: [
    "Reasons",
    "Feedbacks",
    "OriginalReasons",
    "OriginalFeedbacks",
    "taskId"
  ],

  data: function () {
    return {
      ReasonsData: this.Reasons,
      OriginalReasonsData: this.OriginalReasons,

      FeedbacksData: this.Feedbacks,
      OriginalFeedbacksData: this.OriginalFeedbacks
    };
  },
  methods: {
    endEdit: function () {
      this.$emit("close");
    },
    addReasonForm: function () {
      const form = { reason: "" };
      this.ReasonsData.push(form);
    },
    addFeedbackForm: function () {
      const form = { feedback: "" };
      this.FeedbacksData.push(form);
    },
    deleteReasonForm(reason_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (reason_id == null) {
        vm.ReasonsData.splice(index, 1);
      } else {
        api
          .delete(`goals/${goalid}/tasks/${vm.taskId}/reasons/${reason_id}/`)
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.ReasonsData.splice(index, 1);
        vm.OriginalReasonsData.splice(index, 1);
      }
    },
    deleteFeedbackForm(feedback_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (feedback_id == null) {
        vm.FeedbacksData.splice(index, 1);
      } else {
        api
          .delete(
            `goals/${goalid}/tasks/${vm.taskId}/feedbacks/${feedback_id}/`
          )
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.FeedbacksData.splice(index, 1);
        vm.OriginalFeedbacksData.splice(index, 1);
      }
    },

    editReason: function () {
      console.log("start");
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let promises = []; // patch datas

      let goalId = vm.$route.params.id;
      let taskId = vm.taskId;
      console.log("start");

      Array.from(vm.ReasonsData).forEach((reason, index) => {
        // For compute to difference by `OriginalMotives`.
        let originalMo = vm.OriginalReasonsData[index];

        // If existence new post
        if (!reason.reason_id) {
          NewData.push({
            reason: reason.reason
          });
        }

        // edit
        else if (reason.reason !== originalMo.reason) {
          ChangeData.push({
            reason_id: reason.reason_id,
            reason: reason.reason
          });
        }
      });

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/tasks/${taskId}/reasons/`,
          data: { reason: item.reason, task: taskId },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/tasks/${taskId}/reasons/${item.reason_id}/`,
          data: {
            reason: item.reason
          },
          useCredentails: true
        });
        promises.push(newPromise);
      });

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalReasonsData.push(res.data);
          vm.ReasonsData =
            // Deep Copy
            JSON.parse(JSON.stringify(vm.OriginalReasonsData));
        });
      });

      // patch
      Promise.all(promises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.reason_id;
          // Find the object to be changed by `Originalreason`.
          // superscription reason.
          if (
            vm.OriginalReasonsData.find(item => item.reason_id == currentId)
          ) {
            vm.OriginalReasonsData.find(
              item => item.reason_id == currentId
            ).reason = res.data.reason;
          }
        });
      });
      vm.$emit("close");
    },
    editFeedback: function () {
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let promises = []; // patch datas

      let goalId = vm.$route.params.id;
      let taskId = vm.taskId;

      Array.from(vm.FeedbacksData).forEach((feedback, index) => {
        // For compute to difference by `OriginalMotives`.
        let originalMo = vm.OriginalFeedbacksData[index];

        // If existence new post
        if (!feedback.feedback_id) {
          NewData.push({
            feedback: feedback.feedback
          });
        }

        // edit
        else if (feedback.feedback !== originalMo.feedback) {
          ChangeData.push({
            feedback_id: feedback.feedback_id,
            feedback: feedback.feedback
          });
        }
      });

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/tasks/${taskId}/feedbacks/`,
          data: { feedback: item.feedback, task: taskId },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/tasks/${taskId}/feedbacks/${item.feedback_id}/`,
          data: {
            feedback: item.feedback
          },
          useCredentails: true
        });
        promises.push(newPromise);
      });

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalFeedbacksData.push(res.data);
          vm.FeedbacksData =
            // Deep Copy
            JSON.parse(JSON.stringify(vm.OriginalFeedbacksData));
        });
      });

      // patch
      Promise.all(promises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.feedback_id;
          // Find the object to be changed by `Originalfeedback`.
          // superscription feedback.
          if (
            vm.OriginalFeedbacksData.find(item => item.feedback_id == currentId)
          ) {
            vm.OriginalFeedbacksData.find(
              item => item.feedback_id == currentId
            ).feedback = res.data.feedback;
          }
        });
      });
      vm.$emit("close");
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  background-color: #f0f0f0;
}

#form-area {
  grid-area: form;
}
#tips-area {
  grid-area: tips;
}

@media all and (max-width: 100000px) {
  #css-grid {
    grid-template-columns: 55% 45%;
    grid-template-areas: "form tips";
    padding: 0px 17%;
  }
}

@media all and (max-width: 1264px) {
  #css-grid {
    grid-template-columns: 100%;
    grid-template-areas:
      "form"
      "tips";
    padding: 0px 13%;
  }
}

@media all and (max-width: 960px) {
  #css-grid {
    padding: 0px 5%;
  }
}

/*   ------------------------------------------------------------
                            Transition
 ------------------------------------------------------------*/
motivation-enter-active,
.motivation-leave-active {
  transition: opacity 0.3s;
}
.motivation-enter,
.motivation-leave-to {
  opacity: 0;
}

/* add(delete) form */
.form-enter-active {
  animation: fadeInUp 0.3s;
  transition: opacity 0.3s;
}
.form-leave-active {
  animation: fadeInUp 0.3s reverse;
  transition: opacity 0.3s;
}
.form-enter,
.form-leave-to {
  opacity: 0;
}

@keyframes fadeInUp {
  0% {
    transform: translateX(20px);
    opacity: 0;
  }
  60% {
    opacity: 0.3;
  }
  100% {
    transform: translateX(0px);
    opacity: 1;
  }
}

/*   ------------------------------------------------------------
                            Font Desiign
-----------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #4465c0;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 40px;
  color: #4d4d4d;
}

.motive-left-border {
  border-left: 20px #3994bf solid;
}
</style>
