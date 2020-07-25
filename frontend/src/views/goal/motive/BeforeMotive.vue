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
              <v-btn small color="gray" @click="endEdit">OK!</v-btn>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--                       Motive                                       -->
          <!----------------------------------------------------------------------->
          <v-form v-model="valid">
            <h2 class="category-title">Motivation</h2>
            <transition-group name="form" tag="div">
              <div
                v-for="(motives, motive_index) in Motives.motives"
                :key="motive_index"
              >
                <!-- If it's two or more forms, show ✘, and label and hint is hide. -->
                <template v-if="motive_index >= 1">
                  <v-row>
                    <v-col cols="11">
                      <v-textarea
                        v-model="motives.motive"
                        rows="1"
                        auto-grow
                      ></v-textarea>
                    </v-col>
                    <v-col cols="1">
                      <!-- Form Delete Buttom -->
                      <v-btn
                        @click="deleteMotiveForm(motive_index)"
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
                self_index) in SelfTranscendence.self_transcendence_goals"
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
                        @click="deleteSelfTranscendenceGoalForm(self_index)"
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
                future_selves_index) in FutureSelves.future_selves"
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
                        @click="deleteFutureSelfForm(future_selves_index)"
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
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "Goal",
  props: ["Motives", "SelfTranscendence", "FutureSelves"],
  data: function () {
    return {
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
      this.Motives.motives.push(form);
    },

    addSelfTranscendenceGoalForm: function () {
      const form = { self_transcendence_goal: "" };
      this.SelfTranscendence.self_transcendence_goals.push(form);
    },

    addFutureSelf: function () {
      const form = { future_self: "" };
      this.FutureSelves.future_selves.push(form);
    },

    //  ------------------------------------------------------------
    //                   Form Delete
    //  ------------------------------------------------------------
    deleteMotiveForm(index) {
      this.Motives.motives.splice(index, 1);
    },

    deleteSelfTranscendenceGoalForm(index) {
      this.SelfTranscendence.self_transcendence_goals.splice(index, 1);
    },

    deleteFutureSelfForm(index) {
      this.FutureSelves.future_selves.splice(index, 1);
    },
    endEdit: function () {
      this.$emit("close");
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
