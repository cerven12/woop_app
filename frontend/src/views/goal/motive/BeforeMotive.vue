<template>
  <div>
    <!-- Split | Left Side "form"| Right Side "TIps" | -->
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
                @click="
                  editMotive();
                  editSelfTrans();
                  editfuture();
                "
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--                       Motive                                       -->
          <!----------------------------------------------------------------------->
          <v-form v-model="valid">
            <h2 class="category-title">Motivation</h2>
            <transition-group name="form" tag="div">
              <div
                v-for="(motives, motive_index) in MotivesData.motives"
                :key="motive_index"
              >
                <!-- If it's two or more forms, show ✘, and label and hint is hide. -->
                <template v-if="motive_index >= 1">
                  <v-row>
                    <v-col cols="11">
                      <v-textarea
                        color="#3994bf"
                        v-model="motives.motive"
                        rows="1"
                        auto-grow
                      ></v-textarea>
                    </v-col>
                    <v-col cols="1">
                      <!-- Form Delete Buttom -->
                      <v-btn
                        @click="
                          deleteMotiveForm(motives.motive_id, motive_index)
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
                        v-model="motives.motive"
                        label="motive"
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
                <v-btn depressed small @click="addMotiveForm">
                  ＋
                </v-btn>
              </v-col>
            </v-row>
          </v-form>

          <!----------------------------------------------------------------------->
          <!--                    Self Transcendence                       -->
          <!----------------------------------------------------------------------->
          <v-form v-model="valid">
            <h2 class="category-title">Self Transendense</h2>
            <transition-group name="form" tag="div">
              <div
                v-for="(self_transcendence_goals,
                self_index) in SelfTransData.self_transcendence_goals"
                :key="self_index"
              >
                <!-- If it's two or more forms, show ✘, and label and hint is hide. -->
                <template v-if="self_index >= 1">
                  <v-row>
                    <v-col cols="11" md="11">
                      <v-textarea
                        rows="1"
                        auto-grow
                        v-model="
                          self_transcendence_goals.self_transcendence_goal
                        "
                      ></v-textarea>
                    </v-col>
                    <v-col cols="1">
                      <!-- Form Delete Buttom -->
                      <v-btn
                        @click="
                          deleteSelfTranscendenceGoalForm(
                            self_transcendence_goals.selftrans_id,
                            self_index
                          )
                        "
                        text
                        depressed
                        height="55"
                        color="error"
                        >✘</v-btn
                      >
                    </v-col>
                  </v-row>
                </template>

                <!-- If it's first form, show label, hint.  -->
                <template v-else>
                  <v-row>
                    <v-col cols="12" md="12">
                      <v-textarea
                        label="Self Transendense"
                        hint="After achieve goal, you think what sort of good impact to
                  my-self, family, friend etc...?"
                        rows="1"
                        auto-grow
                        v-model="
                          self_transcendence_goals.self_transcendence_goal
                        "
                      ></v-textarea> </v-col
                  ></v-row>
                </template>
              </div>
            </transition-group>

            <!-- Form Increase Buttom -->
            <v-row justify="end">
              <v-col cols="1"
                ><v-btn depressed small @click="addSelfTranscendenceGoalForm"
                  >＋</v-btn
                ></v-col
              >
            </v-row>
          </v-form>

          <!----------------------------------------------------------------------->
          <!--                    Future self                                     -->
          <!----------------------------------------------------------------------->
          <v-form v-model="valid">
            <h2 class="category-title">Bad future self</h2>
            <transition-group name="form" tag="div">
              <div
                v-for="(future_selves,
                future_selves_index) in FutureData.future_selves"
                v-bind:key="future_selves_index"
              >
                <!-- If it's two or more forms, show ✘, and label and hint is hide. -->
                <template v-if="future_selves_index >= 1">
                  <v-row>
                    <v-col cols="11" md="11">
                      <v-textarea
                        rows="1"
                        auto-grow
                        v-model="future_selves.future_self"
                      ></v-textarea>
                    </v-col>
                    <v-col cols="1">
                      <!-- Form Delete Buttom -->
                      <v-btn
                        @click="
                          deleteFutureSelfForm(
                            future_selves.future_id,
                            future_selves_index
                          )
                        "
                        text
                        depressed
                        height="55"
                        color="error"
                        >✘</v-btn
                      ></v-col
                    ></v-row
                  >
                </template>

                <!-- If it's first form, show label, hint.  -->
                <template v-else>
                  <v-row>
                    <v-col cols="12" md="12">
                      <v-textarea
                        label="Bad future self"
                        hint="If not action to goal think what sort of bad state a far future self."
                        rows="1"
                        auto-grow
                        v-model="future_selves.future_self"
                      ></v-textarea> </v-col
                  ></v-row>
                </template>
              </div>
            </transition-group>

            <!-- Form Increase Buttom -->
            <v-row justify="end">
              <v-col cols="1"
                ><v-btn depressed small @click="addFutureSelf">＋</v-btn></v-col
              >
            </v-row>
            <v-btn outlined>submit</v-btn>
          </v-form>
        </div>
      </v-container>

      <!----------------------------------------------------------------------->
      <!--                       Right Side "form"                        -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="tips-area">
        <h1>Tips</h1>
        <pre>MotivesData: {{ MotivesData }}</pre>
        <pre>SelfTransData :{{ SelfTransData }}</pre>
        <pre>OriginalSelf :{{ OriginalSelf }}</pre>
        <hr />
        <pre>FutureData:{{ FutureData }}</pre>
        <pre>OriginalFuture:{{ OriginalFuture }}</pre>
      </v-container>
    </div>
  </div>
</template>

<script>
import api from "@/services/api.js";

export default {
  name: "Goal",
  props: [
    "Motives",
    "SelfTranscendence",
    "FutureSelves",

    "OriginalMotives",
    "OriginalSelf",
    "OriginalFuture"
  ],
  data: function () {
    return {
      MotivesData: this.Motives,
      OriginalMotivesData: this.OriginalMotives,

      SelfTransData: this.SelfTranscendence,
      OriginalSelfTransData: this.OriginalSelf,

      FutureData: this.FutureSelves,
      OriginalFutureData: this.OriginalFuture,

      testdata: "",
      root: "",
      valid: "",
      form: "",

      // Registration details of Three Models
      motiveList: [{ motive: "" }],
      selfTranscendenceGoalList: [{ self_transcendence_goal: "" }],
      futureSelfList: [{ future_self: "" }]
    };
  },

  methods: {
    endEdit: function () {
      this.$emit("close");
    },

    //  ------------------------------------------------------------
    //                   Form Increase
    //  ------------------------------------------------------------
    addMotiveForm: function () {
      const form = { motive: "" };
      this.MotivesData.motives.push(form);
    },

    addSelfTranscendenceGoalForm: function () {
      const form = { self_transcendence_goal: "" };
      this.SelfTransData.self_transcendence_goals.push(form);
    },

    addFutureSelf: function () {
      const form = { future_self: "" };
      this.FutureData.future_selves.push(form);
    },

    //  ------------------------------------------------------------
    //                   Form Delete
    //  ------------------------------------------------------------
    deleteMotiveForm(motive_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (motive_id == null) {
        vm.MotivesData.motives.splice(index, 1);
      } else {
        api
          .delete(`goals/${goalid}/motives/${motive_id}/`)
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.MotivesData.motives.splice(index, 1);
        vm.OriginalMotivesData.motives.motives.splice(index, 1);
      }
    },

    deleteSelfTranscendenceGoalForm(selftrans_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (selftrans_id == null) {
        vm.SelfTransData.self_transcendence_goals.splice(index, 1);
      } else {
        api
          .delete(`goals/${goalid}/self_transcendence_goals/${selftrans_id}/`)
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.SelfTransData.self_transcendence_goals.splice(index, 1);
        vm.OriginalSelfTransData.self_transcendence_goals.self_transcendence_goals.splice(
          index,
          1
        );
      }
    },

    deleteFutureSelfForm(future_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (future_id == null) {
        vm.FutureData.future_selves.splice(index, 1);
      } else {
        api
          .delete(`goals/${goalid}/future_selves/${future_id}/`)
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.FutureData.future_selves.splice(index, 1);
        vm.OriginalFutureData.future_selves.future_selves.splice(index, 1);
      }
    },

    endEdit: function () {
      this.$emit("close");
    },
    editMotive: function () {
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let promises = []; // patch datas

      let goalId = vm.$route.params.id;
      Array.from(vm.MotivesData.motives).forEach((motive, index) => {
        // For compute to difference by `OriginalMotives`.
        let originalMo = vm.OriginalMotivesData.motives.motives[index];

        // If existence new post
        if (!motive.motive_id) {
          NewData.push({
            motive: motive.motive
          });
        }

        // edit
        else if (motive.motive !== originalMo.motive) {
          ChangeData.push({
            motive_id: motive.motive_id,
            motive: motive.motive
          });
        }
      });

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/motives/`,
          data: { motive: item.motive, goal: goalId },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/motives/${item.motive_id}/`,
          data: {
            motive: item.motive
          },
          useCredentails: true
        });
        promises.push(newPromise);
      });

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalMotivesData.motives.motives.push(res.data);
          vm.$set(
            vm.MotivesData,
            "motives",
            // Deep Copy
            JSON.parse(JSON.stringify(vm.OriginalMotivesData.motives.motives))
          );
        });
      });

      // patch
      Promise.all(promises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.motive_id;
          // Find the object to be changed by `OriginalMotive`.
          // superscription motive.
          if (
            vm.OriginalMotivesData.motives.motives.find(
              item => item.motive_id == currentId
            )
          ) {
            vm.OriginalMotivesData.motives.motives.find(
              item => item.motive_id == currentId
            ).motive = res.data.motive;
          }
        });
      });
      vm.$emit("close");
    },

    editSelfTrans: function () {
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let promises = []; // patch datas

      let goalId = vm.$route.params.id;
      Array.from(vm.SelfTransData.self_transcendence_goals).forEach(
        (selftrans, index) => {
          // For compute to difference by `OriginalMotives`.
          let originalMo =
            vm.OriginalSelfTransData.self_transcendence_goals
              .self_transcendence_goals[index];

          // If existence new post
          if (!selftrans.selftrans_id) {
            NewData.push({
              self_transcendence_goal: selftrans.self_transcendence_goal
            });
          }

          // edit
          else if (
            selftrans.self_transcendence_goal !==
            originalMo.self_transcendence_goal
          ) {
            ChangeData.push({
              selftrans_id: selftrans.selftrans_id,
              self_transcendence_goal: selftrans.self_transcendence_goal
            });
          }
        }
      );

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/self_transcendence_goals/`,
          data: {
            self_transcendence_goal: item.self_transcendence_goal,
            goal: goalId
          },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/self_transcendence_goals/${item.selftrans_id}/`,
          data: {
            self_transcendence_goal: item.self_transcendence_goal
          },
          useCredentails: true
        });
        promises.push(newPromise);
      });

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalSelfTransData.self_transcendence_goals.self_transcendence_goals.push(
            res.data
          );
          vm.$set(
            vm.SelfTransData,
            "self_transcendence_goals",
            // Deep Copy
            JSON.parse(
              JSON.stringify(
                vm.OriginalSelfTransData.self_transcendence_goals
                  .self_transcendence_goals
              )
            )
          );
        });
      });

      // patch
      Promise.all(promises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.selftrans_id;
          // Find the object to be changed by `OriginalMotive`.
          // superscription motive.
          if (
            vm.OriginalSelfTransData.self_transcendence_goals.self_transcendence_goals.find(
              item => item.selftrans_id == currentId
            )
          ) {
            vm.OriginalSelfTransData.self_transcendence_goals.self_transcendence_goals.find(
              item => item.selftrans_id == currentId
            ).self_transcendence_goal = res.data.self_transcendence_goal;
          }
        });
      });
      vm.$emit("close");
    },

    editfuture: function () {
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let promises = []; // patch datas

      let goalId = vm.$route.params.id;
      Array.from(vm.FutureData.future_selves).forEach((futureSelf, index) => {
        // For compute to difference by `OriginalMotives`.
        let originalMo =
          vm.OriginalFutureData.future_selves.future_selves[index];

        // If existence new post
        if (!futureSelf.future_id) {
          NewData.push({
            future_self: futureSelf.future_self
          });
        }

        // edit
        else if (futureSelf.future_self !== originalMo.future_self) {
          ChangeData.push({
            future_id: futureSelf.future_id,
            future_self: futureSelf.future_self
          });
        }
      });

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/future_selves/`,
          data: { future_self: item.future_self, goal: goalId },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/future_selves/${item.future_id}/`,
          data: {
            future_self: item.future_self
          },
          useCredentails: true
        });
        promises.push(newPromise);
      });

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalFutureData.future_selves.future_selves.push(res.data);
          vm.$set(
            vm.FutureData,
            "future_selves",
            // Deep Copy
            JSON.parse(
              JSON.stringify(vm.OriginalFutureData.future_selves.future_selves)
            )
          );
        });
      });

      // patch
      Promise.all(promises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.future_id;
          // Find the object to be changed by `OriginalMotive`.
          // superscription motive.
          if (
            vm.OriginalFutureData.future_selves.future_selves.find(
              item => item.future_id == currentId
            )
          ) {
            vm.OriginalFutureData.future_selves.future_selves.find(
              item => item.future_id == currentId
            ).future_self = res.data.future_self;
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
