<template>
  <div id="countermeasure" class="input_group">
    <v-form v-model="valid">
      <v-container>
        <h2>挫折をしないために準備する</h2>
        <v-row>
          <v-col cols="12" md="12">
            <v-textarea
              name="障壁"
              label="障壁"
              value=""
              hint="行動するにあたって、不安やわからないことをたくさん書いておきましょう"
              rows="1"
              auto-grow
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="2"><v-btn depressed small>＋</v-btn></v-col>
          <v-col cols="9">
            <v-textarea
              name="解決策"
              label="解決策"
              value=""
              hint="前もって障壁に対する解決策を考えておきましょう"
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
            <v-col cols="4">
              <v-text-field
                label="資料"
                hint="参考にしたい資料を前もって登録しておきましょう"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-text-field
                label="用途"
                hint="この資料の用途を書きましょう"
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-text-field label="URL"></v-text-field>
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
