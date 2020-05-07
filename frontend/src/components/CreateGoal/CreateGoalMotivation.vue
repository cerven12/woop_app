<template>
  <div id="motivation" class="input_group">
    <v-container
      ><v-row
        ><v-col cols="12"><h2>▶モチベーションを高めよう</h2></v-col></v-row
      ></v-container
    >
    <v-form v-model="valid">
      <v-container>
        <h3>目標を叶えたい理由を書きましょう</h3>
        <div v-for="(motives, index) in motiveList" v-bind:key="motives.id">
          <div v-if="index >= 1">
            <v-row>
              <v-col cols="11" md="11">
                <v-textarea
                  v-model="motives.motive"
                  rows="1"
                  auto-grow
                  outlined
                ></v-textarea>
              </v-col>
              <v-col cols="1"
                ><v-btn
                  @click="deleteMotiveForm(index)"
                  text
                  depressed
                  height="55"
                  color="error"
                  >✘</v-btn
                ></v-col
              >
            </v-row>
          </div>
          <div v-else>
            <v-row>
              <v-col cols="12">
                <v-textarea
                  v-model="motives.motive"
                  placeholder=""
                  name="理由"
                  label="理由"
                  value=""
                  hint="目標を叶えたい理由を書きましょう"
                  rows="1"
                  outlined
                  auto-grow
                ></v-textarea>
              </v-col>
            </v-row>
          </div>
        </div>
        <!-- The "v-for" ends here. -->
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
          <h3>
            目標を達成したら周囲にどのような良い影響を与えるか、想像してみてください
          </h3>
          <div
            v-for="(self_transcendence_goals,
            index) in selfTranscendenceGoalList"
            v-bind:key="self_transcendence_goals.id"
          >
            <div v-if="index >= 1">
              <v-row>
                <v-col cols="11" md="11">
                  <v-textarea
                    rows="1"
                    auto-grow
                    outlined
                    v-model="self_transcendence_goals.self_transcendence_goal"
                  ></v-textarea>
                </v-col>
                <v-col cols="1"
                  ><v-btn
                    @click="deleteSelfTranscendenceGoalForm(index)"
                    text
                    depressed
                    height="55"
                    color="error"
                    >✘</v-btn
                  ></v-col
                ></v-row
              >
            </div>
            <div v-else>
              <v-row>
                <v-col cols="12" md="12">
                  <v-textarea
                    name="自己超越目標"
                    label="周囲への影響"
                    hint="目標を達成した時、周りの人々や環境にどのような良い影響が与えるか、想像してみてください"
                    rows="1"
                    outlined
                    auto-grow
                    v-model="self_transcendence_goals.self_transcendence_goal"
                  ></v-textarea> </v-col
              ></v-row>
            </div>
          </div>

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
          <h3>
            もし行動しなかった場合。10年度、20年後のあなたの後悔を想像してみましょう
          </h3>

          <div
            v-for="(future_selves, index) in futureSelfList"
            v-bind:key="future_selves.id"
          >
            <div v-if="index >= 1">
              <v-row>
                <v-col cols="11" md="11">
                  <v-textarea
                    rows="1"
                    clearable
                    auto-grow
                    outlined
                    v-model="future_selves.future_self"
                  ></v-textarea>
                </v-col>
                <v-col cols="1">
                  <v-btn
                    @click="deleteFutureSelfForm(index)"
                    text
                    depressed
                    height="55"
                    color="error"
                    >✘</v-btn
                  ></v-col
                ></v-row
              >
            </div>
            <div v-else>
              <v-row>
                <v-col cols="12" md="12">
                  <v-textarea
                    outlined
                    name="後悔"
                    clearable
                    label="後悔"
                    hint="もし行動しなかった場合。10年度、20年後のあなたの後悔を想像してみましょう"
                    rows="1"
                    auto-grow
                    v-model="future_selves.future_self"
                  ></v-textarea> </v-col
              ></v-row>
            </div>
          </div>

          <v-row justify="end">
            <v-col cols="1"
              ><v-btn depressed small @click="addFutureSelf">＋</v-btn></v-col
            >
          </v-row>
          <v-btn @click="allMotivesRegister" outlined>登録！</v-btn>
        </v-container>
      </v-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id"],

  data: function() {
    return {
      this_time_goal_data: "",
      new_goal_registered: false,
      valid: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",

      motiveList: [{ motive: "" }],
      selfTranscendenceGoalList: [{ self_transcendence_goal: "" }],
      futureSelfList: [{ future_self: "" }],
    };
  },
  methods: {
    //  everyメソッドで、最初にformの内容をバリデーションできそう。

    // Dynamically increase the form
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

    // Delete Form
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
    motivesRegister: function() {
      const vm = this;
      this.motiveList.forEach(function(motives) {
        // Remove spaces and null strings
        const judgeStr = motives.motive.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
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
        const judgeStr = self_transcendence_goals.self_transcendence_goal.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (judgeStr) {
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
        const judgeStr = future_selves.future_self.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (judgeStr) {
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
  },
};
</script>

<style scoped>
#motivation {
  background-color: #f0f0f0;

  /* border: 1px black solid; */
  border-radius: 50px;
  padding: 40px 20px 40px 20px;
  margin: 40px 20px 40px 20px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}

#motivation:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h2,
h3 {
  color: rgb(83, 83, 83);
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
