<template>
  <div>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="12">
            <div v-for="worries in worryList" v-bind:key="worries.id">
              <v-textarea
                name="障壁"
                label="障壁"
                hint="行動するにあたって、不安やわからないことをたくさん書いておきましょう"
                rows="1"
                outlined
                auto-grow
                v-model="worries.worry"
              ></v-textarea>
            </div>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="2"></v-col>
          <v-col cols="9">
            <div v-for="(ideas, index) in ideaList" v-bind:key="ideas.id">
              <div v-if="index >= 1">
                <v-textarea
                  rows="1"
                  auto-grow
                  outlined
                  v-model="ideas.idea"
                ></v-textarea>
              </div>
              <div v-else>
                <v-textarea
                  name="解決策"
                  label="解決策"
                  hint="前もって障壁に対する解決策を考えておきましょう"
                  rows="1"
                  auto-grow
                  outlined
                  v-model="ideas.idea"
                ></v-textarea>
              </div>
            </div>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="1"
            ><v-btn depressed small @click="addIdeaForm">＋</v-btn></v-col
          >
        </v-row>
        <v-btn outlined @click="worryRegister">障害と対策の登録OK</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
"use strict";

export default {
  name: "CreateGoal",
  props: ["goal_id"],

  data: function() {
    return {
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",

      worryList: [{ worry: "" }],
      ideaList: [{ idea: "" }],
      parentWorryId: "",
    };
  },
  methods: {
    addIdeaForm: function() {
      const form = { idea: "" };
      this.ideaList.push(form);
    },

    // worryとideaを同時に登録するメソッド
    worryRegister: function() {
      let vm = this;
      // worryListを１つずつ取り出して、axios.postする
      vm.worryList.forEach(function(worries) {
        let judgeStr = worries.worry.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "worries/", {
              goal: vm.goal_id,
              worry: worries.worry,
            })
            .then((res) => {
              vm.parentWorryId = res.data.worry_id;
              // 現在のworryに対するideaを、ideaListから１つずつ取り出して順番にaxios.post
              vm.ideaRegister(vm.parentWorryId);
            })
            // worryのaxios.postでエラーだった時にキャッチ↓
            // worryのpostがエラーを吐いた場合は、そのworryに対するideaの登録はスキップされる。
            .catch((error) => {
              console.log(`ideaのエラーです${error}`);
            });
          // worryのフォームに入力された情報が`if (judgementStr)`でfalseならここまで飛ぶ
        } else {
          console.log("そのworryの文字列は認められませんね。");
        }
      });
    },

    ideaRegister: function(parentWorryId) {
      const vm = this;
      vm.ideaList.forEach(function(ideas) {
        let judgeStr = ideas.idea.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/worries/" + parentWorryId + "/ideas/",
              {
                worry: parentWorryId,
                idea: ideas.idea,
              }
            )
            .then((res) => (vm.this_time_goal_data = res.data))
            .catch((error) => {
              console.log(`worryのエラーです${error}`);
            });
        } else {
          console.log(`そのideaの文字列はだめです`);
        }
      });
    },
  },
};
</script>

<style scoped></style>
