<template>
  <div id="motivation" class="input_group">
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <h2>モチベーションを高める</h2>
          <v-col cols="12" md="12">
            <v-textarea
              placeholder=""
              name="理由"
              label="理由"
              value=""
              hint="目標を叶えたい理由を書きましょう"
              rows="1"
              auto-grow
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
        </v-row>
      </v-container>
    </v-form>
    <div>
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="12" md="12">
              <v-textarea
                name="自己超越目標"
                label="周囲への影響"
                value=""
                hint="目標を達成した時、周りの人々や環境にどのような良い影響が与えるか、想像してみてください"
                rows="1"
                auto-grow
              ></v-textarea>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
    <div>
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="12" md="12">
              <v-textarea
                name="後悔"
                label="後悔"
                value=""
                hint="もし行動しなかった場合。10年度、20年後のあなたの後悔を想像してみましょう"
                rows="1"
                auto-grow
              ></v-textarea>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",

  data: function() {
    return {
      goal_title:
        "Django Rest FrameworkとVue CLI&Vuetifyで、SPAなタスク管理アプリケーションを作成する。",
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
      valid: "",
    };
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
</style>
