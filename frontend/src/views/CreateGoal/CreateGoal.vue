<template>
  <div>
    <v-app>
      <div id="back">
        <div id="main"></div>
        <v-btn @click="toggle">表示の切り替え</v-btn>
        <div id="goal" class="reg">
          <transition name="goal" mode="out-in">
            <div v-if="reg" key="0">
              <v-container>
                <v-row>
                  <v-col cols="12" md="12">
                    <h2 class="headline">
                      Write it down your Goal.
                    </h2>
                  </v-col>
                </v-row>

                <v-row justify="start">
                  <v-col cols="8" md="12" lg="8"
                    ><h1 class="display-2">
                      {{ goal_title }}
                    </h1>
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-col cols="2">
                    <v-icon
                      x-large
                      color="#3f5eb5"
                      v-show="new_goal_registered"
                      id="check"
                      >mdi-check-bold</v-icon
                    ><v-btn
                      class="ma-2"
                      text
                      x-large
                      id="check"
                      @click="newGoalRegister(goal_title, goal_description)"
                      >Post!</v-btn
                    >
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" md="12">
                    <!-- <div
                      style="white-space: pre-line;"
                      class="title font-regular"
                    >
                      {{ goal_description }}
                    </div> -->
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      label="Your Goal"
                      hint=""
                      placeholder=""
                      v-model="goal_title"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="12" md="12">
                    <!-- <mavon-editor
                  v-model="goal_description"
                  language="en"
                  :toolbars="toolbars"
                /> -->
                    <v-textarea
                      name="Detail"
                      label="Detail"
                      hint="In more detail."
                      rows="1"
                      auto-grow
                      placeholder=""
                      v-model="goal_description"
                    ></v-textarea>
                  </v-col>
                </v-row>
                <!-- <v-row>
                  <v-col cols="12">
                    <v-btn
                      class="ma-2"
                      outlined
                      @click="newGoalRegister(goal_title, goal_description)"
                      >submit</v-btn
                    >
                  </v-col>
                </v-row> -->
              </v-container>
            </div>
            <!-- 登録後 -->

            <div v-else key="1">
              <v-container>
                <v-row>
                  <v-col cols="12" md="12">
                    <h3 class="headline">
                      Your Goal
                    </h3>
                  </v-col>
                </v-row>

                <v-row justify="start">
                  <v-col cols="8" md="12" lg="8"
                    ><h1 class="display-2">{{ goal_title }}</h1>
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-col cols="2">
                    <v-icon
                      x-large
                      color="#3f5eb5"
                      v-show="new_goal_registered"
                      id="check"
                      >mdi-check-bold</v-icon
                    >
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" md="12">
                    <div
                      style="white-space: pre-line;"
                      class="title font-weight-light"
                    >
                      {{ goal_description }}
                    </div>
                  </v-col>
                </v-row>
              </v-container>
            </div>
          </transition>
        </div>

        <CreateGoalMotivation
          :goal_id="this_time_goal_data.goal_id"
          :token="token"
        ></CreateGoalMotivation>

        <CreateGoalCounterMeasure
          :goal_id="this_time_goal_data.goal_id"
          :token="token"
        ></CreateGoalCounterMeasure>

        <CreateGoalSchedule
          :goal_id="this_time_goal_data.goal_id"
          :token="token"
        ></CreateGoalSchedule>
        <br /><br /><br /><br /><br /><br /><br /><br />
      </div>
    </v-app>
  </div>
</template>

<script>
import CreateGoalCounterMeasure from "./CreateGoalCounterMeasure.vue";
import CreateGoalMotivation from "./CreateGoalMotivation.vue";
import CreateGoalSchedule from "./CreateGoalSchedule.vue";

export default {
  components: {
    CreateGoalCounterMeasure,
    CreateGoalMotivation,
    CreateGoalSchedule,
  },

  data: function() {
    return {
      goal_title:
        "Create Web SPA Todo App  at use Django Rest Framework and Vue.",
      goal_description: "",
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",

      reg: true,
      token:
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwNTkxMzIxLCJqdGkiOiJmYzg4NzYwOWYwNjQ0NGQ1YTFhNGM3YTM5YzM1NmQ1OSIsInVzZXJfaWQiOjF9.d-RDj8eQ2JKd1y5-iEO9uIAM1kjaD5_GFcR3_GWm9NI",
    };
  },

  computed: {
    url() {
      return this.$store.state.url;
    },
  },

  // Goalモデルの新規登録と、登録完了:new_goal_registered = True
  methods: {
    toggle: function() {
      if (this.reg === true) {
        this.reg = false;
      } else {
        this, (this.reg = true);
      }
    },

    newGoalRegister: function(goal_title, goal_description) {
      const vm = this;
      vm.axios
        .post(
          "http://127.0.0.1:8000/api/v1/goals/",
          {
            goal_title: goal_title,
            goal_description: goal_description,
          },
          {
            //  JWT
            headers: {
              "Content-type": "application/json",
              Authorization: `JWT ${vm.token}`,
            },
          }
        )
        .then((response) => (vm.this_time_goal_data = response.data))
        .then((reaponse) => (vm.new_goal_registered = true))
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#goal {
  background-color: #f0f0f0;
  border-radius: 50px;
  padding: 70px;
  margin: 40px 40px 40px 40px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}
#goal:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h1 {
  color: #394e86;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}
.v-stepper {
  box-shadow: none;
}

#back {
  background: #f0f0f0;
}

/* transition */
.goal-enter-active,
.goal-leave-active {
  transition: opacity 0.3s;
}
.goal-enter,
.goal-leave-to {
  opacity: 0;
}
</style>
