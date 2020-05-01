<template>
  <div id="motivation" class="input_group">
    親は{{ goal_id }}
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <h2>モチベーションを高める</h2>
          <v-col cols="12" md="12">
            <div v-for="motives in motiveList" v-bind:key="motives.id">
              <v-textarea
                v-model="motives.motive"
                placeholder=""
                name="理由"
                label="理由"
                value=""
                hint="目標を叶えたい理由を書きましょう"
                rows="1"
                auto-grow
              ></v-textarea>
            </div>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="1"
            ><v-btn depressed small @click="addMotiveForm">＋</v-btn></v-col
          >
        </v-row>
      </v-container>
    </v-form>

    <div>
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="12" md="12">
              <div
                v-for="self_transcendence_goals in selfTranscendenceGoalList"
                v-bind:key="self_transcendence_goals.id"
              >
                <v-textarea
                  name="自己超越目標"
                  label="周囲への影響"
                  hint="目標を達成した時、周りの人々や環境にどのような良い影響が与えるか、想像してみてください"
                  rows="1"
                  auto-grow
                  v-model="self_transcendence_goals.self_transcendence_goal"
                ></v-textarea>
              </div>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="1"
              ><v-btn depressed small @click="addSelfTranscendenceGoalForm"
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
          <v-row>
            <v-col cols="12" md="12">
              <div
                v-for="future_selves in futureSelfList"
                v-bind:key="future_selves.id"
              >
                <v-textarea
                  name="後悔"
                  label="後悔"
                  hint="もし行動しなかった場合。10年度、20年後のあなたの後悔を想像してみましょう"
                  rows="1"
                  auto-grow
                  v-model="future_selves.future_self"
                ></v-textarea>
              </div>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="1"
              ><v-btn depressed small @click="addFutureSelf">＋</v-btn></v-col
            >
          </v-row>
        </v-container>
      </v-form>

      <v-btn @click="allMotivesRegister">All Motivations register</v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id"],

  data: function() {
    return {
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",
      motive: "",
      self_transcendence_goal: "",
      future_self: "",

      motiveList: [{ motive: "" }],
      selfTranscendenceGoalList: [{ self_transcendence_goal: "" }],
      futureSelfList: [{ future_self: "" }],
    };
  },
  methods: {
    addMotiveForm: function() {
      const form = { motive: "" };
      this.motiveList.push(form);
    },

    addSelfTranscendenceGoalForm: function() {
      const form = { motive: "" };
      this.selfTranscendenceGoalList.push(form);
    },

    addFutureSelf: function() {
      const form = { future_self: "" };
      this.futureSelfList.push(form);
    },

    motivesRegister: function() {
      const vm = this;
      this.motiveList.forEach(function(motives) {
        const judgementStr = motives.motive.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgementStr) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "motives/", {
              goal: vm.goal_id,
              motive: motives.motive,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log(`その文字列はだめです`);
        }
      });
    },

    selfTranscendenceGoalListRegister: function() {
      const vm = this;
      this.selfTranscendenceGoalList.forEach(function(
        self_transcendence_goals
      ) {
        const judgementStr = self_transcendence_goals.self_transcendence_goal.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (self_transcendence_goals.self_transcendence_goal) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "self_transcendence_goals/", {
              goal: vm.goal_id,
              self_transcendence_goal:
                self_transcendence_goals.self_transcendence_goal,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log("その文字列はだめです");
        }
      });
    },

    futureSelvesRegister: function() {
      const vm = this;
      this.futureSelfList.forEach(function(future_selves) {
        const judgementStr = future_selves.future_self.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (future_selves.future_self) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "future_selves/", {
              goal: vm.goal_id,
              future_self: future_selves.future_self,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log("その文字列はだめ");
        }
      });
    },

    allMotivesRegister: function() {
      this.motivesRegister();
      this.selfTranscendenceGoalListRegister();
      this.futureSelvesRegister();
    },

    // プロミスでaxiosの処理を配列に格納して、増えた文のフォームを格納すればmultipleなフォームも一気にpostできそう
    // allGet: function(){
    //   const vm = this;
    //   const rq = [
    //     vm.axios.post(vm.url, { goal_title: 'jsfidle1', goal_description: 'テストです' }),
    //     vm.axios.post(vm.url, { goal_title: 'jsfidle2', goal_description: 'テストです' }),
    //     vm.axios.post(vm.url, { goal_title: 'jsfidle3', goal_description: 'テストです' }),
    //   ];
    //   Promise.all(rq).then((rq1, rq2, rq3)=> {vm.rq = (rq1, rq2, rq3)})
    //   console.log(vm.rq)
    // }
  },
};
</script>

<style scoped>
.input_group {
  margin: 20px;
  transition: all 0.2s;
}

#motivation {
  /* background: rgba(105, 105, 105, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#countermeasure {
  /* background: rgba(79, 79, 80, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#goal {
  padding: 20px;
}
.v-stepper {
  box-shadow: none;
}
</style>

<style>
.v-messages {
  font-size: 15px;
}
.v-messages__message {
  padding-top: 2px;
}
</style>
