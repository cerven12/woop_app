<template>
  <div>
    <v-btn @click="toggle">TOGGLE</v-btn>

    <div id="motivation" class="input_group">
      <transition name="motivation" mode="out-in">
        <div v-if="reg" key="0">
          <v-container
            ><v-row
              ><v-col cols="12"
                ><h2 class="display-1 font-regular">
                  To Keep Your Motivation Flying High.
                </h2></v-col
              ></v-row
            >
          </v-container>
          <v-form v-model="valid">
            <v-container>
              <h2 class="headline">Motivation</h2>
              <transition-group name="form" tag="div">
                <div
                  v-for="(motives, motive_index) in motiveList"
                  :key="motive_index"
                >
                  <div>
                    <template v-if="motive_index >= 1">
                      <v-row>
                        <v-col cols="11" md="11">
                          <v-textarea
                            v-model="motives.motive"
                            rows="1"
                            auto-grow
                          ></v-textarea>
                        </v-col>
                        <v-col cols="1"
                          ><v-btn
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
                    <template v-else>
                      <v-row>
                        <v-col cols="12">
                          <v-textarea
                            v-model="motives.motive"
                            placeholder=""
                            name="理由"
                            label=""
                            value=""
                            hint="Why want to achieve it ?"
                            rows="1"
                            auto-grow
                          ></v-textarea>
                        </v-col>
                      </v-row>
                    </template>
                  </div>
                </div>
              </transition-group>
              <!-- The "v-for" ends here. -->
              <v-row justify="end">
                <v-col cols="1"
                  ><v-btn depressed small @click="addMotiveForm"
                    >＋</v-btn
                  ></v-col
                >
              </v-row>
            </v-container>
          </v-form>

          <div>
            <v-form v-model="valid">
              <v-container>
                <h2 class="headline">
                  Self Transendense
                </h2>
                <transition-group name="form" tag="div">
                  <div
                    v-for="(self_transcendence_goals,
                    self_index) in selfTranscendenceGoalList"
                    :key="self_index"
                  >
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
                        <v-col cols="1"
                          ><v-btn
                            @click="deleteSelfTranscendenceGoalForm(self_index)"
                            text
                            depressed
                            height="55"
                            color="error"
                            >✘</v-btn
                          ></v-col
                        ></v-row
                      >
                    </template>
                    <template v-else>
                      <v-row>
                        <v-col cols="12" md="12">
                          <v-textarea
                            name="自己超越目標"
                            label=""
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

                <v-row justify="end">
                  <v-col cols="1"
                    ><v-btn
                      depressed
                      small
                      @click="addSelfTranscendenceGoalForm"
                      >＋</v-btn
                    ></v-col
                  >
                </v-row>
              </v-container>
            </v-form>
          </div>
          <div>
            <v-form v-model="valid">
              <v-container>
                <h2 class="headline">
                  Bad future self
                </h2>
                <transition-group name="form" tag="div">
                  <div
                    v-for="(future_selves,
                    future_selves_index) in futureSelfList"
                    v-bind:key="future_selves_index"
                  >
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
                    <template v-else>
                      <v-row>
                        <v-col cols="12" md="12">
                          <v-textarea
                            name="後悔"
                            label=""
                            hint="If not action to goal think what sort of bad state a far future self."
                            rows="1"
                            auto-grow
                            v-model="future_selves.future_self"
                          ></v-textarea> </v-col
                      ></v-row>
                    </template>
                  </div>
                </transition-group>

                <v-row justify="end">
                  <v-col cols="1"
                    ><v-btn depressed small @click="addFutureSelf"
                      >＋</v-btn
                    ></v-col
                  >
                </v-row>
                <v-btn @click="allMotivesRegister" outlined>submit</v-btn>
              </v-container>
            </v-form>
          </div>
        </div>

        <!-- View mode -->
        <div v-else key="1">
          <v-container
            ><v-row
              ><v-col cols="12"
                ><h2 class="display-1 font-regular">
                  To Keep Your Motivation Flying High.
                </h2></v-col
              ></v-row
            >
          </v-container>
          <!-- reason  -->

          <v-container>
            <div>
              <h3 class="headline">Motivation</h3>
              <v-row
                ><v-col>
                  <v-list shaped color="#f0f0f0" flat class="list">
                    <v-list-item-group
                      ><div
                        class="contents"
                        v-for="(motives, motives_index) in motiveList"
                        v-bind:key="motives_index"
                      >
                        <v-list-item
                          v-for="(motive, index) in motives"
                          v-bind:key="motive.id"
                          ><v-list-item-content
                            v-text="motive"
                            :key="index"
                          ></v-list-item-content>
                        </v-list-item>
                        <v-divider inset></v-divider>
                      </div>
                    </v-list-item-group>
                  </v-list>
                </v-col>
              </v-row>
            </div>
          </v-container>
          <!-- reason ここまで -->

          <!-- self stanscendence  -->
          <v-container>
            <div>
              <h3 class="headline">Self Transendense</h3>
              <v-row
                ><v-col>
                  <v-list shaped color="#f0f0f0" flat class="list">
                    <v-list-item-group
                      ><div
                        class="contents"
                        v-for="self_transcendence_goals in selfTranscendenceGoalList"
                        v-bind:key="self_transcendence_goals.id"
                      >
                        <v-list-item
                          v-for="(self_transcendence_goal,
                          index) in self_transcendence_goals"
                          v-bind:key="self_transcendence_goal.id"
                        >
                          <v-list-item-content
                            class="text-justify"
                            v-text="self_transcendence_goal"
                            :key="index"
                          ></v-list-item-content>
                        </v-list-item>
                        <v-divider inset></v-divider>
                      </div>
                    </v-list-item-group>
                  </v-list>
                </v-col>
              </v-row>
            </div>
          </v-container>
          <!-- self transedence ここまで -->

          <!-- self stanscendence  -->
          <v-container>
            <div>
              <h3 class="headline">Bad future self</h3>
              <v-row
                ><v-col>
                  <v-list shaped color="#f0f0f0" flat class="list">
                    <v-list-item-group
                      ><div
                        class="contents"
                        v-for="future_selves in futureSelfList"
                        :key="future_selves.id"
                      >
                        <v-list-item
                          v-for="(future_self, index) in future_selves"
                          :key="future_self.id"
                          ><v-list-item-content
                            v-text="future_self"
                            :key="index"
                          ></v-list-item-content>
                        </v-list-item>
                        <v-divider inset></v-divider>
                      </div>
                    </v-list-item-group>
                  </v-list>
                </v-col>
              </v-row>
            </div>
          </v-container>
          <!-- self transedence ここまで -->
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id", "token"],

  data: function() {
    return {
      root: "",
      valid: "",
      form: "",
      // Registration details of Three Models
      motiveList: [{ motive: "" }],
      selfTranscendenceGoalList: [{ self_transcendence_goal: "" }],
      futureSelfList: [{ future_self: "" }],

      reg: true,
      judgeStr: "",
    };
  },
  mounted() {
    this.root = process.env.VUE_APP_ROOT_API;
  },
  computed: {
    url() {
      return this.$store.state.url;
    },
  },
  methods: {
    toggle: function() {
      if (this.reg === true) {
        this.reg = false;
      } else {
        this, (this.reg = true);
      }
    },
    //  everyメソッドで、最初にformの内容をバリデーションできそう。

    //  Form Increase
    addMotiveForm: function() {
      const form = { motive: "" };
      this.motiveList.push(form);
    },

    addSelfTranscendenceGoalForm: function() {
      const form = { self_transcendence_goal: "" };
      this.selfTranscendenceGoalList.push(form);
    },

    addFutureSelf: function() {
      const form = { future_self: "" };
      this.futureSelfList.push(form);
    },

    // Form Delete
    deleteMotiveForm(index) {
      this.motiveList.splice(index, 1);
      console.log(this.motiveList);
    },

    deleteSelfTranscendenceGoalForm(index) {
      this.selfTranscendenceGoalList.splice(index, 1);
      console.log(this.selfTranscendenceGoalList);
    },

    deleteFutureSelfForm(index) {
      this.futureSelfList.splice(index, 1);
      console.log(this.futureSelfList);
    },

    // Posting a dynamically increased form
    // Motive Model
    motivesRegister: function() {
      let vm = this;
      vm.motiveList.forEach(function(motives) {
        // Remove spaces and null strings
        let judgeStr = motives.motive.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/" + "motives/",
              {
                goal: vm.goal_id,
                motive: motives.motive,
              },
              {
                //  JWT
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `JWT ${vm.token}`,
                },
              }
            )
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log(`その文字列はだめです`);
        }
      });
    },

    // SelfTranscendenceGoal Model
    selfTranscendenceGoalListRegister: function() {
      const vm = this;
      vm.selfTranscendenceGoalList.forEach(function(self_transcendence_goals) {
        const judgeStr = self_transcendence_goals.self_transcendence_goal.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/" + "self_transcendence_goals/",
              {
                goal: vm.goal_id,
                self_transcendence_goal:
                  self_transcendence_goals.self_transcendence_goal,
              },
              {
                //  JWT
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `JWT ${vm.token}`,
                },
              }
            )
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log("その文字列はだめです");
        }
      });
    },

    // FutureSelf Model
    futureSelvesRegister: function() {
      const vm = this;
      this.futureSelfList.forEach(function(future_selves) {
        const judgeStr = future_selves.future_self.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/" + "future_selves/",
              {
                goal: vm.goal_id,
                future_self: future_selves.future_self,
              },
              {
                //  JWT
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `JWT ${vm.token}`,
                },
              }
            )
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log("その文字列はだめ");
        }
      });
    },

    // Consolidate of  above three models register.
    allMotivesRegister: function() {
      this.motivesRegister();
      this.selfTranscendenceGoalListRegister();
      this.futureSelvesRegister();
    },
  },
};
</script>

<style scoped>
#motivation {
  background-color: #f0f0f0;
  border-radius: 50px;
  padding: 70px;
  margin: 40px 40px 40px 40px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);
}

#motivation:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}

/* .subtitle {
  padding: 0 0 0 25px;
  margin: 0 0 0 25px;
}

.list {
  padding: 0 50px 0 50px;
  margin: 0 50px 0 50px;
} */

.v-messages {
  font-size: 15px;
}
.v-messages__message {
  padding-top: 2px;
}

.motivation-enter-active,
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
</style>
